# Finanças em Ordem — Analisador de Gastos Pessoais

## Integrantes
| Matrícula | Nome |
| :--- | :--- |
| 231027005 | Maria Samara |
| 2310391400 | Marjorie Mitzi |

##  Vídeo da Apresentação
**

## 1. Sobre o projeto

O Finanças em Ordem é uma aplicação desenvolvida em Python para registrar e analisar despesas pessoais. O sistema permite cadastrar gastos, consultar os valores de um mês, visualizar despesas por categoria e ordenar os registros utilizando algoritmos de ordenação estudados na disciplina de Estruturas de Dados 2 (EDA2).

## 2. Funcionalidades

- Cadastro de despesas com descrição, valor, categoria e data.
- Armazenamento dos dados em arquivo CSV.
- Filtro das despesas por mês.
- Cálculo do total gasto, quantidade de despesas e número de categorias utilizadas.
- Gráfico de gastos por categoria.
- Ordenação por valor, data, descrição ou categoria.
- Ordenação crescente ou decrescente.
- Comparação do número de comparações e do tempo de execução dos algoritmos.
- Ranking das cinco maiores despesas.

## 3. Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- CSV
- Unittest

## 4. Algoritmos de ordenação

### Insertion Sort

Ordena os registros inserindo cada elemento na posição correta em relação aos elementos já percorridos.

### Merge Sort recursivo

Divide a lista em partes menores, ordena essas partes recursivamente e combina os resultados em uma única lista ordenada.

## 5. Estrutura do projeto

- `app.py`: interface e integração das funcionalidades.
- `src/despesas.py`: funções de carregamento, cadastro, preparação e salvamento das despesas.
- `src/ordenacao.py`: implementação dos algoritmos de ordenação.
- `tests/test_ordenacao.py`: testes automatizados dos algoritmos.
- `dados/despesas.csv`: arquivo de armazenamento das despesas.
- `requirements.txt`: dependências do projeto.

## 6. Como executar

1. Instale o Python.
2. Crie e ative um ambiente virtual.
3. Instale as dependências com `python -m pip install -r requirements.txt`.
4. Execute os testes com `python -m unittest discover -s tests -v`.
5. Inicie a aplicação com `python -m streamlit run app.py`.
