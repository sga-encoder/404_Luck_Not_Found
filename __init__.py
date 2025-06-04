"""
Casino Virtual 404 Luck Not Found
Proyecto unificado cliente-servidor
"""
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Importar módulos principales
from . import cliente
from . import servidor
from . import main
from . import main_dev_miguel

__all__ = [
    'cliente',
    'servidor', 
    'main',
    'main_dev_miguel',
    'BASE_DIR'
]
