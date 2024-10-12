"""script para extrair termos e definições de um PDF e gerar um CSV

  Returns:
      csv: com os termos e definições extraídos do PDF
"""
# Importar bibliotecas necessárias
import re
import logging
import pdfplumber
import openai
import pandas as pd

# Configurar o logging
logging.basicConfig(filename='termos_invalidos.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Função para extrair o texto do PDF
def extrair_texto_pdf(pdf_path):
    texto_completo = ""
    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            texto_completo += pagina.extract_text()
    return texto_completo


# Função para gerar uma definição de um termo usando GPT-4
def gerar_definicao(termo):
    prompt = f"Defina o termo '{termo}' no contexto de teste de software."
    resposta = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=256
    )
    return resposta.choices[0].text.strip()


# Função para identificar termos e suas definições no texto do PDF
def extrair_termos_definicoes(texto):
    termos_definicoes = []
    linhas = texto.split("\n")
    i = 0
    while i < len(linhas):
        linha = linhas[i].strip()
        # Remover o texto "Procurar resultados" que aparece no final de cada página
        linha = re.sub(r"Procurar resultados Página\W+\d+ de \d+", "", linha)

        if "Versão" in linha:  # Exemplo de padrão simples para termos
            termo = linha.split("Versão")[0].strip()
            definicao = ""
            i += 1
            while i < len(linhas) and "Versão" not in linhas[i]:
                # Remover o texto "Procurar resultados Página: x de y" das linhas subsequentes
                linha_definicao = re.sub(r'Procurar resultados Página: \d+ de \d+', '', linhas[i].strip())
                definicao += " " + linha_definicao
                i += 1
            if termo:  # Verificar se o termo não está vazio
                termos_definicoes.append({"Termo": termo, "Definição": definicao.strip()})
            else:
                # Logar o termo com a definição se o termo estiver vazio
                logging.info("Termo vazio encontrado. Definição: %s", definicao.strip())
        else:
            i += 1
    return termos_definicoes


# Função principal para processar o PDF e gerar o CSV
def processar_pdf_gerar_csv(pdf_path, csv_output_path):
    # Etapa 1: Extrair texto do PDF
    texto = extrair_texto_pdf(pdf_path)

    # Etapa 2: Extrair termos e definições
    termos_definicoes = extrair_termos_definicoes(texto)

    # Etapa 3: Gerar CSV
    df = pd.DataFrame(termos_definicoes)
    df.to_csv(csv_output_path, index=False)
    print(f"Arquivo CSV gerado: {csv_output_path}")


# Caminho do arquivo PDF de entrada
PDF_PATH = "search_result_11_10_2024.pdf"
# Caminho para o arquivo CSV de saída
CSV_OUTPUT_PATH = "termos_e_definicoes_teste_software.csv"

# Processar o PDF e gerar o CSV
processar_pdf_gerar_csv(PDF_PATH, CSV_OUTPUT_PATH)
