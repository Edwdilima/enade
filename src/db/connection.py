import os
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do banco de dados PostgreSQL
DB_HOST = os.getenv('LOCAL_DB_HOST')
DB_NAME = os.getenv('LOCAL_DB_NAME')
DB_USER = os.getenv('LOCAL_DB_USER')
DB_PASS = os.getenv('LOCAL_DB_PASSWORD')

# Função para conectar ao banco de dados
def connect():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn
