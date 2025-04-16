import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar las variables del archivo .env desde la raíz del proyecto
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Verifica que la variable de entorno se carga correctamente
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
print("URL de la base de datos:", SQLALCHEMY_DATABASE_URL)

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("No se pudo cargar la URL de la base de datos desde el archivo .env")

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la sesión local para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar la base para los modelos
Base = declarative_base()
