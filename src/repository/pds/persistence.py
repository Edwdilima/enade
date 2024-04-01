import csv

import pandas as pd
from src.repository.pds import *
from src.repository.pds import read_file


# o parâmetro da função é um data_frame e o caminho de onde o arquivo deve persistir
def to_excel_table(dados, excel_file):
    with pd.ExcelWriter(excel_file) as writer:
        for i, chunk in enumerate(dados):
            chunk.to_excel(writer, sheet_name=f'Sheet_{i+1}', index=False)
    return success

# salvar dados .txt em planilhas individualmente
def save_only_archive(file, path):
    chunks = read_file(file)
    msg = to_excel_table(chunks, path)
    return msg

# para salvar data frame em planilha
def save_to_excel(data_frame, excel_file):
    try:
        # Escreve o DataFrame em um arquivo Excel
        data_frame.to_excel(excel_file, index=False)
        return "Salvo com sucesso!"
    except Exception as e:
        return f"Erro ao salvar: {str(e)}"

## para csv

def converter_to_number(value):
    try:
        return int(ast.literal_eval(value))
    except (SyntaxError, ValueError):
        return value


def converter_txt_para_csv(arquivo_txt, arquivo_csv):
    df = pd.read_csv(arquivo_txt, delimiter=';', dtype=str)

    for coluna in df.columns:
        df[coluna] = df[coluna].apply(converter_to_number)

    df.to_csv(arquivo_csv, index=False)

# Importe apenas o pandas dentro da função
def converter_csv_para_inteiro(input_file, output_file):
    # Carregar o arquivo CSV
    df = pd.read_csv(input_file, dtype=str)

    # Remover as aspas das colunas
    df.columns = df.columns.str.replace('"', '')

    # Remover as aspas dos valores e converter para inteiros
    for col in df.columns:
        df[col] = df[col].str.replace('"', '').astype(int)

    # Salvar o DataFrame de volta para o arquivo CSV
    df.to_csv(output_file, index=False)

######################################################
########### Funções específicas do projeto ###########
######################################################

# Persistir_resultado_questoes_certas_rt_2011 função para resgatar registros da quantidade de questões certas na
# parte das questões de objetivo da formação geral
def persistir_resultado_questoes_ofg_corretas_rt_2011(resultados):
    # Criando um arquivo CSV para escrever os resultados
    with open('/home/luiz/Documentos/workspace/enade/src/repository/csv/resultado_rt_ofg_2011.csv', 'w', newline='') as arquivo_csv:
        escrever_csv = csv.writer(arquivo_csv)
        # Escrevendo o cabeçalho
        escrever_csv.writerow(['ds_vt_ace_ofg', 'corretas', 'erradas', 'total_questoes', 'taxa_acerto_percentual'])
        # Iterando sobre os resultados
        for linha in resultados:
            ds_vt_ace_ofg = linha[1].strip('"')
            # Contagem de acertos e erros
            corretas = ds_vt_ace_ofg.count('1')
            erradas = ds_vt_ace_ofg.count('0')
            total_questoes = len(ds_vt_ace_ofg)
            taxa_acerto_percentual = (corretas / total_questoes) * 100 if total_questoes != 0 else 0
            # Escrevendo os dados no CSV
            escrever_csv.writerow([ds_vt_ace_ofg, corretas, erradas, total_questoes, taxa_acerto_percentual])

# Persistir_resultado_questoes_oce_corretas_rt_2011 função para resgatar registros da quantidade de questões certas na
# parte das questões de objetivo de conhecimento específico
def persistir_resultado_questoes_oce_corretas_rt_2011(resultados):
    # Criando um arquivo CSV para escrever os resultados
    with open('/home/luiz/Documentos/workspace/enade/src/repository/csv/resultado_rt_oce_2011.csv', 'w', newline='') as arquivo_csv:
        escrever_csv = csv.writer(arquivo_csv)
        # Escrevendo o cabeçalho
        escrever_csv.writerow(
            ['ds_vt_ace', 'corretas', 'erradas', 'questoes_anuladas', 'total_questoes', 'taxa_acerto_percentual'])
        # Iterando sobre os resultados
        for linha in resultados:
            ds_vt_ace = linha[1].strip('"')
            # Contagem de acertos, erros e questões anuladas
            corretas = ds_vt_ace.count('1')
            erradas = ds_vt_ace.count('0')
            questoes_anuladas = ds_vt_ace.count('9')
            total_questoes = len(ds_vt_ace)
            taxa_acerto_percentual = (corretas / total_questoes) * 100 if total_questoes != 0 else 0
            # Escrevendo os dados no CSV
            escrever_csv.writerow(
                [ds_vt_ace, corretas, erradas, questoes_anuladas, total_questoes, taxa_acerto_percentual])