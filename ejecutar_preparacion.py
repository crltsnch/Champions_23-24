import subprocess

if __name__ == "__main__":
    # Nombre del script que deseas ejecutar
    script_name = "preparacion.py"

    # Comando para ejecutar el script
    command = f"python {script_name}"

    # Ejecutar el script
    subprocess.run(command, shell=True)