import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date
from src.despesas import (
    carregar_despesas,
    salvar_despesas,
    adicionar_despesa,
    preparar_dados
)
from src.ordenacao import insertion_sort, merge_sort, heap_sort
from src.analise import calcular_resumo, obter_top_5_despesas

ARQUIVO = Path("dados/despesas.csv")

st.set_page_config(page_title="Finanças em Ordem", page_icon="💰", layout="wide")
st.title("💰 Finanças em Ordem")
st.caption("Analisador de Gastos Pessoais — EDA2")

despesas = carregar_despesas(ARQUIVO)

with st.sidebar:
    st.header("Nova despesa")
    with st.form("form_despesa"):
        descricao = st.text_input("Descrição")
        valor = st.number_input("Valor (R$)", min_value=0.01, step=1.0)
        categoria = st.selectbox(
            "Categoria",
            ["Alimentação", "Transporte", "Moradia", "Estudos", "Saúde", "Lazer", "Contas", "Outros"]
        )
        data_despesa = st.date_input("Data", value=date.today())
        enviar = st.form_submit_button("Cadastrar")

        if enviar:
            if not descricao.strip():
                st.error("Informe a descrição.")
            else:
                despesas = adicionar_despesa(
                    despesas, descricao.strip(), valor, categoria, data_despesa.isoformat()
                )
                salvar_despesas(despesas, ARQUIVO)
                st.experimental_rerun()

if despesas.empty:
    st.info("Cadastre uma despesa na barra lateral para começar.")
    st.stop()

df = preparar_dados(despesas)

meses = sorted(df["data"].str.slice(0, 7).unique(), reverse=True)
mes = st.selectbox("Mês de análise", meses, format_func=lambda x: f"{x[5:7]}/{x[:4]}")
df_mes = df[df["data"].str.startswith(mes)].copy()

# Resumo financeiro refatorado (Pessoa 2)
total, qtd, cat = calcular_resumo(df_mes)
col1, col2, col3 = st.columns(3)
col1.metric("Total gasto", f"R$ {total:,.2f}")
col2.metric("Número de despesas", qtd)
col3.metric("Categorias utilizadas", cat)

st.subheader("Gastos por categoria")
gastos_categoria = df_mes.groupby("categoria")["valor"].sum()
st.bar_chart(gastos_categoria)

# Ordenação de registros
st.subheader("Ordenar despesas")
col1, col2, col3 = st.columns(3)
with col1:
    criterio = st.selectbox("Ordenar por", ["Valor", "Data", "Descrição", "Categoria"])
with col2:
    ordem = st.selectbox("Direção", ["Crescente", "Decrescente"])
with col3:
    algoritmo_nome = st.selectbox("Algoritmo", ["Insertion Sort", "Merge Sort recursivo", "Heap Sort"])

chaves = {"Valor": "valor", "Data": "data", "Descrição": "descricao", "Categoria": "categoria"}
algoritmos = {
    "Insertion Sort": insertion_sort,
    "Merge Sort recursivo": merge_sort,
    "Heap Sort": heap_sort
}

registros = df_mes.to_dict("records")
reverso = (ordem == "Decrescente")
chave_ordenacao = chaves[criterio]

resultado, comparacoes, tempo_ms = algoritmos[algoritmo_nome](registros, chave=chave_ordenacao, reverso=reverso)

tabela = pd.DataFrame(resultado)
st.dataframe(tabela[["descricao", "valor", "categoria", "data"]])
st.caption(f"Algoritmo: {algoritmo_nome} | Comparações: {comparacoes} | Tempo: {tempo_ms:.4f} ms")

# Comparativo de Desempenho (Pessoa 2)
st.subheader("📊 Comparativo de Desempenho")
dados_comparativo = []
for nome, func in algoritmos.items():
    _, comp, tempo = func(registros, chave=chave_ordenacao, reverso=reverso)
    dados_comparativo.append({"Algoritmo": nome, "Comparações": comp, "Tempo (ms)": tempo})

df_comp = pd.DataFrame(dados_comparativo)

colA, colB = st.columns(2)
with colA:
    st.write("**Número de Comparações**")
    st.bar_chart(df_comp.set_index("Algoritmo")["Comparações"])
with colB:
    st.write("**Tempo de Execução (ms)**")
    st.bar_chart(df_comp.set_index("Algoritmo")["Tempo (ms)"])

# Ranking das cinco maiores despesas (Pessoa 2)
st.subheader("🏆 Cinco maiores despesas")
top5_lista = obter_top_5_despesas(registros)
top5 = pd.DataFrame(top5_lista)
if not top5.empty:
    st.dataframe(top5[["descricao", "valor", "categoria", "data"]])