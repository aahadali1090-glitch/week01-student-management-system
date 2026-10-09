
import os
from pathlib import Path
from dotenv import load_dotenv

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Load environment variables
load_dotenv(BASE_DIR / ".env")

APP_NAME = os.getenv("APP_NAME", "Student Information System")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

MAX_STUDENTS = int(os.getenv("MAX_STUDENTS", "100"))

API_KEY = os.getenv("API_KEY")
DATA_FILE = BASE_DIR / "data" / "student.json"