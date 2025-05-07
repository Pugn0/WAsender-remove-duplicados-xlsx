import pandas as pd
import os

def extrair_numeros_xlsx():
    pasta_xlsx = "tel"
    pasta_saida = "base"
    os.makedirs(pasta_saida, exist_ok=True)
    
    todos_numeros = []

    for arquivo in os.listdir(pasta_xlsx):
        if arquivo.endswith(".xlsx"):
            caminho_arquivo = os.path.join(pasta_xlsx, arquivo)
            df = pd.read_excel(caminho_arquivo)

            if "Número" in df.columns:
                numeros = df["Número"].dropna().astype(str).tolist()
                todos_numeros.extend(numeros)

    numeros_unicos = list(set(todos_numeros))
    saida_txt = os.path.join(pasta_saida, "numeros_unicos.txt")

    with open(saida_txt, "w", encoding="utf-8") as f:
        for numero in numeros_unicos:
            f.write(f"{numero}\n")

    print(f"[✓] {len(numeros_unicos)} números únicos salvos em '{saida_txt}'.")

    # Verifica duplicatas no TXT final
    with open(saida_txt, "r", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f if linha.strip()]
    sem_repeticao_final = list(set(linhas))

    if len(sem_repeticao_final) < len(linhas):
        print("[!] Havia duplicatas no TXT. Removendo e regravando...")
        with open(saida_txt, "w", encoding="utf-8") as f:
            for numero in sem_repeticao_final:
                f.write(f"{numero}\n")
        print(f"[✓] Agora há {len(sem_repeticao_final)} números únicos no arquivo.")
    else:
        print("[✓] O arquivo já estava sem duplicatas.")

def contar_linhas_txt(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return sum(1 for linha in f if linha.strip())

def formatar_milhar(valor):
    return f"{valor:,}".replace(",", ".")

def listar_txts(diretorio):
    txts = [f for f in os.listdir(diretorio) if f.endswith(".txt")]
    if not txts:
        print("[!] Nenhum arquivo .txt encontrado.")
        return []
    
    print("\nArquivos disponíveis:")
    for idx, nome in enumerate(txts, start=1):
        caminho = os.path.join(diretorio, nome)
        total = contar_linhas_txt(caminho)
        print(f"{idx:02d}) {nome} - {formatar_milhar(total)} números")
    return txts

def dividir_txt_em_partes(caminho_arquivo, tamanho_lote, pasta_destino):
    nome_arquivo = os.path.basename(caminho_arquivo)
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f if linha.strip()]

    os.makedirs(pasta_destino, exist_ok=True)

    for i in range(0, len(linhas), tamanho_lote):
        lote = linhas[i:i + tamanho_lote]
        nome_saida = os.path.join(pasta_destino, f"{nome_arquivo.replace('.txt','')}_parte_{i//tamanho_lote + 1}.txt")
        with open(nome_saida, "w", encoding="utf-8") as f_out:
            for numero in lote:
                f_out.write(f"{numero}\n")

    print(f"[✓] {nome_arquivo} dividido em {len(linhas) // tamanho_lote + 1} partes na pasta '{pasta_destino}'.")

def dividir_arquivos_txt():
    pasta_base = "base"
    pasta_saida = "leads"

    arquivos_txt = listar_txts(pasta_base)
    if not arquivos_txt:
        return

    opcao = input("\nDigite o número do arquivo para dividir (ou 'todos' para processar todos): ").strip().lower()
    try:
        tamanho_lote = int(input("Quantos números por novo arquivo? Ex: 300: ").strip())
    except ValueError:
        print("[!] Valor inválido para quantidade.")
        return

    if opcao == "todos":
        for arquivo in arquivos_txt:
            dividir_txt_em_partes(os.path.join(pasta_base, arquivo), tamanho_lote, pasta_saida)
    else:
        try:
            idx = int(opcao) - 1
            if 0 <= idx < len(arquivos_txt):
                dividir_txt_em_partes(os.path.join(pasta_base, arquivos_txt[idx]), tamanho_lote, pasta_saida)
            else:
                print("[!] Número inválido.")
        except ValueError:
            print("[!] Entrada inválida.")

# === MENU PRINCIPAL ===
def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Remover duplicados dos arquivos XLSX e salvar em base/")
        print("2 - Listar arquivos TXT da base/ e dividir em partes")
        print("0 - Sair")

        escolha = input("Digite sua opção: ").strip()

        if escolha == "1":
            extrair_numeros_xlsx()
        elif escolha == "2":
            dividir_arquivos_txt()
        elif escolha == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Início do script
if __name__ == "__main__":
    menu()
