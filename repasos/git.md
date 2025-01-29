<!-- Grabación del día 29.01 entre las 11:15 - 11:45 -->
# **📌 Guión: Introducción a Git (30 min)**  

## **1️⃣ ¿Qué es Git? (5 min)**
📌 **Objetivo:** Explicar qué es Git y por qué es importante.  

✅ **Puntos clave:**  
- Git es un **sistema de control de versiones distribuido**.  
- Permite hacer **seguimiento de cambios** en el código y volver a versiones anteriores.  
- Facilita la **colaboración** en proyectos de software.  
- **Git ≠ GitHub**: Git es la herramienta, GitHub es una plataforma donde se almacenan repositorios Git.  

📌 **Ejemplo real:**  
- Guardar múltiples versiones de un documento como `archivo_v1.docx`, `archivo_v2.docx`, etc.  
- Git hace esto de forma automática y organizada.  

---

## **2️⃣ Configuración básica de Git (5 min)**
📌 **Objetivo:** Configurar Git en la máquina del usuario.  

✅ **Configurar nombre y correo:**  
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```
✅ **Ver configuración actual:**  
```bash
git config --list
```
💡 **Consejo:** Explicar la diferencia entre configuración local (`--local`) y global (`--global`).  

---

## **3️⃣ Creando y gestionando un repositorio Git (10 min)**
📌 **Objetivo:** Explicar el flujo básico de Git.  

✅ **Crear un nuevo repositorio:**  
```bash
mkdir mi_proyecto
cd mi_proyecto
git init
```
✅ **Ver estado del repositorio:**  
```bash
git status
```
✅ **Añadir archivos a Git:**  
```bash
echo "Hola Mundo" > index.txt # puedes abrirlo con Vs Code y escribir algo
git add index.txt
git commit -m "Añadir index.txt"
```
✅ **Explicación:**  
- `git init`  : Inicia un repositorio vacío.  
- `git add`   : Prepara archivos para el commit.  
- `git commit`: Guarda los cambios con un mensaje.  

---
## Estados de Git y Staging

```bash
  Sin seguimiento -> staging (en preparación) -> Confirmado (commit en historial)
```
---

## **4️⃣ Uso de Branches (5 min)**
📌 **Objetivo:** Explicar qué son las ramas en Git.  

✅ **Comandos esenciales:**  
```bash
git branch nombre-rama   # Crear una nueva rama
git checkout nombre-rama # Cambiar a la nueva rama
git merge nombre-rama    # Fusionar la rama con la principal
git branch -d nombre-rama # Eliminar una rama
```
💡 **Consejo:** Explicar cómo las ramas permiten trabajar en paralelo sin afectar la versión principal del código.  

---

## Tipos de merge (fusión de ramas):

- **Fast-forward:** adelanta el historial al último commit
- **No Fast-forward:** crear un commit nuevo para fusionar y coloca "Merge de branch..."
- **Squash:** permite juntar todos los cambios en un commit que puedes editar

---

## **5️⃣ Eliminación de archivos y `.gitignore` (5 min)**
📌 **Objetivo:** Explicar cómo eliminar archivos y evitar que Git rastree archivos innecesarios.  

✅ **Eliminar archivos del control de versiones:**  
```bash
git rm --cached archivo.txt
git commit -m "Eliminar archivo innecesario"
```
✅ **Ejemplo de `.gitignore`:**  
```bash
# Ignorar archivos temporales
*.log
node_modules/
__pycache__/
.env
```

---

## **6️⃣ Cierre y Preguntas (5 min)**
📌 **Objetivo:** Resolver dudas y reforzar los conceptos clave.  

✅ **Resumen rápido:**  
- `git init`    → Crear repo  
- `git status`  → Ver estado  
- `git add`     → Preparar cambios: `git add .` añade todo
- `git commit -m "Mensaje"` → Guardar cambios  
- `git log`     → Ver el historial de commits, `git log --name-only` (muestra archivos)
- `git branch`  → Ver las ramas, `git branch <rama>` crea rama nueva 
  - `git checkout <rama>` → cambiar de rama
- `.gitignore`  → Ignorar archivos innecesarios  

**💬 Preguntas:**  
- ¿Dudas sobre la configuración o comandos básicos?  
- ¿Quieres hacer una práctica en vivo?  

---

### **🚀 Fin de la sesión de Git. Ahora pasamos a GitHub.**  
