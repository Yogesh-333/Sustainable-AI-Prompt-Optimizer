import streamlit as st
import numpy as np

# Import functions from our custom modules
from src.config import API_KEY, BASE_ENERGY_PER_COMPLEXITY, LLM_SIZE_MULTIPLIERS
from src.optimization_logic import (
    load_embedding_model,
    get_prompt_embedding,
    find_most_similar_example_prompt,
    estimate_local_complexity,
    perform_gemini_optimization
)
from src.ui_components import (
    set_page_config_and_css,
    render_sidebar,
    render_main_header,
    render_results_section # NEW IMPORT
)
from utils.data_loader import get_example_optimized_embeddings, example_optimized_prompts

# --- Initialize Models and Data ---
embedding_model = load_embedding_model()
example_optimized_prompt_embeddings = get_example_optimized_embeddings(example_optimized_prompts, embedding_model)

# --- Streamlit UI Setup ---
set_page_config_and_css()
render_sidebar()
render_main_header()

# --- Input Section ---
with st.container(border=False):
    st.markdown('<div class="input-section-bg">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #1e40af;"><img src="https://api.iconify.design/lucide/edit.svg?color=%231e40af" width="24" height="24" /> Your AI Prompt:</h3>', unsafe_allow_html=True)
    user_prompt = st.text_area(
        "Enter your prompt here:",
        placeholder="e.g., 'Generate a detailed report on the global climate change impacts of industrialization over the last two centuries, including socio-economic factors and future projections.'",
        height=150,
        label_visibility="collapsed"
    )

    st.markdown('<h3 style="color: #1e40af; margin-top: 1.5rem;"><img src="https://api.iconify.design/lucide/hard-drive.svg?color=%231e40af" width="24" height="24" /> Target LLM Size:</h3>', unsafe_allow_html=True)
    llm_size = st.selectbox(
        "Select the size of the Large Language Model:",
        ('small', 'medium', 'large'),
        format_func=lambda x: {
            'small': 'Small (e.g., Llama 3 8B)',
            'medium': 'Medium (e.g., Gemini 1.5 Flash)',
            'large': 'Large (e.g., GPT-4o, Gemini 1.5 Pro)'
        }[x],
        label_visibility="collapsed"
    )

    st.markdown('<h3 style="color: #1e40af; margin-top: 1.5rem;"><img src="https://api.iconify.design/lucide/settings.svg?color=%231e40af" width="24" height="24" /> Optimization Method:</h3>', unsafe_allow_html=True)
    optimization_mode = st.radio(
        "Choose how to optimize your prompt:",
        ("Local Heuristic Optimization", "Generative AI Optimization (Gemini API)"),
        index=0, # Default to local heuristic
        horizontal=True,
        label_visibility="collapsed"
    )

    if st.button("⚡ Analyze Energy & Optimize", use_container_width=True):
        if not user_prompt.strip():
            st.error("Please enter a prompt to analyze.")
        else:
            with st.spinner(f"Analyzing prompt and calculating energy estimates using {optimization_mode}..."):
                try:
                    original_energy_calc = 0.0
                    optimized_energy_calc = 0.0
                    most_similar_optimized_prompt = ""
                    similarity_score = 0.0

                    if optimization_mode == "Local Heuristic Optimization":
                        user_prompt_embedding = get_prompt_embedding(user_prompt, embedding_model)
                        most_similar_optimized_prompt, similarity_score = find_most_similar_example_prompt(
                            user_prompt_embedding, example_optimized_prompt_embeddings, example_optimized_prompts
                        )
                        original_prompt_complexity = estimate_local_complexity(user_prompt)
                        optimized_prompt_complexity = estimate_local_complexity(most_similar_optimized_prompt)

                    elif optimization_mode == "Generative AI Optimization (Gemini API)":
                        # This mode uses Gemini API for generation and complexity estimation
                        result = perform_gemini_optimization(user_prompt, example_optimized_prompts, API_KEY)
                        
                        most_similar_optimized_prompt = result["generatedOptimizedPrompt"]
                        similarity_score = result["similarityScore"]
                        original_prompt_complexity = result["originalPromptComplexity"]
                        optimized_prompt_complexity = result["optimizedPromptComplexity"]
                        
                        if not all([most_similar_optimized_prompt, similarity_score is not None, original_prompt_complexity is not None, optimized_prompt_complexity is not None]):
                             raise ValueError("Gemini API did not return all expected data.")

                    # Calculate mock energy based on complexity and LLM size (common to both modes)
                    original_energy_calc = (original_prompt_complexity / 100) * BASE_ENERGY_PER_COMPLEXITY * LLM_SIZE_MULTIPLIERS[llm_size]
                    optimized_energy_calc = (optimized_prompt_complexity / 100) * BASE_ENERGY_PER_COMPLEXITY * LLM_SIZE_MULTIPLIERS[llm_size]

                    st.session_state['original_energy'] = original_energy_calc
                    st.session_state['optimized_prompt'] = most_similar_optimized_prompt
                    st.session_state['optimized_energy'] = optimized_energy_calc
                    st.session_state['similarity_score'] = float(similarity_score) # Cast to float
                    st.session_state['llm_size_display'] = llm_size # Store for display
                    st.session_state['optimization_mode_display'] = optimization_mode # Store for display
                    
                except Exception as e:
                    st.error(f"An error occurred during analysis using {optimization_mode}: {e}. Please ensure API key is valid for Generative AI mode, or all libraries are installed for Local mode.")
                    st.session_state['original_energy'] = None # Reset state on error
    st.markdown('</div>', unsafe_allow_html=True) # Close input-section-bg div


render_results_section()

st.markdown("---")
st.markdown(
    """
    <p style="text-align: center; font-size: 0.8rem; color: #6b7280;">
        Powered by Local Machine Learning Models and/or Google Gemini API and Streamlit.
    </p>
    """,
    unsafe_allow_html=True
)
