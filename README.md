💡 Sustainable AI Prompt Optimizer
Project Overview
The rapid expansion of Artificial Intelligence (AI) data centers poses significant environmental challenges, including surging electricity demand, increased carbon emissions, and substantial water usage. With upcoming regulations like the EU's energy usage reporting requirement by August 2026, there's a critical need for transparency in AI energy consumption and dynamic workload optimization.

This project, "Sustainable AI - Transparency and Energy-Efficient Prompt/Context Engineering with Machine Learning," addresses these concerns by providing a tool to estimate the energy consumption of Large Language Model (LLM) prompts and suggest more energy-efficient alternatives. It demonstrates how machine learning and prompt engineering can contribute to more sustainable AI practices.

✨ Features
Mock Energy Estimation: Provides a simulated energy consumption (in kWh) for user-defined AI prompts based on their complexity and the selected LLM size.

Prompt Optimization Strategies: Offers two distinct methods for optimizing prompts:

Local Heuristic Optimization: Uses local semantic models (sentence-transformers) and heuristic rules to find the most similar pre-optimized prompt from a curated database.

Generative AI Optimization (Gemini API): Leverages the Google Gemini API to dynamically generate a concise and energy-efficient version of the user's prompt, along with AI-estimated complexity and similarity scores.

Detailed Analytics View: Presents clear, visually enhanced metrics including:

Original Prompt Energy Estimate

Optimized Prompt Energy Estimate

Potential Energy Savings (kWh and percentage)

Semantic Similarity Score (between original and optimized prompts)

Professional UI: Built with Streamlit, featuring a clean, responsive, and intuitive user interface with custom CSS for enhanced aesthetics.

Modular Codebase: Organized into a clean folder structure (src/, utils/, data/) for maintainability and scalability.

Secure API Key Handling: Utilizes .env files for securely managing the Gemini API key during local development.

🚀 How It Works
The application processes user input through the following steps:

Prompt Input: The user enters a natural language prompt and selects a target LLM size (Small, Medium, Large).

Optimization Method Selection: The user chooses between "Local Heuristic Optimization" and "Generative AI Optimization (Gemini API)".

Analysis & Optimization:

Local Heuristic Mode:

The sentence-transformers model generates a vector embedding for the user's prompt.

It finds the most semantically similar prompt from a pre-defined, energy-efficient prompt database.

Prompt complexity (for both original and optimized) is estimated using a local heuristic based on length, unique words, and average word length.

Generative AI Mode (Gemini API):

The user's prompt is sent to the Google Gemini API.

The Gemini model is instructed to generate a concise, energy-efficient version of the prompt.

Gemini also provides complexity scores for both the original and generated prompts, and a semantic similarity score between them.

Mock Energy Prediction: Based on the estimated complexity (from either local heuristics or Gemini) and the chosen LLM size, the application calculates a mock energy consumption value.

Results Display: All energy estimates, savings, and similarity scores are presented in a visually enhanced analytics dashboard.

🛠️ Installation and Setup
To run this application locally, follow these steps:

1. Clone the Repository (Optional, if you've already set up locally)
If you're starting fresh, clone your project repository:

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME # Replace with your actual repository name (e.g., sustainable_ai_app)

2. Create Project Structure (If not cloned from Git)
If you're setting up the files manually, ensure your project has the following structure:

sustainable_ai_app/
├── app.py
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── optimization_logic.py
│   └── ui_components.py
├── utils/
│   ├── __init__.py
│   └── data_loader.py
└── data/
    ├── __init__.py
    └── optimized_prompts.py
├── .env                 # Will be created in step 4
├── .gitignore           # Will be created in step 5
└── requirements.txt     # Will be created in step 3

3. Create a Virtual Environment (Recommended)
It's best practice to use a virtual environment to manage dependencies.

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

4. Install Dependencies
Install all required Python packages using the requirements.txt file.

pip install -r requirements.txt

requirements.txt content:

streamlit==1.36.0
numpy==1.26.4
sentence-transformers==2.7.0
scipy==1.13.1
google-generativeai==0.7.0
python-dotenv==1.0.0

5. Set Up Your Gemini API Key Securely
For the "Generative AI Optimization (Gemini API)" mode, you'll need a Google Gemini API key.

Obtain an API key from Google AI Studio.

In the root directory of your project (sustainable_ai_app/), create a new file named .env.

Add your API key to this file:

# .env
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"

Replace "YOUR_GEMINI_API_KEY_HERE" with your actual key.

6. Create or Update .gitignore
To prevent accidentally committing your .env file (which contains your API key) to Git, ensure you have a .gitignore file in your project's root directory with the following content:

# .gitignore
.env
venv/
__pycache__/
*.pyc
.streamlit/

🚀 Usage
Once all dependencies are installed and your .env file is set up, you can run the Streamlit application from your project's root directory:

streamlit run app.py

This command will open the application in your default web browser.

⚠️ Disclaimer
All energy estimates and complexity scores provided by this application are mock values based on simple heuristics and a pre-defined database (or simulated generative logic). This application is intended for demonstration purposes only and does not reflect real-world LLM energy consumption or optimization accurately.

🤝 Contributing
Feel free to fork this repository, open issues, or submit pull requests. Contributions to improve the mock models, add more sophisticated heuristics, or expand the optimized prompt database are welcome!

Developed for the 'Foundations of Machine Learning Frameworks (CSCN8010)' final project.
