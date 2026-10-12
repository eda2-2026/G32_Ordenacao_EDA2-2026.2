import pandas as pd
from src.ordenacao import merge_sort

def calcular_resumo(df_mes):
    if df_mes.empty:
        return 0.0, 0, 0
    total = float(df_mes["valor"].sum())
    quantidade = len(df_mes)
    categorias = df_mes["categoria"].nunique()
    return total, quantidade, categorias

def obter_top_5_despesas(registros):
    if not registros:
        return []
    ranking, _, _ = merge_sort(registros, chave="valor", reverso=True)
    return ranking[:5]
