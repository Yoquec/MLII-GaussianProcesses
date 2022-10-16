# Assignment 3 MLII
Repo para hostear el trabajo de Machine. <span style="color:gray">(😓 Perdón por lo del dropbox)</span>

## Git cheatsheet

<p class="callout info">Los nombres en todo mayúscula se refieren a algo que tienes que cambiar.</p>

- Clonar este repo en una carpeta (sólo se tiene que hacer una vez).
```bash
git clone https://github.com/Yoquec/MLII-GaussianProcesses
```

- Descargar los cambios de otra gente (debería hacerse siempre que se empiece a trabajar).
```bash
git pull
```

- Mirar qué cambios se han hecho dentro de este conjunto de cambios
```bash
git status
```

- Añandir un archivo al nuevo conjunto de cambios
```bash
git add FILENAME
```

- Añandir todos los archivos cambiados al nuevo conjunto de cambios
```bash
git add .
```


- Registrar los cambios hechos (después de haber seleccionado todos los archivos cambiados con `git add`)
```bash
git commit -m "MENSAJE DE COMMIT"
```

- Subir los cambios a Github
```bash
git push

#También podemos especificar una rama
git push -u origin RAMA
```


- Quitar un archivo añadido al conjunto de cambios (cuando lo añades sin quere)
```bash
git restore --staged FILENAME 
```
