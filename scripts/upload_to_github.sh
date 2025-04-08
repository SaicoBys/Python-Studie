#!/bin/bash

# ✅ Mensaje del commit como argumento o por defecto
COMMIT_MSG=${1:-"Auto commit - $(date +'%Y-%m-%d %H:%M')"}

# ✅ Verificar si estamos dentro de un repositorio Git
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  echo "❌ Error: Not inside a Git repository."
  exit 1
fi

# ✅ Navegar al directorio del repo (ajusta si es necesario)
# cd /Users/saicobys/Developer/Python || exit

# ✅ Mostrar rama actual
branch=$(git rev-parse --abbrev-ref HEAD)
echo "📦 Subiendo cambios a la rama: $branch"

# ✅ Añadir cambios
git add .

# ✅ Hacer commit
git commit -m "$COMMIT_MSG"

# ✅ Subir al repositorio
git push origin "$branch"

echo "✅ Cambios subidos correctamente con mensaje: $COMMIT_MSG"