# Historial de comandos
## Tres modos de merge

**Notación:**
 -  `➜` precede un comando de terminal

---

```bash
➜  git add .     
➜  git status
En la rama main

No hay commits todavía

Cambios a ser confirmados:
  (usa "git rm --cached <archivo>..." para sacar del área de stage)
        nuevos archivos: index.html

➜  git commit -m "crear index.html"      
[main (commit-raíz) f98ed19] crear index.html
 1 file changed, 12 insertions(+)
 create mode 100644 index.html
➜  git log                         
➜  git log --name-only
➜  git checkout -b conflicto                
Cambiado a nueva rama 'conflicto'
➜  conflictos git:(conflicto) git branch               
➜  conflictos git:(conflicto) git log            
➜  conflictos git:(conflicto) git add .
➜  conflictos git:(conflicto) git status
En la rama conflicto
Cambios a ser confirmados:
  (usa "git restore --staged <archivo>..." para sacar del área de stage)
        modificados:     index.html

➜  conflictos git:(conflicto) git add index.html 
➜  conflictos git:(conflicto) git commit -m "crear conflicto de ejemplo"
[conflicto 3bdba2c] crear conflicto de ejemplo
 1 file changed, 1 insertion(+), 1 deletion(-)
➜  conflictos git:(conflicto) git checkout main                         
Cambiado a rama 'main'
➜  git add .         
➜  git commit -m "modificación"              
[main e043bb2] modificación
 1 file changed, 1 insertion(+), 1 deletion(-)
➜  git log                     
➜  git branch
➜  git merge conflicto         
Auto-fusionando index.html
CONFLICTO (contenido): Conflicto de fusión en index.html
Fusión automática falló; arregle los conflictos y luego realice un commit con el resultado.
```