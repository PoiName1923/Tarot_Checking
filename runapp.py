import os
import subprocess
import sys


subprocess.Popen([sys.executable, "-m", "streamlit", "run", "app.py"])
from pyngrok import ngrok

public_url = ngrok.connect(8501)
print("Public URL:", public_url)