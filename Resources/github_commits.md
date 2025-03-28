# 📝 Commit Message Template Guide

I use this template to write clear, meaningful Git commit messages for your projects.

---

## ✍️ Estructura recomendada

```
<tipo>: <descripción breve y significativa>
```

### Tipos comunes

- `feat:` Una nueva funcionalidad.
- `fix:` Corrección de un bug.
- `docs:` Cambios en la documentación.
- `style:` Formato (espacios, comas, etc.) sin cambios en la lógica del código.
- `refactor:` Refactorización de código sin cambiar su comportamiento.
- `test:` Añadir o corregir pruebas.
- `chore:` Tareas que no modifican el código de producción (actualizar dependencias, etc.)

---

## 🧾 Ejemplos

```bash
feat: add input validation to registration form
fix: correct typo in email validation regex
docs: add explanation for sorting algorithm in README
style: format code according to PEP8
refactor: simplify loop logic in shipping calculation
test: add unit tests for new thread color counter
chore: update pip dependencies
```

---

## ✅ Recomendaciones

- Usa verbos en infinitivo (“add”, “fix”, “update”).
- Que el mensaje no supere los 72 caracteres en su línea principal.
- Si necesitas detalles adicionales, usa una segunda línea en blanco y escribe un párrafo más extenso.

---

> 🧠 Consejo: Mantener una convención clara para los commits ayuda a colaborar mejor y entender la evolución del proyecto.

---

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
