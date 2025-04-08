#!/bin/bash

# ================================
# 🚀 GIT AUTO PUSH SCRIPT
# ================================

# ✅ Colores
GREEN="\033[0;32m"
RED="\033[0;31m"
YELLOW="\033[1;33m"
BLUE="\033[1;34m"
NC="\033[0m" # No Color

# ✅ Verificar si estamos dentro de un repositorio Git
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  echo -e "${RED}❌ Error: Not inside a Git repository.${NC}"
  exit 1
fi

# ✅ Mensaje del commit como argumento o por defecto
COMMIT_MSG=${1:-"Auto commit - $(date +'%Y-%m-%d %H:%M')"}
BRANCH=$(git branch --show-current)

echo -e "${BLUE}📦 Subiendo cambios a la rama: ${YELLOW}${BRANCH}${NC}"
echo -e "${BLUE}------------------------------------------${NC}"

# ✅ Mostrar archivos modificados antes del commit
CHANGES=$(git status --short)
NUM_CHANGES=$(echo "$CHANGES" | wc -l | tr -d ' ')

if [ "$NUM_CHANGES" -eq 0 ]; then
  echo -e "${YELLOW}⚠️  No hay archivos para commitear.${NC}"
else
  echo -e "${BLUE}📄 Archivos listos para commit: ${YELLOW}$NUM_CHANGES${NC}"
  echo -e "${BLUE}------------------------------------------${NC}"
  echo -e "$CHANGES"
  echo -e "${BLUE}------------------------------------------${NC}"
fi

# ✅ Agregar cambios
git add .

# ✅ Hacer commit
git commit -m "$COMMIT_MSG"

# ✅ Push con detección automática de rama
git push -u origin "$BRANCH"

# ✅ Mensaje final
echo -e "${GREEN}✅ Cambios subidos correctamente con mensaje:${NC} ${YELLOW}$COMMIT_MSG${NC}"
echo -e "${GREEN}✨ ¡Todo listo!${NC}"
echo -e "${BLUE}------------------------------------------${NC}"