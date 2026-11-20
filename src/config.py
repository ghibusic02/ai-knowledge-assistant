import os
from dotenv import load_dotenv

# Load enviroment from .env file
load_dotenv()

# Model Settings
LLM_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"
TEMPERATURE = 0.0

#Chuncking settings
CHUNK_SIZE=1000
CHUNK_OVERLAP=200

#PAths
DATA_DIR="data"
CHROMA_DB_DIR="chroma_db"
