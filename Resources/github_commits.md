# 📝 Commit Message Template Guide

I use this template to write clear, meaningful Git commit messages for my projects.

## ✍️ Estructura básica del mensaje de commit

```
<tipo>: <descripción breve y significativa>
```

## 🗂️ Tipos de commits comunes y útiles

- `feat:` Una nueva funcionalidad.
- `fix:` Corrección de un bug.
- `docs:` Cambios en la documentación.
- `style:` Formato (espacios, comas, etc.) sin cambios en la lógica del código.
- `refactor:` Refactorización de código sin cambiar su comportamiento.
- `test:` Añadir o corregir pruebas.
- `chore:` Tareas que no modifican el código de producción (actualizar dependencias, etc.)
- `ci:` Cambios relacionados con integración continua (GitHub Actions, workflows).
- `build:` Cambios en dependencias, compilación o configuración de entorno.
- `perf:` Mejoras de rendimiento sin alterar el comportamiento.
- `revert:` Reversión de un commit anterior.
- `content:` Añadir contenido nuevo como soluciones de ejercicios o texto.
- `log:` Cambios en mensajes de consola o depuración (prints, logging).
- `temp:` Cambios temporales con intención de eliminar más adelante.
- `structure:` Reorganización de archivos, carpetas o convenciones.

## 🧩 Plantillas específicas para cada tipo de commit

### `feat:` Nueva funcionalidad
```bash
feat: add [feature] to [section]
# Ejemplo:
feat: add dark mode toggle to settings menu
```

### `fix:` Corrección de errores
```bash
fix: fix [bug or issue] in [module or component]
# Ejemplo:
fix: fix off-by-one error in loop iteration
```

### `docs:` Cambios en documentación
```bash
docs: update [topic or file] with more details/examples
# Ejemplo:
docs: update Variables.py with clearer type examples
```

### `style:` Formato o estilo
```bash
style: format [file or section] for readability
# Ejemplo:
style: format DataTypes.py according to PEP8
```

### `refactor:` Mejora de código sin cambiar su función
```bash
refactor: simplify [function or logic block] in [file]
# Ejemplo:
refactor: simplify validation logic in Errors.py
```

### `test:` Tests nuevos o ajustados
```bash
test: add tests for [function or module]
# Ejemplo:
test: add tests for is_even() in Operators.py
```

### `chore:` Mantenimiento u otras tareas
```bash
chore: rename [folder or file] to match new structure
# Ejemplo:
chore: rename VariablesAndDataTypes to 01_Variables_And_DataTypes
```

## ✅ Ejemplos reales de mensajes

```bash
feat: add input validation to registration form
fix: correct typo in email validation regex
docs: add explanation for sorting algorithm in README
style: format code according to PEP8
refactor: simplify loop logic in shipping calculation
test: add unit tests for new thread color counter
chore: update pip dependencies
```

## 🧪 Flujo de trabajo personal con Git

1. Escribo soluciones o actualizo los archivos.
2. Guardo cambios en VS Code.
3. Luego corro este comando desde cualquier parte del proyecto:

```bash
gitup "Added solution for challenge 024: string_length"
```

4. Esto ejecuta el script `scripts/upload_to_github.sh` con el mensaje de commit proporcionado.

## ✅ Comandos útiles de Git

```bash
git add nombre_del_archivo.py
git commit -m "feat: add solución para challenge 025"
git push
```

O usando mi alias personalizado:

```bash
gitup "Added solution for challenge 025: iterate_string"
```
