import os 
import dotenv 

dotenv.load_dotenv()

class Env:
    HOST = os.environ.get("HOST", "0.0.0.0")
    PORT = int(os.environ.get("PORT", 80))
    DEBUG = os.environ.get("DEBUG", "False") == "True"

class DatabaseEnv:
    HOST = os.environ.get("DATABASE_HOST")
    PORT = os.environ.get("DATABASE_PORT")
    USERNAME = os.environ.get("DATABASE_USERNAME")
    PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE = os.environ.get("DATABASE_NAME")
    
class RedisEnv:
    HOST = os.environ.get("REDIS_HOST")
    PORT = int(os.environ.get("REDIS_PORT"))
    RATE_LIMITER_DB = int(os.environ.get("REDIS_RATE_LIMITER_DB"))

class GetWinnerEnv:
    KEY = os.environ.get("GET_WINNER_KEY")