#Compartilhado por Nicollas Isaac Batista do Grupo 05
#Serve para importar as bases do postgrees
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

variable_value = os.getenv("POSTGREES_BLACK_BOX_KEY")
print(variable_value)

import pandas as pd
from sqlalchemy import create_engine, text

def download_postgres_to_csv(db_url, output_dir):
    # Conecta ao banco de dados PostgreSQL
    engine = create_engine(db_url)

    # Lista todas as tabelas no banco de dados
    with engine.connect() as conn:
        result = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
        tables = result.fetchall()

    # Cria o diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)
    
    # Itera sobre cada tabela e exporta os dados para CSV
    for table in tables:
        try:
            table_name = table[0]
            print(f"Baixando a tabela {table_name}...")

            # Lê os dados da tabela
            df = pd.read_sql(f"SELECT * FROM {table_name}", engine)

            # Define o caminho do arquivo CSV
            csv_file_path = os.path.join(output_dir, f"{table_name}.csv")

            # Salva os dados como CSV
            df.to_csv(csv_file_path, index=False)
            print(f"Tabela {table_name} salva em {csv_file_path}")
        except Exception as error:
            print("Um erro ocorreu ao tentar baixar a tabela", table_name)
            print(str(error))


# String de conexão para o banco de dados PostgreSQL
db_url = str(variable_value)

# Diretório de saída para os arquivos CSV
output_dir = "./csv"

# Baixa os dados do PostgreSQL e salva em CSV
download_postgres_to_csv(db_url, output_dir)
