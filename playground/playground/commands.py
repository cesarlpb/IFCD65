import os
import json
import click
from bs4 import BeautifulSoup

CONTEXT_FILE = "context.json"  # Archivo que contiene el ejercicio actual

@click.command()
def test():
    """Realiza el test de ejemplo del ejercicio actual (pg_dd...html) especificado en el contexto"""
    try:
        # Cargar el contexto actual
        if not os.path.exists(CONTEXT_FILE):
            click.echo("❌ No se encontró el archivo de contexto. Ejecuta primero 'start'.")
            return

        with open(CONTEXT_FILE, "r") as f:
            context = json.load(f)

        topic = context.get("topic")
        level = context.get("level", "basico")  # Nivel por defecto si no está en el contexto
        exercise = context.get("exercise")

        if not (topic and exercise):
            click.echo("❌ El archivo de contexto no tiene suficiente información.")
            return

        # Construir la ruta del archivo a revisar
        exercise_number = exercise.split(".")[0]  # Obtener la numeración del ejercicio
        # solution_path = os.path.join("html", level, f"pg_{exercise_number}.html")
        solution_path = os.path.abspath(os.path.join("playground", "html", level, f"pg_{exercise_number}.html"))

        if not os.path.exists(solution_path):
            click.echo(f"❌ No se encontró el archivo de solución en: {solution_path}")
            return

        click.echo(f"✅ Archivo encontrado: {solution_path}")

        # Leer el archivo de solución
        with open(solution_path, "r", encoding="utf-8") as f:
            solution_content = f.read()

        # Parsear el HTML
        soup = BeautifulSoup(solution_content, "html.parser")

        # Definir los puntos a revisar (puedes extender esta lógica)
        checks = [
            ("title", lambda s: bool(s.find("title")), "El documento debe tener un <title>."),
            ("h1", lambda s: bool(s.find("h1")), "Debe existir al menos un <h1> en el archivo."),
            ("p", lambda s: bool(s.find("p")), "Debe existir al menos un párrafo (<p>)."),
        ]

        # Validar los puntos
        for tag, check, message in checks:
            if check(soup):
                click.echo(f"✅ {message}")
            else:
                click.echo(f"❌ {message}")

    except Exception as e:
        click.echo(f"❌ Error inesperado: {e}")
