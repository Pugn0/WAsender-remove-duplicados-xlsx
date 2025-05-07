### 📁 **Remoção de Números Duplicados e Divisão de Arquivos TXT**

Este script em Python permite **ler vários arquivos `.xlsx` de uma pasta**, extrair os números de uma coluna específica (ex: "Número"), **remover duplicados**, **salvar todos os números únicos em um arquivo `.txt`**, e **dividir o arquivo `.txt` em partes menores**. Após a execução, o usuário pode escolher se quer processar arquivos `.xlsx` ou dividir arquivos `.txt` em lotes menores.

---

## 🚀 Funcionalidades

* Lê automaticamente todos os arquivos `.xlsx` em uma pasta.
* Extrai números da coluna "Número" (ajustável).
* Remove números duplicados entre todos os arquivos.
* Salva os dados únicos em um arquivo `numeros_unicos.txt`.
* Verifica se o `.txt` está sem duplicatas e corrige se necessário.
* **Divisão de arquivos `.txt`**: Selecione um arquivo `.txt` para dividir em partes menores com a quantidade de números desejada.
* **Exibição interativa** de arquivos e contagem de números.

---

## 🧰 Requisitos

* Python 3.7+
* Bibliotecas:

  * `pandas`
  * `openpyxl`

---

## 🔧 Instalação

1. Clone o repositório ou baixe os arquivos.

2. Crie e ative um ambiente virtual:

```bash
python -m venv env

# Ativar no Windows
env\Scripts\activate

# Ativar no macOS/Linux
source env/bin/activate
```

3. Instale as dependências:

```bash
pip install pandas openpyxl
```

---

## 📂 Como usar

1. Coloque todos os arquivos `.xlsx` que deseja processar dentro de **tel**.

2. No script Python, altere a variável `pasta` para o caminho dessa pasta:

3. Execute o script:

```bash
python main.py
```

4. O script exibirá um menu com as opções:

   * **1**: Remover duplicados dos arquivos `.xlsx` e salvar em `base/`
   * **2**: Listar arquivos `.txt` de `base/` e dividir em partes menores

5. Após a execução, será gerado o arquivo `numeros_unicos.txt` na pasta `base/`, e, se escolher dividir, os arquivos divididos serão salvos na pasta `leads/`.

---

## ✉️ Suporte

Se precisar de ajuda, fale comigo no Telegram: [@pugno\_fc](https://t.me/pugno_fc)

---

## ⚠️ Observações

* Certifique-se de que os arquivos `.xlsx` tenham a coluna chamada **"Número"**. Caso esteja com outro nome, altere no código:

```python
if "Número" in df.columns:
```

para:

```python
if "SeuNomeDeColuna" in df.columns:
```

---

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar.
