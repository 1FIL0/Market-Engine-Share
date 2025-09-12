from pathlib import Path
from dotenv import load_dotenv

def loadEnv(envPath: Path):
    try:
        _ = load_dotenv(dotenv_path=envPath)
        print(f".env loaded from {envPath}")
    except Exception as e:
        print(f"Failed to load .env file at {envPath}: {e}")