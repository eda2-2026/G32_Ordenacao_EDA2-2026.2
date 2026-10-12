import unittest
import pandas as pd
from src.analise import calcular_resumo, obter_top_5_despesas

class TestAnaliseFinanceira(unittest.TestCase):
    def setUp(self):
        self.dados_teste = pd.DataFrame([
            {"descricao": "Mercado", "valor": 150.0, "categoria": "Alimentação", "data": "2026-10-01"},
            {"descricao": "Cinema", "valor": 45.0, "categoria": "Lazer", "data": "2026-10-02"},
            {"descricao": "Ifood", "valor": 60.0, "categoria": "Alimentação", "data": "2026-10-03"},
            {"descricao": "Luz", "valor": 120.0, "categoria": "Contas", "data": "2026-10-04"},
            {"descricao": "Passagem", "valor": 20.0, "categoria": "Transporte", "data": "2026-10-05"},
            {"descricao": "Livro", "valor": 80.0, "categoria": "Estudos", "data": "2026-10-06"}
        ])
        self.registros = self.dados_teste.to_dict("records")

    def test_calcular_resumo(self):
        total, qtd, cat = calcular_resumo(self.dados_teste)
        self.assertEqual(total, 475.0)
        self.assertEqual(qtd, 6)
        self.assertEqual(cat, 5)

    def test_calcular_resumo_vazio(self):
        df_vazio = pd.DataFrame(columns=["descricao", "valor", "categoria", "data"])
        total, qtd, cat = calcular_resumo(df_vazio)
        self.assertEqual(total, 0.0)
        self.assertEqual(qtd, 0)
        self.assertEqual(cat, 0)

    def test_obter_top_5_despesas(self):
        top5 = obter_top_5_despesas(self.registros)
        self.assertEqual(len(top5), 5)
        self.assertEqual(top5[0]["descricao"], "Mercado")
        self.assertEqual(top5[1]["descricao"], "Luz")
        self.assertEqual(top5[-1]["valor"], 45.0)

if __name__ == "__main__":
    unittest.main()
