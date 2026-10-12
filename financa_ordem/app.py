import streamlit as st
import pandas as pd

from pathlib import Path
from datetime import date

from scr.despesas import (
    carregar_despesas,
    salvar_despesas,
    adicionar_despesa,
    preparar_dados
)

from scr.ordenacao import insertion_sort, merge_sort


ARQUIVO = Path("dados/despesas.csv")

st.set_page_config(
    page_title="Finanças em Ordem",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Finanças em Ordem")
st.caption("Analisador de Gastos Pessoais — EDA2")

despesas = carregar_despesas(ARQUIVO)

# Cadastro de despesas
with st.sidebar:
    st.header("Nova despesa")

    with st.form("form_despesa"):
        descricao = st.text_input("Descrição")

        valor = st.number_input(
            "Valor (R$)",
            min_value=0.01,
            step=1.0
        )

        categoria = st.selectbox(
            "Categoria",
            [
                "Alimentação", "Transporte", "Moradia",
                "Estudos", "Saúde", "Lazer", "Contas", "Outros"
            ]
        )

        data_despesa = st.date_input(
            "Data",
            value=date.today()
        )

        enviar = st.form_submit_button("Cadastrar")

        if enviar:
            if not descricao.strip():
                st.error("Informe a descrição.")
            else:
                despesas = adicionar_despesa(
                    despesas,
                    descricao.strip(),
                    valor,
                    categoria,
                    data_despesa.isoformat()
                )

                salvar_despesas(despesas, ARQUIVO)
                st.rerun()


if despesas.empty:
    st.info("Cadastre uma despesa na barra lateral para começar.")
    st.stop()


df = preparar_dados(despesas)

# Seleção do mês
meses = sorted(
    df["data"].str.slice(0, 7).unique(),
    reverse=True
)

mes = st.selectbox(
    "Mês de análise",
    meses,
    format_func=lambda x: f"{x[5:7]}/{x[:4]}"
)

df_mes = df[df["data"].str.startswith(mes)].copy()

# Resumo financeiro
total = df_mes["valor"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total gasto", f"R$ {total:,.2f}")
col2.metric("Número de despesas", len(df_mes))
col3.metric("Categorias utilizadas", df_mes["categoria"].nunique())

# Gráfico por categoria
st.subheader("Gastos por categoria")

gastos_categoria = (
    df_mes.groupby("categoria")["valor"].sum()
)

st.bar_chart(gastos_categoria)

# Ordenação manual
st.subheader("Ordenar despesas")

col1, col2, col3 = st.columns(3)

with col1:
    criterio = st.selectbox(
        "Ordenar por",
        ["Valor", "Data", "Descrição", "Categoria"]
    )

with col2:
    ordem = st.selectbox(
        "Direção",
        ["Crescente", "Decrescente"]
    )

with col3:
    algoritmo_nome = st.selectbox(
        "Algoritmo",
        ["Insertion Sort", "Merge Sort recursivo"]
    )

chaves = {
    "Valor": "valor",
    "Data": "data",
    "Descrição": "descricao",
    "Categoria": "categoria"
}

algoritmos = {
    "Insertion Sort": insertion_sort,
    "Merge Sort recursivo": merge_sort
}

registros = df_mes.to_dict("records")

resultado, comparacoes, tempo_ms = algoritmos[algoritmo_nome](
    registros,
    chave=chaves[criterio],
    reverso=(ordem == "Decrescente")
)

tabela = pd.DataFrame(resultado)

st.dataframe(
    tabela[["descricao", "valor", "categoria", "data"]],
    use_container_width=True,
    hide_index=True
)

st.caption(
    f"Algoritmo: {algoritmo_nome} | "
    f"Comparações: {comparacoes} | "
    f"Tempo: {tempo_ms:.4f} ms"
)

# Ranking das cinco maiores despesas
st.subheader("🏆 Cinco maiores despesas")

ranking, _, _ = merge_sort(
    registros,
    chave="valor",
    reverso=True
)

top5 = pd.DataFrame(ranking[:5])

if not top5.empty:
    st.dataframe(
        top5[["descricao", "valor", "categoria", "data"]],
        use_container_width=True,
        hide_index=True
    )
