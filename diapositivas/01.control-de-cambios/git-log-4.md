# Historial de comandos
## Tres modos de merge

**Notación:**
 -  `➜` precede un comando de terminal

---

## squash

# Crear y entrar en el directorio squash
➜  0.IFCD65 mkdir <repo>
➜  0.IFCD65 cd <repo>

# Inicializar un repositorio Git
➜  git init

Inicializado repositorio Git vacío en <ruta hasta.../.../repo/.git/>

# Crear archivo index.html y hacer el primer commit
➜  touch index.html      # crear archivo desde VS Code en Windows
➜  git add index.html
➜  git commit -m "Primer commit en main"

[main (commit-raíz) b1b6e69] Primer commit en main
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 index.html

# Crear y cambiar a la rama feature
➜   git checkout -b feature

Cambiado a nueva rama 'feature'

# Crear archivo about.html y hacer commit
➜   touch about.html   # crear archivo desde VS Code en Windows
➜   git add .
➜   git commit -m "Añadir about.html"

[feature 642a796] Añadir about.html
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 about.html

# Cambiar a la rama main y crear archivo contact.html
➜   git checkout main
Cambiado a rama 'main'
➜   touch contact.html
➜  git add .
➜  git commit -m "Añadir contact.html"

[main 5c8809a] Añadir contact.html
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 contact.html

# Hacer un merge squash de la rama feature en main
➜   git merge feature --squash

Commit de aplastamiento -- no actualizando HEAD
Fusión automática fue bien; detenida antes del commit como se solicitó

# Confirmar el commit de squash
➜  git commit -m "Commit de Squash"

[main 4871f47] Commit de Squash
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 about.html

## no-ff

# Crear y cambiar a la rama feature2
➜  git checkout -b feature2

Cambiado a nueva rama 'feature2'

# Crear un archivo test.html y hacer commit
➜  touch test.html
➜  git add .
➜  git commit -m "Commit en feature 2"

[feature2 06259e3] Commit en feature 2
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test.html

# Cambiar a la rama main y hacer merge de feature2 sin fast-forward
➜  git checkout main
Cambiado a rama 'main'
➜  git merge feature2 --no-ff

Merge made by the 'ort' strategy.
 test.html | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test.html

## ff-only

# Crear y cambiar a la rama feature3
➜  git checkout -b feature3
Cambiado a nueva rama 'feature3'

# Crear archivos a.html y b.html, y hacer commits
➜  touch a.html
➜  touch b.html
➜  git add a.html
➜  git commit -m "Añadir a.html"

[feature3 e611a32] Añadir a.html
 1 file changed, 0 insertions(+), 0 deletions(-)

 create mode 100644 a.html

➜  git add b.html
➜  git commit -m "Añadir b.html"

[feature3 8a97578] Añadir b.html
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 b.html

# Cambiar a la rama main y hacer merge de feature3 con fast-forward
➜  git checkout main

Cambiado a rama 'main'

➜  git merge feature3 --ff-only

Actualizando 0324438..8a97578
Fast-forward
 a.html | 0
 b.html | 0
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.html
 create mode 100644 b.html

# Verificar el estado del repositorio
➜  git status
En la rama main
nada para hacer commit, el árbol de trabajo está limpio