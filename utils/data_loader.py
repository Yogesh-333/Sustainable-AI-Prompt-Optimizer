import streamlit as st
from data.optimized_prompts import example_optimized_prompts

@st.cache_data(show_spinner="Pre-computing example optimized prompt embeddings...")
def get_example_optimized_embeddings(prompts: list, _model) -> dict:
    """
    Generates and caches embeddings for the example optimized prompt database.
    
    Args:
        prompts: A list of example optimized prompt strings.
        _model: The SentenceTransformer model (prefixed with _ to avoid hashing issues).
        
    Returns:
        A dictionary where keys are "example_1", "example_2", etc., and values are their embeddings.
    """
    return {f"example_{i+1}": _model.encode(p) for i, p in enumerate(prompts)}
