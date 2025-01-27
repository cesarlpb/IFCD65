# Ejemplo 3 de Git School: commit de merge

## Notación:
  
  - `#$` representa salidas de consola
  - `#` comentarios
  - Y el resto de líneas son comandos

Probar en: [Git School](https://git-school.github.io/visualizing-git/)

---

```bash
#$ Have fun!
git commit -m "1"
git commit -m "2"
git commit -m "3"
git checkout -b rama
git branch
#$   master
#$ * rama
git commit -m " rama 1"
git commit -m " rama 2"
git checkout master
git commit -m "4"
git commit -m "5"
git merge rama
```