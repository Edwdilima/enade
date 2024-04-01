from src.db.connection import connect
from src.sql.querry import *
from src.repository.pds import *

def get_acertos_ofg_rt_2011():
    try:
        conexao = connect()
        cursor = conexao.cursor()

        # Executando a consulta SQL
        cursor.execute(questoes_ofg_certas_2011_rio_tinto)
        resultados = cursor.fetchall()

        # Fechando o cursor e a conexão
        cursor.close()
        conexao.close()

        persistir_resultado_questoes_ofg_corretas_rt_2011(resultados)
        print("Success")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever os resultados no arquivo CSV: {str(e)}")

def get_acertos_oce_rt_2011():
    try:
        conexao = connect()
        cursor = conexao.cursor()

        # Executando a consulta SQL
        cursor.execute(questoes_oce_certas_2011_rio_tinto)
        resultados = cursor.fetchall()

        # Fechando o cursor e a conexão
        cursor.close()
        conexao.close()

        persistir_resultado_questoes_oce_corretas_rt_2011(resultados)
        print("Success")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever os resultados no arquivo CSV: {str(e)}")

get_acertos_ofg_rt_2011()
get_acertos_oce_rt_2011()