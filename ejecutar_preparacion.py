from nbconvert import PythonExporter
import subprocess

def convert_ipynb_to_py(ipynb_file):
    exporter = PythonExporter()
    with open(ipynb_file, 'r') as f:
        notebook_content = f.read()
    python_script, _ = exporter.from_notebook_node(notebook_content)
    return python_script

def execute_python_script(python_script):
    exec(python_script)

if __name__ == "__main__":
    ipynb_file = "preparacion.ipynb"
    python_script = convert_ipynb_to_py(ipynb_file)
    execute_python_script(python_script)
