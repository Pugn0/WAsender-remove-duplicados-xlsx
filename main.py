import pandas as pd
import os

# Caminho da pasta com os arquivos .xlsx
pasta = "tel"
todos_numeros = []

# Lê todos os arquivos .xlsx da pasta
for arquivo in os.listdir(pasta):
    if arquivo.endswith(".xlsx"):
        caminho_arquivo = os.path.join(pasta, arquivo)
        df = pd.read_excel(caminho_arquivo)
        
        # Ajuste o nome da coluna conforme necessário (ex: "Número")
        if "Número" in df.columns:
            numeros = df["Número"].dropna().astype(str).tolist()
            todos_numeros.extend(numeros)

# Remove duplicatas e salva em um TXT
numeros_unicos = list(set(todos_numeros))
with open("numeros_unicos.txt", "w", encoding="utf-8") as f:
    for numero in numeros_unicos:
        f.write(f"{numero}\n")

print(f"{len(numeros_unicos)} números únicos salvos em 'numeros_unicos.txt'.")

# Releitura e verificação final
with open("numeros_unicos.txt", "r", encoding="utf-8") as f:
    linhas = [linha.strip() for linha in f if linha.strip()]

# Verifica duplicatas
sem_repeticao_final = list(set(linhas))

if len(sem_repeticao_final) < len(linhas):
    print("Havia duplicatas no TXT. Removendo e regravando...")
    with open("numeros_unicos.txt", "w", encoding="utf-8") as f:
        for numero in sem_repeticao_final:
            f.write(f"{numero}\n")
    print(f"Agora há {len(sem_repeticao_final)} números únicos no arquivo.")
else:
    print("O arquivo já estava sem duplicatas.")
