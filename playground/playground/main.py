import click
import json
import os
from playground import commands
from datetime import datetime

VERSION = "0.1.0"  # Define la versión de tu aplicación
CONTEXT_FILE = "context.json"  # Archivo para guardar el contexto


# Grupo principal de comandos
@click.group()
@click.version_option(version=VERSION, prog_name="playground")
def cli() -> None:
    """CLI principal de Playground."""
    pass


# Comando "start" para inicializar el contexto
@cli.command()
# @click.option("--list-path", type=click.Path(exists=True), required=True, help="Path al JSON con la lista de ejercicios")
@click.option(
    "--list-path", 
    type=click.Path(exists=True), 
    default="exercise_list.json", 
    show_default=True, 
    help="Path al JSON con la lista de ejercicios"
)
def start(list_path):
    """Inicia un ejercicio especificando el tema y número"""
    try:
        # Cargar el listado de ejercicios
        exercise_data = load_exercise_list(list_path)
        topics = list(exercise_data.keys())

        # Mostrar temas disponibles y pedir selección
        click.echo("Temas disponibles (selecciona por número en [ ]):")
        for idx, topic in enumerate(topics, start=1):
            click.echo(f"[{idx}] - {topic}")

        topic_choice = click.prompt("Selecciona un tema (número)", type=int)
        if topic_choice < 1 or topic_choice > len(topics):
            raise ValueError("Selección de tema inválida.")
        topic = topics[topic_choice - 1]

        # Verificar si el tema tiene niveles
        if isinstance(exercise_data[topic], dict):
            levels = list(exercise_data[topic].keys())
            click.echo(f"Niveles disponibles para {topic}:")
            for idx, level in enumerate(levels, start=1):
                click.echo(f"[{idx:<2}] - {level.capitalize()}")

            level_choice = click.prompt("Selecciona un nivel (número)", type=int)
            if level_choice < 1 or level_choice > len(levels):
                raise ValueError("Selección de nivel inválida.")
            level = levels[level_choice - 1]
            exercises = exercise_data[topic][level]
        else:
            exercises = exercise_data[topic]
        
        # Mostrar ejercicios disponibles y pedir selección
        click.echo(f"Ejercicios disponibles para {topic} ({level if 'level' in locals() else 'General'}):")
        for idx, exercise in enumerate(exercises, start=1):
          # if exercise[:2].isdigit() and exercise[2] == ".":
          #     click.echo(f"{exercise}")
          # else:
              click.echo(f"[{idx:<2}] - {exercise}")

        exercise_choice = click.prompt("Selecciona un número de ejercicio", type=int)
        if exercise_choice < 1 or exercise_choice > len(exercises):
            raise ValueError("Selección de ejercicio inválida.")
        exercise = exercises[exercise_choice - 1]

        # Cargar o inicializar el contexto
        if os.path.exists(CONTEXT_FILE):
            with open(CONTEXT_FILE, "r") as f:
                context = json.load(f)
        else:
            context = {}

        # Obtener autor y email si no están en el archivo de contexto
        author = context.get("author")
        if not author:
            author = click.prompt("Introduce el autor (se puede dejar en blanco)")
        email = context.get("email")
        if not email:
            email = click.prompt("Introduce el email (se puede dejar en blanco)")

        # Añadir fecha actual y guardar contexto
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        context.update({
            "topic": topic,
            "level": level if "level" in locals() else None,
            "exercise": exercise,
            "updated": current_date,
            "author": author,
            "email": email
        })

        with open(CONTEXT_FILE, "w", encoding="utf-8") as f:
            json.dump(context, f, indent=4, ensure_ascii=False)

        click.echo(f"🚀 ¡Contexto guardado!\n----------------------\nTema: {topic}, ejercicio: {exercise}\nAutor: {author}, email: {email}")

    except FileNotFoundError as e:
        click.echo(f"Error: {e}")
    except ValueError as e:
        click.echo(f"Error: {e}")


# Función auxiliar para cargar el listado de ejercicios desde JSON
def load_exercise_list(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"No se encontró el archivo: {path}")
    with open(path, "r") as f:
        return json.load(f)


# Añadir el comando "test" desde commands.py
cli.add_command(commands.test)