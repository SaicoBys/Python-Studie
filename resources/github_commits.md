# 📝 Guía de Plantilla para Mensajes de Commit en Git

Utilizo esta plantilla para escribir mensajes de commit claros y significativos en mis proyectos.

---

## ⚙️ Estructura Básica del Mensaje de Commit

```bash
<tipo>(<scope>): <descripción breve y significativa>
```

**Ejemplo:**

```bash
feat(settings): add dark mode toggle
```

---

## 🗂️ Tipos Comunes de Commits y Ejemplos

| Tipo      | Descripción                                                       | Ejemplo                                       |
|-----------|-------------------------------------------------------------------|-----------------------------------------------|
| `feat`    | Nueva funcionalidad                                               | `feat(login): add OAuth2 support`              |
| `fix`     | Corrección de un bug                                              | `fix(loop): correct off-by-one error`          |
| `docs`    | Cambios en documentación                                          | `docs(readme): update installation guide`     |
| `style`   | Formato o estilo sin afectar lógica                              | `style(code): format according to PEP8`       |
| `refactor`| Refactorización sin cambiar comportamiento                       | `refactor(auth): simplify token validation`   |
| `test`    | Añadir o corregir pruebas                                         | `test(utils): add tests for string parser`    |
| `chore`   | Tareas de mantenimiento o sin impacto en código de producción   | `chore(deps): update dependencies`             |
| `ci`      | Cambios en integración continua                                  | `ci(workflow): add lint check`                  |
| `build`   | Cambios en dependencias o configuración de entorno               | `build(docker): update base image`              |
| `perf`    | Mejoras de rendimiento                                           | `perf(api): optimize query execution`           |
| `revert`  | Reversión de un commit anterior                                  | `revert: revert "feat(login): add OAuth2 support"` |
| `content` | Añadir contenido nuevo (ejercicios, texto)                       | `content(exercises): add solution for challenge 024` |
| `log`     | Cambios en mensajes de consola o debug                           | `log(debug): add verbose output`                 |
| `temp`    | Cambios temporales con intención de eliminar después            | `temp: disable feature X temporarily`            |
| `structure`| Reorganización de archivos o carpetas                           | `structure: move utils to helpers folder`        |

---

## 🧩 Plantillas y Ejemplos Detallados por Tipo

### `feat:` Nueva Funcionalidad

```bash
feat(<scope>): add [feature] to [section]
# Ejemplo:
feat(settings): add dark mode toggle
```

---

### `fix:` Corrección de Errores

```bash
fix(<scope>): fix [bug or issue] in [module or component]
# Ejemplo:
fix(loop): correct off-by-one error
```

---

### `docs:` Cambios en Documentación

```bash
docs(<scope>): update [topic or file] with more details/examples
# Ejemplo:
docs(readme): add installation instructions
```

---

### `style:` Formato o Estilo

```bash
style(<scope>): format [file or section] for readability
# Ejemplo:
style(code): format according to PEP8
```

---

### `refactor:` Mejora de Código sin Cambiar Función

```bash
refactor(<scope>): simplify [function or logic block]
# Ejemplo:
refactor(auth): simplify token validation logic
```

---

### `test:` Tests Nuevos o Ajustados

```bash
test(<scope>): add tests for [function or module]
# Ejemplo:
test(utils): add tests for string parser
```

---

### `chore:` Mantenimiento y Otras Tareas

```bash
chore(<scope>): rename [folder or file] to match new structure
# Ejemplo:
chore(project): update dependencies
```

---

## ✅ Ejemplos Reales de Mensajes de Commit

```bash
feat(user): add input validation to registration form
fix(email): correct typo in validation regex
docs(readme): add sorting algorithm explanation
style(code): format according to PEP8
refactor(cart): simplify loop logic in shipping calculation
test(thread): add unit tests for color counter
chore(deps): update pip dependencies
```

---

## 🧪 Flujo de Trabajo Personal con Git

1. Escribo o actualizo archivos.
2. Guardo cambios en el editor (VS Code).
3. Ejecuto desde cualquier parte del proyecto:

```bash
gitup "feat(exercises): add solution for challenge 024 string_length"
```

4. Esto ejecuta el script `scripts/upload_to_github.sh` con el mensaje de commit proporcionado.

---

## ✅ Comandos Útiles de Git

```bash
git add <archivo>
git commit -m "feat(scope): descripción"
git push
```

O usando mi alias personalizado:

```bash
gitup "feat(exercises): add solution for challenge 025 iterate_string"
```
