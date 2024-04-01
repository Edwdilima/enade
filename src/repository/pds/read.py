import pandas as pd
import openpyxl

success = "Gravado com sucesso!"

# lê arquivos .txt em lotes
def read_file(file_path, chunk_size=10000):
    chunks = pd.read_csv(file_path, sep=";", index_col=False, chunksize=chunk_size, dtype='unicode')
    return chunks

# lê arquivos excel em lotes
def read_excel(file_path):
    table = pd.read_excel(file_path, encoding='latin1')
    return table

#lê arquivos excel por aba
def read_excel_tab(file_path, tab):
    table = pd.read_excel(file_path, sheet_name=tab, header=5)
    return table

## deve retornar todos os códigos de curso da região nordeste
def show_co_curso_ne_region(file_path, area_avaliacao_desejada, Sigla_uf):
    # Carregando o arquivo Excel com openpyxl
    wb = openpyxl.load_workbook(file_path)

    # Selecionando a primeira planilha
    sheet = wb.active

    # Obtendo os dados da planilha e convertendo para DataFrame do pandas
    data = sheet.values
    colunas = next(data)  # Assume-se que a primeira linha contém os cabeçalhos das colunas
    planilha = pd.DataFrame(data, columns=colunas)

    # Definindo os critérios de filtro
    siglas_nordeste = ['MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'SE', 'AL', 'BA']

    # Aplicando os filtros
    nova_tabela = planilha[(planilha['Área de Avaliação'] == area_avaliacao_desejada) & (planilha[Sigla_uf].isin(siglas_nordeste))]

    # Extraindo os códigos de curso da nova tabela
    codigos_de_curso = nova_tabela['Código do Curso'].unique()

    # Exibindo os códigos de curso
    print(codigos_de_curso)

## deve retornar todos os códigos de curso
def show_co_curso_country(file_path, area_avaliacao_desejada):
    # Carregar o arquivo Excel
    planilha = pd.read_excel(file_path)

    # Filtrar os dados com base na coluna 'Área de Avaliação' contendo 'SISTEMAS DE INFORMAÇÃO'
    filtro = planilha[planilha['Área de Avaliação'].str.contains(area_avaliacao_desejada, na=False)]

    # Obter os 'Código do Curso' correspondentes
    codigos_do_curso = filtro['Código do Curso'].tolist()

    # Imprimir os resultados
    print("Códigos dos cursos de Sistemas de Informação:")
    print(codigos_do_curso)


