import sys
import subprocess
import pathlib

print("--- CLEANING-UP the temporary py files ---")
path = pathlib.Path()/'_make_npm_script.py'
path.unlink()
subprocess.Popen(
    "python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format(sys.argv[0]), shell=True)
sys.exit(0)