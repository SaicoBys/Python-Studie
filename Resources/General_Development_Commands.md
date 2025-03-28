# ========================================
# Comandos Generales de Desarrollo en Python, Django, Git y Terminal
# ========================================

# 1. Configuración de Entorno Virtual
# ----------------------------------------
# Crear un entorno virtual
python3 -m venv env

# Activar el entorno virtual
source env/bin/activate

# Desactivar el entorno virtual
deactivate

# ========================================
# 2. Comandos de Django
# ========================================

# a. Iniciar Proyecto y Apps
# ----------------------------------------
# Crear un nuevo proyecto de Django
django-admin startproject <nombre_proyecto>

# Crear una nueva app dentro del proyecto
python manage.py startapp <nombre_app>

# b. Migraciones y Bases de Datos
# ----------------------------------------
# Crear migraciones para la base de datos
python manage.py makemigrations

# Aplicar migraciones a la base de datos
python manage.py migrate

# c. Ejecutar el Servidor de Desarrollo
# ----------------------------------------
# Iniciar el servidor
python manage.py runserver

# Iniciar el servidor en un puerto específico
python manage.py runserver 8080

# d. Creación de Superusuario (Admin)
# ----------------------------------------
# Crear un superusuario para acceder al panel admin
python manage.py createsuperuser

# ========================================
# 3. Comandos de Git
# ========================================

# a. Comandos Básicos de Git
# ----------------------------------------
# Inicializar un repositorio
git init

# Ver el estado del repositorio
git status

# Agregar cambios al staging
git add .

# Realizar un commit con un mensaje
git commit -m "mensaje del commit"

# Ver el historial de commits
git log

# Subir cambios a un repositorio remoto
git push origin main

# b. Comandos de Ramas en Git
# ----------------------------------------
# Crear una nueva rama
git branch <nombre_rama>

# Cambiar a una rama específica
git checkout <nombre_rama>

# Crear y cambiar a una nueva rama
git checkout -b <nombre_rama>

# Unir una rama a la rama principal
git merge <nombre_rama>

# ========================================
# 4. Comandos Útiles de la Terminal (macOS y Linux)
# ========================================

# a. Navegación Básica
# ----------------------------------------
# Listar archivos y carpetas en el directorio actual
ls

# Cambiar al directorio especificado
cd <nombre_directorio>

# Volver al directorio anterior
cd -

# Crear un nuevo directorio
mkdir <nombre_directorio>

# Crear un archivo vacío
touch <nombre_archivo>

# Mover archivos o directorios
mv <origen> <destino>

# Eliminar un archivo
rm <nombre_archivo>

# Eliminar un directorio y su contenido
rm -r <nombre_directorio>

# Copiar archivos o directorios
cp <origen> <destino>

# b. Otros Comandos Útiles de Terminal
# ----------------------------------------
# Limpiar la terminal
clear

# Ver la ruta completa del directorio actual
pwd

# Buscar un texto en archivos (case-sensitive)
grep "<texto>" <nombre_archivo>

# Buscar texto en todos los archivos del directorio actual (insensible a mayúsculas)
grep -iR "<texto>"

# Ver las primeras 10 líneas de un archivo
head <nombre_archivo>

# Ver las últimas 10 líneas de un archivo
tail <nombre_archivo>

# c. Comandos de Sistema en macOS
# ----------------------------------------
# Ver procesos activos
ps aux

# Forzar el cierre de un proceso específico
kill -9 <PID>

# Comprobar la memoria disponible
vm_stat

# Ver la información de la red
ifconfig

# Apagar el Mac
sudo shutdown -h now

# Reiniciar el Mac
sudo shutdown -r now

# Poner el Mac en modo reposo (sleep)
pmset sleepnow

# ========================================
# 5. Otros Comandos Útiles de Python
# ========================================

# Ejecutar un archivo Python
python <nombre_archivo>.py

# Iniciar el intérprete interactivo de Python
python3

# Instalar paquetes con pip
pip install <nombre_paquete>

# Ver la versión de Python instalada
python --version

# Ver la versión de pip instalada
pip --version

# ========================================
# Notas Finales
# - Reemplaza <nombre_proyecto>, <nombre_app>, <nombre_rama>, y <nombre_archivo> con los nombres específicos que desees.
# - Este archivo se puede actualizar a medida que agregues más herramientas o comandos a tu flujo de trabajo.
# ========================================