# src/optimization_logic.py

import streamlit as st
import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
import re
import json
import google.generativeai as genai

from src.config import API_KEY # Import API_KEY from config

# --- Model Initialization ---
@st.cache_resource(show_spinner="Loading AI model for embeddings...")
def load_embedding_model():
    """Caches and loads the SentenceTransformer model."""
    return SentenceTransformer('all-MiniLM-L6-v2')

# Configure Gemini model for content generation with structured output
genai.configure(api_key=API_KEY)
gemini_model = genai.GenerativeModel(
    'gemini-2.5-flash-preview-05-20',
    generation_config={
        "response_mime_type": "application/json",
        "response_schema": {
            "type": "OBJECT",
            "properties": {
                "generatedOptimizedPrompt": {"type": "STRING"},
                "similarityScore": {"type": "NUMBER"},
                "originalPromptComplexity": {"type": "NUMBER"},
                "optimizedPromptComplexity": {"type": "NUMBER"}
            },
        }
    }
)

# --- Core Logic Functions ---

def get_prompt_embedding(prompt: str, model: SentenceTransformer) -> np.ndarray:
    """
    Generates a dense vector embedding for a given prompt using the pre-trained local model.
    """
    return model.encode(prompt)

def find_most_similar_example_prompt(user_embedding: np.ndarray, 
                                     example_embeddings: dict, 
                                     example_prompts_list: list) -> tuple[str, float]:
    """
    Finds the most semantically similar example prompt from the database using cosine similarity.
    This is used for the "Local Heuristic Optimization" mode.
    
    Args:
        user_embedding: The vector embedding of the user's input prompt.
        example_embeddings: A dictionary of pre-computed embeddings for example optimized prompts.
        example_prompts_list: The list of example optimized prompt strings.
        
    Returns:
        A tuple containing the most similar example prompt text and its cosine similarity score (0-100).
    """
    most_similar_prompt = ""
    highest_similarity = -1.0
    
    # Iterate through the dictionary of pre-computed embeddings
    for key, example_embedding in example_embeddings.items():
        similarity = 1 - cosine(user_embedding, example_embedding)
        if similarity > highest_similarity:
            highest_similarity = similarity
            # Retrieve the prompt string using its index or key from the original list/dict
            # Assuming keys are like "example_1", "example_2"
            prompt_index = int(key.split('_')[1]) - 1
            most_similar_prompt = example_prompts_list[prompt_index]
            
    return most_similar_prompt, highest_similarity * 100 # Convert to 0-100 scale

def estimate_local_complexity(prompt: str) -> float:
    """
    A heuristic function to estimate prompt complexity locally.
    This version considers prompt length, number of unique words, and average word length.
    
    Args:
        prompt: The raw prompt string.
        
    Returns:
        A complexity score between 0 and 100.
    """
    words = re.findall(r'\b\w+\b', prompt.lower())
    num_words = len(words)
    num_unique_words = len(set(words))
    
    if num_words == 0:
        return 0.0

    avg_word_length = sum(len(word) for word in words) / num_words

    length_score = min(num_words / 50, 1.0)
    unique_word_score = min(num_unique_words / 30, 1.0)
    avg_word_length_score = min(avg_word_length / 8, 1.0)

    complexity = (length_score * 0.4 + unique_word_score * 0.3 + avg_word_length_score * 0.3) * 100
    
    return max(0.0, min(100.0, complexity))

def perform_gemini_optimization(user_prompt: str, example_optimized_prompts: list, api_key: str) -> dict:
    """
    Performs prompt optimization and complexity estimation using the Gemini API.
    
    Args:
        user_prompt: The user's original raw prompt string.
        example_optimized_prompts: A list of example optimized prompts to guide Gemini.
        api_key: The Gemini API key.
        
    Returns:
        A dictionary containing generatedOptimizedPrompt, similarityScore, 
        originalPromptComplexity, and optimizedPromptComplexity.
    """
    # Ensure API key is configured before making the call
    genai.configure(api_key=api_key)

    # The prompt now asks Gemini to GENERATE the optimized prompt
    gemini_prompt_text = f"""Given the user prompt: "{user_prompt}".
    
    Your task is to generate a concise and energy-efficient version of this prompt.
    Also, provide:
    1.  A 'complexity score' for the user's original prompt (a number between 0 and 100, where higher complexity generally implies more computational effort and thus higher energy consumption).
    2.  A 'complexity score' for the generated optimized prompt (a number between 0 and 100).
    3.  A 'similarity score' between the original prompt and your generated optimized prompt (a number between 0 and 100, where 100 is identical).
    
    Return the results in JSON format.
    
    Example of desired optimized prompts are: {json.dumps(example_optimized_prompts)}.
    """
    
    response = gemini_model.generate_content(gemini_prompt_text)
    
    # Extract the JSON string from the response
    response_text = response.candidates[0].content.parts[0].text
    parsed_data = json.loads(response_text)
    
    return parsed_data
