import os
from functools import lru_cache
from pathlib import Path
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def _int(name, default):
    try: return int(os.getenv(name, default))
    except (TypeError, ValueError): return default

@lru_cache
def settings():
    return {
        "app_name": os.getenv("APP_NAME","Trapsoul Researcher"),
        "env": os.getenv("ENV","development"),
        "host": os.getenv("HOST","127.0.0.1"),
        "port": _int("PORT",8000),
        "youtube_api_key": os.getenv("YOUTUBE_API_KEY"),
        "spotify_client_id": os.getenv("SPOTIFY_CLIENT_ID"),
        "spotify_client_secret": os.getenv("SPOTIFY_CLIENT_SECRET"),
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "openai_model": os.getenv("OPENAI_MODEL","gpt-5.6-mini"),
        "request_timeout": float(os.getenv("REQUEST_TIMEOUT_SECONDS","15")),
        "max_results": _int("MAX_RESULTS",25)
    }
