# Ejemplo 2 de Git School: fast-forward

## Notación:
  
  - `#$` representa salidas de consola
  - `#` comentarios
  - Y el resto de líneas son comandos

Probar en: [Git School](https://git-school.github.io/visualizing-git/)

---

```bash
  #$ Have fun!
  git commit -m "index.html"
  git commit -m "about.html"
  git commit -m "contact.html"
  git checkout -b bugfix
  git checkout bugfix
  git branch
  #$    master
  #$  * bugfix
  git commit -m "fix 1"
  git commit -m "fix 2"
  git commit -m "fix 3 (solved)"
  git checkout master
  git merge bugfix
  #$ You have performed a fast-forward merge.
```