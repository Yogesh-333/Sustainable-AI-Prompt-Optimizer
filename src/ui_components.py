# src/ui_components.py

import streamlit as st

def set_page_config_and_css():
    """Sets Streamlit page configuration and injects custom CSS for styling."""
    st.set_page_config(
        page_title="Sustainable AI Prompt Optimizer",
        page_icon="💡",
        layout="centered",
        initial_sidebar_state="auto"
    )

    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
        .stApp {
            background: linear-gradient(to bottom right, #e0f2fe, #e8eaf6); /* Light blue to light indigo gradient */
            color: #333;
        }
        .stButton>button {
            background-color: #2563eb; /* Blue-600 */
            color: white;
            font-weight: bold;
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        }
        .stButton>button:hover {
            background-color: #1d4ed8; /* Blue-700 */
            transform: scale(1.02);
        }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>select {
            border: 1px solid #93c5fd; /* Blue-300 */
            border-radius: 0.5rem;
            padding: 0.75rem;
            font-size: 1.125rem;
        }
        .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus, .stSelectbox>div>div>select:focus {
            border-color: #3b82f6; /* Blue-500 */
            box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.5);
        }
        .stAlert {
            border-radius: 0.5rem;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .main .block-container {
            max-width: 960px; /* max-w-4xl */
        }
        .css-1d391kg { /* Target for main content container */
            background-color: #ffffff;
            border-radius: 0.75rem;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
            padding: 2.5rem;
            border: 1px solid #bfdbfe;
        }
        .input-section-bg {
            background-color: #eff6ff; /* Blue-50 */
            border-radius: 0.5rem;
            box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);
            border: 1px solid #bfdbfe;
            padding: 1.5rem;
            margin-bottom: 2rem;
        }
        .results-section-bg {
            background-color: #ecfdf5; /* Green-50 */
            border-radius: 0.5rem;
            box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);
            border: 1px solid #a7f3d0;
            padding: 1.5rem;
        }
        .metric-card {
            background-color: #ffffff;
            padding: 1.25rem;
            border-radius: 0.5rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06);
            border: 1px solid #e5e7eb;
        }
        .stProgress > div > div {
            background-color: #8b5cf6; /* Purple-500 */
        }
        h1 {
            color: #1e40af; /* Blue-800 */
            text-align: center;
            font-weight: 800;
            font-size: 2.5rem; /* text-4xl */
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.75rem;
        }
        h2 {
            color: #065f46; /* Green-800 */
            font-weight: 700;
            font-size: 2rem; /* text-3xl */
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        h3 {
            color: #1f2937; /* Gray-800 */
            font-weight: 600;
            font-size: 1.5rem; /* text-2xl */
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .stMarkdown p {
            font-size: 1.125rem; /* text-lg */
            color: #4b5563; /* Gray-700 */
        }

        /* Specific styling for the new metric cards */
        .energy-original-card {
            background-color: #e0f7fa; /* Light cyan */
            border: 1px solid #80deea; /* Darker cyan border */
        }
        .energy-optimized-card {
            background-color: #e8f5e9; /* Light green */
            border: 1px solid #a5d6a7; /* Darker green border */
        }
        .savings-card {
            background-color: #f3e5f5; /* Light purple */
            border: 1px solid #ce93d8; /* Darker purple border */
        }
        .similarity-card {
            background-color: #fff3e0; /* Light orange */
            border: 1px solid #ffcc80; /* Darker orange border */
        }
        .metric-value-large {
            font-size: 2.5rem; /* text-4xl */
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .metric-value-large.blue { color: #2563eb; } /* Blue-600 */
        .metric-value-large.green { color: #10b981; } /* Green-500 */
        .metric-value-large.purple { color: #8b5cf6; } /* Purple-500 */
        .metric-value-large.orange { color: #f97316; } /* Orange-500 */ /* NEW COLOR CLASS */
        </style>
        """,
        unsafe_allow_html=True
    )

def render_sidebar():
    """Renders the sidebar content for project context and disclaimer."""
    with st.sidebar:
        st.header("About This Project 💡")
        st.markdown(
            """
            This application demonstrates **Sustainable AI - Transparency and Energy-Efficient Prompt/Context Engineering**.
            
            As AI models become more resource-intensive, understanding and optimizing their energy consumption is critical. This tool provides a mock estimation of prompt energy usage and suggests more efficient alternatives.
            
            **Key Features:**
            - Estimate energy consumption of AI prompts.
            - Suggest energy-efficient prompt alternatives.
            - Analyze potential energy savings.
            
            **Disclaimer:** All energy estimates and complexity scores are **mock values** based on simple heuristics and a pre-defined database. This application is for demonstration purposes only and does not reflect real-world LLM energy consumption accurately.
            """
        )
        st.markdown("---")
        st.info("Developed for the 'Foundations of Machine Learning Frameworks (CSCN8010)' final project.")

def render_main_header():
    """Renders the main header and subtitle of the application."""
    st.markdown(
        """
        <h1><img src="https://api.iconify.design/lucide/lightbulb.svg?color=%23facc15" width="48" height="48" /> Sustainable AI Prompt Optimizer</h1>
        <p style="text-align: center; font-size: 1.25rem; color: #4b5563; margin-bottom: 2rem;">
            Estimate energy usage and optimize your AI prompts for efficiency.
        </p>
        """,
        unsafe_allow_html=True
    )

def render_results_section():
    """
    Renders the results display section of the application with enhanced visuals.
    Assumes results are stored in st.session_state.
    """
    if 'original_energy' in st.session_state and st.session_state['original_energy'] is not None:
        st.markdown('<div class="results-section-bg">', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: #065f46;"><img src="https://api.iconify.design/lucide/trending-up.svg?color=%23065f46" width="32" height="32" /> Analysis Results ({st.session_state.get("optimization_mode_display", "Unknown Mode")})</h2>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"""
                <div class="metric-card energy-original-card">
                    <h3 style="color: #1f2937;">Original Prompt Energy Estimate:</h3>
                    <p class="metric-value-large blue">
                        {st.session_state['original_energy']:.4f} kWh
                        <img src="https://api.iconify.design/lucide/zap.svg?color=%232563eb" width="32" height="32" />
                    </p>
                    <p style="color: #4b5563; font-size: 0.9rem;">
                        Estimated for a <span style="font-weight: 600; color: #1e40af;">{st.session_state['llm_size_display']}</span> LLM.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="metric-card energy-optimized-card">
                    <h3 style="color: #1f2937;">Optimized Energy Estimate:</h3>
                    <p class="metric-value-large green">
                        {st.session_state['optimized_energy']:.4f} kWh
                        <img src="https://api.iconify.design/lucide/leaf.svg?color=%2310b981" width="32" height="32" />
                    </p>
                    <p style="color: #4b5563; font-size: 0.9rem;">
                        Using the suggested optimized prompt.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("---")

        st.markdown('<h3 style="color: #1f2937;"><img src="https://api.iconify.design/lucide/sparkles.svg?color=%23facc15" width="24" height="24" /> Optimized Prompt Suggestion:</h3>', unsafe_allow_html=True)
        st.info(f"**\"{st.session_state['optimized_prompt']}\"**")
        st.markdown(
            """
            <p style="color: #4b5563; font-size: 0.9rem;">
                This is a semantically similar prompt from our optimized database, designed for lower energy consumption.
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.markdown('<h3 style="color: #1f2937;"><img src="https://api.iconify.design/lucide/bar-chart-2.svg?color=%238b5cf6" width="24" height="24" /> Energy Savings Analytics:</h3>', unsafe_allow_html=True)

        energy_savings = st.session_state['original_energy'] - st.session_state['optimized_energy']
        savings_percentage = (energy_savings / st.session_state['original_energy']) * 100 if st.session_state['original_energy'] else 0

        col_analytics1, col_analytics2, col_analytics3 = st.columns(3)

        with col_analytics1:
            st.markdown(
                f"""
                <div class="metric-card savings-card">
                    <p style="font-size: 1.125rem; font-weight: 500; color: #4b5563;">Potential Savings:</p>
                    <p class="metric-value-large purple">
                        {energy_savings:.4f} kWh
                        <img src="https://api.iconify.design/lucide/arrow-down-circle.svg?color=%238b5cf6" width="32" height="32" />
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_analytics2:
            st.markdown(
                f"""
                <div class="metric-card savings-card">
                    <p style="font-size: 1.125rem; font-weight: 500; color: #4b5563;">Savings Percentage:</p>
                    <p class="metric-value-large purple">
                        {savings_percentage:.2f}%
                        <img src="https://api.iconify.design/lucide/percent.svg?color=%238b5cf6" width="32" height="32" />
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_analytics3:
            st.markdown(
                f"""
                <div class="metric-card similarity-card">
                    <p style="font-size: 1.125rem; font-weight: 500; color: #4b5563;">Similarity to Original:</p>
                    <p class="metric-value-large orange">
                        {st.session_state['similarity_score']:.0f}%
                        <img src="https://api.iconify.design/lucide/check-circle.svg?color=%23f97316" width="32" height="32" />
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.progress(float(st.session_state['similarity_score']) / 100)
        st.markdown(
            """
            <p style="font-size: 0.9rem; color: #6b7280;">
                Higher similarity indicates the optimized prompt closely matches the intent of your original prompt.
            </p>
            """,
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True) # Close results-section-bg div
