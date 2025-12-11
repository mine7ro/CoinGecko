import subprocess
import logging
from datetime import datetime


#CONFIGURANDO LOGS

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def run_script(script_name):
    """Executa um script Python e captura erros."""
    logging.info(f"Iniciando: {script_name}")

    try:
        result = subprocess.run(
            ["python", script_name],
            check=True,
            capture_output=True,
            text=True,
        )
        logging.info(f"✔ {script_name} executado com sucesso.")

        if result.stdout:
            logging.info(result.stdout)

    except subprocess.CalledProcessError as e:
        logging.error(f"[ERRO] Erro ao executar {script_name}:")
        logging.error(e.stderr)
        raise  # Para parar o run_all se houver erro grave

def main():
    logging.info("===== INICIANDO PIPELINE ETL =====")

    start = datetime.now()

    # 1. Rodar extract.py
    run_script("scripts/extract.py")

    # 2. Rodar transform.py
    run_script("scripts/transform.py")

    end = datetime.now()
    elapsed = (end - start).total_seconds()

    logging.info(f"===== PIPELINE FINALIZADO EM {elapsed:.2f} segundos =====")

if __name__ == "__main__":
    main()