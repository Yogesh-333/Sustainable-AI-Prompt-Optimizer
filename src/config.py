# src/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Your Gemini API Key.
# It will now be read from the environment variable GEMINI_API_KEY.
# For production, ensure this variable is set in your deployment environment.
API_KEY = os.getenv("GEMINI_API_KEY") 

# Base energy factors (mock values - replace with real data/models in a production system)
BASE_ENERGY_PER_COMPLEXITY = 0.08  # kWh per unit of complexity (0-100)
LLM_SIZE_MULTIPLIERS = {
    'small': 0.8,
    'medium': 1.5,
    'large': 2.5,
}
