import os
import sys
import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode('utf-8', errors='ignore'))
    print(stderr.decode('utf-8', errors='ignore'))

def force_clean():
    print("Forzando la eliminación de todos los archivos de caché...")
    
    # Eliminar todos los directorios __pycache__ y archivos .pyc
    run_command("powershell -Command \"Get-ChildItem . -Include __pycache__ -Recurse -Force | Remove-Item -Recurse -Force\"")
    run_command("powershell -Command \"Get-ChildItem . -Include *.pyc -Recurse -Force | Remove-Item -Force\"")
    
    print("Limpieza forzada completada.")

def restart_django_server():
    print("Deteniendo cualquier servidor Django en ejecución...")
    run_command("powershell -Command \"Stop-Process -Name python -Force -ErrorAction SilentlyContinue\"")
    
    print("Iniciando el servidor Django con opciones de recarga forzada...")
    django_command = f"start cmd /k {sys.executable} manage.py runserver --noreload --insecure"
    subprocess.Popen(django_command, shell=True)

def clear_migrations():
    print("Eliminando archivos de migración (excepto __init__.py)...")
    run_command("powershell -Command \"Get-ChildItem -Path . -Recurse -Include migrations | Get-ChildItem -Exclude __init__.py | Remove-Item -Force\"")

if __name__ == '__main__':
    force_clean()
    
    choice = input("¿Deseas eliminar también los archivos de migración? (s/n): ").lower()
    if choice == 's':
        clear_migrations()
    
    restart_django_server()
    print("El servidor Django ha sido reiniciado con una limpieza forzada.")
    print("Por favor, verifica si tus cambios ahora se reflejan correctamente.")