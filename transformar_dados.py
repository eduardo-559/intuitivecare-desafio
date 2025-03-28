import tabula
import pandas as pd
import zipfile

# Caminho do PDF
caminho_pdf = "anexos/anexo1.pdf"

# Lista para armazenar as tabelas válidas
tabelas_validas = []

print("Extraindo tabelas do PDF página por página...")

# Tenta ler da página 1 até 50 (ajustar depois)
for i in range(1, 51):
    try:
        print(f"Lendo página {i}...")
        tables = tabula.read_pdf(caminho_pdf, pages=i, multiple_tables=True)
        for t in tables:
            if isinstance(t, pd.DataFrame) and len(t.columns) > 2:
                tabelas_validas.append(t)
    except Exception as e:
        print(f"Erro na página {i}: {e}")

# Concatena tudo
df = pd.concat(tabelas_validas, ignore_index=True)

# Substituições
if "OD" in df.columns:
    df["OD"] = df["OD"].replace({"S": "Sim", "N": "Não"})
if "AMB" in df.columns:
    df["AMB"] = df["AMB"].replace({"S": "Sim", "N": "Não"})

# Salvar CSV
csv_nome = "dados_extraidos.csv"
df.to_csv(csv_nome, index=False)
print(f"CSV salvo como {csv_nome}")

# Compactar CSV
with zipfile.ZipFile("Teste_Eduardo.zip", "w") as zipf:
    zipf.write(csv_nome)
    print("ZIP criado: Teste_Eduardo.zip")
