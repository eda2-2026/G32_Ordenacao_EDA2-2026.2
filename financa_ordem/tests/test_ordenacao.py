import unittest

from scr.ordenacao import insertion_sort, merge_sort

REGISTROS = [
    {
        "descricao": "Mercado",
        "valor": 120.0,
        "categoria": "Alimentação",
        "data": "2026-10-02"
    },
    {
        "descricao": "Ônibus",
        "valor": 8.0,
        "categoria": "Transporte",
        "data": "2026-10-01"
    },
    {
        "descricao": "Cinema",
        "valor": 35.0,
        "categoria": "Lazer",
        "data": "2026-10-03"
    }
]


class TestOrdenacao(unittest.TestCase):

    def test_insertion_sort_crescente(self):
        resultado, _, _ = insertion_sort(REGISTROS, "valor")

        self.assertEqual(
            [r["valor"] for r in resultado],
            [8.0, 35.0, 120.0]
        )

    def test_merge_sort_crescente(self):
        resultado, _, _ = merge_sort(REGISTROS, "valor")

        self.assertEqual(
            [r["valor"] for r in resultado],
            [8.0, 35.0, 120.0]
        )

    def test_ordem_decrescente(self):
        for algoritmo in (insertion_sort, merge_sort):
            resultado, _, _ = algoritmo(
                REGISTROS, "valor", reverso=True
            )

            self.assertEqual(
                [r["valor"] for r in resultado],
                [120.0, 35.0, 8.0]
            )

    def test_ordenacao_por_descricao(self):
        resultado, _, _ = merge_sort(REGISTROS, "descricao")

        descricoes = [r["descricao"] for r in resultado]

        self.assertEqual(
            descricoes,
            sorted(descricoes, key=str.casefold)
        )

    def test_lista_original_nao_e_alterada(self):
        original = [registro.copy() for registro in REGISTROS]

        insertion_sort(REGISTROS, "valor")
        merge_sort(REGISTROS, "valor")

        self.assertEqual(REGISTROS, original)

    def test_lista_vazia(self):
        for algoritmo in (insertion_sort, merge_sort):
            resultado, comparacoes, _ = algoritmo([], "valor")

            self.assertEqual(resultado, [])
            self.assertEqual(comparacoes, 0)


if __name__ == "__main__":
    unittest.main()
