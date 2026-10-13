# Finanças em Ordem — Analisador de Gastos Pessoais

## Integrantes
| Matrícula | Nome | 
| ----- | ----- | 
| 231027005 | Maria Samara | 
| 231039140 | Marjorie Mitzi | 

> [!NOTE]
> **Vídeo da Apresentação**
> **Assista à nossa apresentação:** [Projeto Finanças em Ordem (EDA2)](https://www.youtube.com/watch?v=ZAGSqrX1faQ)

---

## 1. Sobre o projeto

O **Finanças em Ordem** é uma aplicação desenvolvida em Python para registrar e analisar despesas pessoais. O sistema permite cadastrar gastos, consultar os valores de um mês, visualizar despesas por categoria e ordenar os registros utilizando três algoritmos de ordenação estudados na disciplina de Estruturas de Dados 2 (EDA2): **Insertion Sort**, **Merge Sort** e **Heap Sort**.

## 2. Funcionalidades

- **Cadastro persistente:** Adição de despesas com descrição, valor, categoria e data, salvas automaticamente em um arquivo CSV.
- **Filtro mensal:** Isolamento e visualização das despesas por mês específico.
- **Resumo financeiro:** Cálculo dinâmico do total gasto, quantidade de despesas e número de categorias utilizadas no período.
- **Gráficos interativos:** Visualização de gastos por categoria.
- **Ordenação multicritério:** Organização da tabela de registros por valor, data, descrição ou categoria, em direção crescente ou decrescente.
- **Comparativo de Desempenho:** Painel com gráficos em tempo real mostrando o número de comparações e o tempo de execução (ms) de cada algoritmo para a massa de dados atual.
- **Ranking Automático:** Identificação e exibição das 5 maiores despesas do mês utilizando ordenação decrescente (*Top 5*).

## 3. Tecnologias utilizadas

- **Python 3** (Linguagem principal)
- **Streamlit** (Interface Web)
- **Pandas** (Leitura, manipulação e estruturação dos dados)
- **Unittest** (Testes automatizados e validação de qualidade)
- **CSV** (Persistência e armazenamento local)

## 4. Algoritmos de ordenação implementados

- **Insertion Sort:** Ordena os registros inserindo cada elemento na posição correta em relação aos elementos já percorridos. Eficiente para listas pequenas ou quase ordenadas. Tem complexidade $O(n^2)$ no pior caso.
- **Merge Sort (recursivo):** Utiliza a estratégia de "dividir para conquistar". Quebra a lista recursivamente em partes menores até ter elementos únicos e, em seguida, intercala essas partes já em ordem. Garante complexidade $O(n \log n)$.
- **Heap Sort:** Modela a lista como uma árvore binária (*Max-Heap*). Extrai repetidamente o maior elemento para o final da estrutura e refaz a propriedade do *heap*. Destaca-se por ter complexidade $O(n \log n)$ e ordenar *in-place* (com uso mínimo de memória auxiliar).

## 5. Estrutura do projeto

O código foi refatorado para manter a lógica de negócios, a ordenação e os testes separados da interface gráfica:

```text
financa_ordem/
├── app.py                   # Interface web principal e integração dos módulos
├── requirements.txt         # Dependências do sistema (streamlit==1.10.0, pandas==1.1.5)
├── README.md                # Documentação
├── dados/
│   └── despesas.csv         # Banco de dados local baseado em texto
├── src/
│   ├── __init__.py
│   ├── despesas.py          # Lógica de carregamento, cadastro e formatação de dados
│   ├── ordenacao.py         # Implementação do Insertion, Merge e Heap Sort
│   └── analise.py           # Funções de cálculo do resumo financeiro e Top 5
└── tests/
    ├── __init__.py
    ├── test_ordenacao.py    # Bateria de testes para os três algoritmos
    └── test_analise.py      # Bateria de testes para os cálculos de negócios
```

## 6. Como executar o sistema

Certifique-se de que o seu terminal está aberto na pasta raiz do projeto (`financa_ordem`).

### Passo 1 — Crie e ative o ambiente virtual

No Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> [!TIP]
> **Execução no Windows**
> Utilize `python -m venv .venv` e ative o ambiente virtual executando `.\.venv\Scripts\Activate.ps1`.

### Passo 2 — Instale as dependências

```bash
python3 -m pip install -r requirements.txt
```

### Passo 3 — Valide a lógica com os testes automatizados

```bash
python3 -m unittest discover -s tests -v
```

> [!NOTE]
> **Qualidade Garantida**
> Todos os testes das categorias `test_analise` e `test_ordenacao` devem retornar um status OK verde, garantindo que os algoritmos funcionam perfeitamente.

### Passo 4 — Inicie a aplicação Web

```bash
python3 -m streamlit run app.py
```

A aplicação abrirá automaticamente no seu navegador padrão (normalmente no endereço `http://localhost:8501`).
