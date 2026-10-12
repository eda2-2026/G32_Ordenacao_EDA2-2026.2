import pandas as pd
from pathlib import Path

COLUNAS = ["descricao", "valor", "categoria", "data"]

def carregar_despesas(caminho):
    caminho = Path(caminho)
    if not caminho.exists():
        caminho.parent.mkdir(parents=True, exist_ok=True)
        return pd.DataFrame(columns=COLUNAS)
    try:
        despesas = pd.read_csv(caminho)
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=COLUNAS)
    
    for coluna in COLUNAS:
        if coluna not in despesas.columns:
            despesas[coluna] = None
    despesas = despesas[COLUNAS]
    if not despesas.empty:
        despesas["valor"] = pd.to_numeric(despesas["valor"], errors="coerce").fillna(0.0)
        despesas["data"] = despesas["data"].astype(str)
    return despesas

def salvar_despesas(despesas, caminho):
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    despesas[COLUNAS].to_csv(caminho, index=False)

def adicionar_despesa(despesas, descricao, valor, categoria, data):
    nova_despesa = pd.DataFrame([{
        "descricao": descricao,
        "valor": float(valor),
        "categoria": categoria,
        "data": data
    }])
    return pd.concat([despesas, nova_despesa], ignore_index=True)

def preparar_dados(despesas):
    resultado = despesas.copy()
    resultado["descricao"] = resultado["descricao"].fillna("").astype(str)
    resultado["valor"] = pd.to_numeric(resultado["valor"], errors="coerce").fillna(0.0)
    resultado["categoria"] = resultado["categoria"].fillna("Outros").astype(str)
    resultado["data"] = resultado["data"].astype(str)
    return resultado
