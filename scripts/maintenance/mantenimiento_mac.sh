#!/bin/bash

# Comenzar caffeinate para evitar que el sistema entre en suspensión
caffeinate &
caffeinate_pid=$!

# Comprobar si se debe abrir en Terminal
if [ "$OPEN_IN_TERMINAL" == "1" ]; then
    echo "Abriendo en Terminal..."
    osascript -e 'tell application "Terminal" to do script "/Users/saicobys/Developer/Scripts/Maintenance/mantenimiento_mac.sh"'
fi


# Mostrar una notificación al iniciar
osascript -e 'display notification "Iniciando mantenimiento" with title "Mantenimiento en progreso"'


# Actualización del sistema y aplicaciones
echo "Actualizando el sistema y aplicaciones..."
softwareupdate --install --all
brew update && brew upgrade


# Limpieza de caché y archivos temporales
echo "Limpiando caché y archivos temporales..."
brew cleanup
rm -rf ~/Library/Caches/*


# Verificación de volúmenes
echo "Verificando la integridad del volumen principal (Macintosh HD)..."
diskutil verifyVolume disk3s1


# Verificación del disco completo
echo "Verificando la integridad del disco completo (disk0)..."
diskutil verifyDisk disk0


# Información de la batería (para MacBooks)
echo "Verificando el estado de la batería..."
system_profiler SPPowerDataType | grep -E "Cycle Count:|Condition:"


# Actualización de aplicaciones instaladas con Homebrew Cask
echo "Actualizando aplicaciones instaladas con Homebrew Cask..."
brew upgrade --cask


# Reconstrucción de la caché de Launch Services
echo "Reconstruyendo la caché de Launch Services..."
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -kill -r -domain local -domain system -domain user


# Liberación de memoria inactiva
echo "Liberando memoria inactiva..."
sudo purge


# Vaciar la Papelera de forma segura
echo "Vaciando la Papelera de forma segura..."
sudo rm -rf ~/.Trash/*


# Vaciar la caché de DNS
echo "Vaciando la caché de DNS..."
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder


# Mostrar una notificación cuando termine el script
osascript -e 'display notification "El script de mantenimiento se ha ejecutado correctamente" with title "Mantenimiento Completado"'


# Terminar el proceso caffeinate para permitir que el sistema gestione su energía normalmente
kill $caffeinate_pid

echo "¡Mantenimiento completado!"