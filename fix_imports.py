#!/usr/bin/env python3
"""
Script para corregir imports incorrectos en el proyecto Casino Virtual
Convierte imports absolutos 'from src.' a imports relativos apropiados
"""

import os
import re
import sys

def fix_imports_in_file(file_path):
    """Corrige los imports en un archivo específico"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Patrones de reemplazo para diferentes tipos de archivos
        replacements = [
            # Para archivos en servidor/src/model/usuario/
            (r'from src\.model\.usuario\.UsuarioServicio import UsuarioServicio', 
             'from .UsuarioServicio import UsuarioServicio'),
            
            # Para archivos en servidor/src/model/salaDeJuego/
            (r'from src\.model\.salaDeJuego\.SalaDeJuego import SalaDeJuego',
             'from .SalaDeJuego import SalaDeJuego'),
            (r'from src\.model\.usuario import Usuario',
             'from ..usuario import Usuario'),
            (r'from src\.utils\.firestore import (.+)',
             r'from ...utils.firestore import \1'),
             
            # Para archivos en servidor/src/model/salaDeJuego/juego/
            (r'from src\.model\.salaDeJuego\.juego\.juegosDeCartas\.JuegoDeCartas import JuegoDeCartas',
             'from .JuegoDeCartas import JuegoDeCartas'),
            (r'from src\.model\.usuario\.Usuario import Usuario',
             'from ....usuario.Usuario import Usuario'),
             
            # Para archivos en servidor/src/view/
            (r'from src\.view\.(.+) import (.+)',
             r'from .\1 import \2'),
            (r'from src\.view\.utils\.(.+) import (.+)',
             r'from .utils.\1 import \2'),
             
            # Para archivos de test
            (r'from src\.model\.(.+) import (.+)',
             r'from servidor.src.model.\1 import \2'),
        ]
        
        # Aplicar todas las correcciones
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
        
        # Si hubo cambios, escribir el archivo
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Corregido: {os.path.relpath(file_path)}")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error procesando {file_path}: {e}")
        return False

def main():
    """Función principal"""
    print("🔧 Corrigiendo imports en el proyecto Casino Virtual...")
    
    base_dir = r"c:\Users\SGA\Programacion\tecnicas_de_programacion\404_Luck_Not_Found"
    files_fixed = 0
    
    # Buscar todos los archivos .py en el proyecto
    for root, dirs, files in os.walk(base_dir):
        # Evitar directorios de cache y venv
        dirs[:] = [d for d in dirs if d not in ['__pycache__', 'casino_env', '.git']]
        
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                if fix_imports_in_file(file_path):
                    files_fixed += 1
    
    print(f"\n🎉 Corrección completada. Archivos modificados: {files_fixed}")

if __name__ == "__main__":
    main()
