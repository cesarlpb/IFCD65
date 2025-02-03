import os
import sys
from bs4 import BeautifulSoup

def is_valid_html(file_path):
    """Verifica si un archivo HTML contiene las etiquetas básicas necesarias."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Analizar con BeautifulSoup
        soup = BeautifulSoup(content, "html.parser")

        # Verificar etiquetas obligatorias
        has_doctype = content.lower().startswith("<!doctype html")
        has_html = soup.html is not None
        has_head = soup.head is not None
        has_body = soup.body is not None

        return has_doctype and has_html and has_head and has_body

    except Exception as e:
        print(f"❌ Error al leer {file_path}: {e}")
        return False

def validate_html_files(directory):
    """Verifica todos los archivos HTML en un directorio."""
    if not os.path.exists(directory):
        print(f"❌ La ruta {directory} no existe.")
        return

    html_files = [f for f in os.listdir(directory) if f.endswith(".html")]
    
    print("Archivos encontrados en carpeta:")
    for f in html_files:
      print("- " + f)
    
    if not html_files:
        print("⚠️ No se encontraron archivos HTML en la ruta proporcionada.")
        return

    for file in html_files:
        file_path = os.path.join(directory, file)
        if is_valid_html(file_path):
            print(f"✅ {file} es un HTML válido: <!DOCTYPE>, <html>, <head>, <body>")
        else:
            print(f"❌ {file} no es un HTML válido.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python test_html_are_valid.py <ruta_del_directorio>")
    else:
        validate_html_files(sys.argv[1])
