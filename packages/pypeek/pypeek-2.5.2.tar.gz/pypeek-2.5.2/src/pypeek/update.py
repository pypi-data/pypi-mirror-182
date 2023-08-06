import subprocess, sys, os

def update():
    python = sys.executable
    subprocess.run([python, "-m", "pip", "install", "--upgrade", "pypeek"])
    os.execl(python, python, "-m", "pypeek")  