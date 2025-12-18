"""
Script para executar a aplicação Streamlit
"""
import subprocess
import sys
import os

# Define o caminho do arquivo principal
app_path = os.path.join("srcpoo", "Agenda", "index.py")

# Executa o Streamlit
if __name__ == "__main__":
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", app_path])
    except KeyboardInterrupt:
        print("\nAplicação encerrada pelo usuário.")
    except Exception as e:
        print(f"Erro ao executar a aplicação: {e}")

