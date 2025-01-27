# Ejemplo 1 de Git School

## Notación:
  
  - `#$` representa salidas de consola
  - `#` comentarios
  - Y el resto de líneas son comandos

Probar en: [Git School](https://git-school.github.io/visualizing-git/)

---

```bash
  #$ Have fun!
  git commit -m "antes de rama"
  git branch mi-primera-rama
  git switch mi-primera-rama
  #$ I don't understand that. 
  # git switch no está implementado
  git checkout mi-primera-rama
  git branch mi-primera-rama
  #$ Branch "mi-primera-rama" already exists.
  git commit -m "commit en rama"
  git commit -m "commit 2"
  git commit -m "commit 3"
  git commit -m "commit final rama"
  git branch --show-current
  #$  master* mi-primera-rama
  git branch
  #$  master* mi-primera-rama
  git switch master
  #$ I don't understand that.
  git checkout master
  git commit -m "commit en master"
  git commit -m "commit 2 master"
  git commit -m "commit 3 master"
  git checkout mi-primera-rama
  git checkout master
  git merge mi-primera-rama
  git commit -m "después de merge"
  git commit -m "después merge 2"
  git checkout -b new-feature
  git branch
  #$  mi-primera-rama  master* new-feature
  git commit -m "new 1"
  git commit -m "new 2"
  git checkout master
  git commit -m "master 1"
  git commit -m "master 2"
  git commit -m "master 3"
```