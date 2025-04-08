#!/bin/bash

# Verifica si ciertos comandos están instalados
command -v htop >/dev/null 2>&1 || { echo "htop no está instalado. Instálalo con: sudo apt install htop (Linux) o brew install htop (Mac)"; exit 1; }
command -v cmatrix >/dev/null 2>&1 || echo "cmatrix no está instalado. Instálalo con: sudo apt install cmatrix (Linux) o brew install cmatrix (Mac)"

# Abre múltiples ventanas de terminal ejecutando distintos comandos
osascript -e 'tell application "Terminal" to do script "htop"' &
osascript -e 'tell application "Terminal" to do script "ping -c 100 google.com"' &
osascript -e 'tell application "Terminal" to do script "tail -f /var/log/system.log"' &
osascript -e 'tell application "Terminal" to do script "openssl rand -hex 1000 | pv -qL 50"' &

# Espera 2 segundos para que las ventanas se abran
sleep 2

# Ejecuta cmatrix en la terminal principal si está instalado
if command -v cmatrix >/dev/null 2>&1; then
    cmatrix
else
    while true; do
        echo "$(openssl rand -hex 10)" | pv -qL 10
        sleep 0.1
    done
fi