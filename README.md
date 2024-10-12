# PDF to CSV Converter

Este projeto contém um script Python que extrai termos e definições de um arquivo PDF e os exporta para um arquivo CSV.

## Descrição

O script `pdf_to_csv.py` processa um arquivo PDF do Glossário de Termos da certificação [CTFL](https://bstqb.online/ctfl), extrai termos e suas definições e gera um arquivo CSV com esses dados. Ele também remove textos indesejados e loga termos vazios em um arquivo de log.
Depois poder ser importado em algum gerador de flashcards para estudos. (Ex: Anki)

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. Para instalá-las, execute:

```sh
pip install -r requirements.txt
```
# Como Executar
## 1. Clone o repositório

```
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

## 2. Crie e ative um ambiente virtual:  

#### No macOS/Linux

```

python -m venv venv
source venv/bin/activate  

```
> .\venv\Scripts\activate  # No Windows

## 3. Instale as dependências:

```
pip install -r requirements.txt
```

## 4. Certifique-se de que o caminho do arquivo PDF (pdf_path) esteja correto no script.

```
pdf_path = "caminho/para/seu/arquivo.pdf"
csv_output_path = "termos_e_definicoes_teste_software.csv"

```

## 5. Execute o script: 

```python
python pdf_to_csv.py
```
