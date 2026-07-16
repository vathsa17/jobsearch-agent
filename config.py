"""
Application configuration.

Loads environment variables and exposes constants that are used
throughout the application.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# -----------------------------------------------------
# Load .env
# -----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

# -----------------------------------------------------
# Paths
# -----------------------------------------------------

DATA_DIR = BASE_DIR / "data"
CV_DIR = BASE_DIR / "cv"
REPORT_DIR = BASE_DIR / "reports"
TEMPLATE_DIR = BASE_DIR / "templates"

DATABASE_FILE = DATA_DIR / "jobs.db"
CV_FILE = CV_DIR / "cv.txt"

# Create folders if they don't exist
DATA_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)

# -----------------------------------------------------
# OpenRouter
# -----------------------------------------------------

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_URL = "https://openrouter.ai/api/v1"

MODEL = "deepseek/deepseek-chat-v3-0324"

# Better alternatives later:
# MODEL = "google/gemini-2.5-flash"
# MODEL = "openai/gpt-4.1-mini"

# -----------------------------------------------------
# Jobsuche
# -----------------------------------------------------

JOBSUCHE_API_KEY = "jobboerse-jobsuche"

JOBSUCHE_URL = (
    "https://rest.arbeitsagentur.de/"
    "jobboerse/jobsuche-service/pc/v6/jobs"
)

SEARCH_TERMS = [
    "Salesforce",
    "Salesforce Developer",
    "Salesforce Consultant",
    "Salesforce Administrator",
    "Sales Cloud",
    "Service Cloud",
    "CRM",
]

SEARCH_LOCATION = os.getenv("SEARCH_LOCATION", "Deutschland")

# -----------------------------------------------------
# Matching
# -----------------------------------------------------

MIN_SCORE = int(os.getenv("MIN_SCORE", 85))

MAX_OUTPUT_TOKENS = 500

TEMPERATURE = 0

# -----------------------------------------------------
# Email
# -----------------------------------------------------

SMTP_SERVER = os.getenv("SMTP_SERVER")

SMTP_PORT = int(os.getenv("SMTP_PORT", 465))

SMTP_USERNAME = os.getenv("SMTP_USERNAME")

SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

EMAIL_FROM = os.getenv("EMAIL_FROM")

EMAIL_TO = os.getenv("EMAIL_TO")

# -----------------------------------------------------
# Logging
# -----------------------------------------------------

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")