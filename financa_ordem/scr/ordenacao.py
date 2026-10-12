from time import perf_counter

def valor_comparavel(valor):
    if isinstance(valor, str):
        return valor.casefold()
    return valor

def vem_depois(a, b, chave, reverso=False):
    valor_a = valor_comparavel(a[chave])
    valor_b = valor_comparavel(b[chave])
    if reverso:
        return valor_a < valor_b
    return valor_a > valor_b

def insertion_sort(registros, chave, reverso=False):
    inicio = perf_counter()
    dados = [registro.copy() for registro in registros]
    comparacoes = 0
    for i in range(1, len(dados)):
        atual = dados[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if vem_depois(dados[j], atual, chave, reverso):
                dados[j + 1] = dados[j]
                j -= 1
            else:
                break
        dados[j + 1] = atual
    tempo_ms = (perf_counter() - inicio) * 1000
    return dados, comparacoes, tempo_ms

def merge_sort(registros, chave, reverso=False):
    inicio = perf_counter()
    comparacoes = 0

    def ordenar(lista):
        nonlocal comparacoes
        if len(lista) <= 1:
            return lista
        meio = len(lista) // 2
        esquerda = ordenar(lista[:meio])
        direita = ordenar(lista[meio:])
        resultado = []
        i = j = 0
        while i < len(esquerda) and j < len(direita):
            comparacoes += 1
            if not vem_depois(esquerda[i], direita[j], chave, reverso):
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado

    dados = ordenar([registro.copy() for registro in registros])
    tempo_ms = (perf_counter() - inicio) * 1000
    return dados, comparacoes, tempo_ms

def heap_sort(registros, chave, reverso=False):
    inicio = perf_counter()
    comparacoes = 0
    dados = [registro.copy() for registro in registros]
    n = len(dados)

    def heapify(arr, n, i):
        nonlocal comparacoes
        maior = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2
        if esquerda < n:
            comparacoes += 1
            if vem_depois(arr[esquerda], arr[maior], chave, reverso):
                maior = esquerda
        if direita < n:
            comparacoes += 1
            if vem_depois(arr[direita], arr[maior], chave, reverso):
                maior = direita
        if maior != i:
            arr[i], arr[maior] = arr[maior], arr[i]
            heapify(arr, n, maior)

    for i in range(n // 2 - 1, -1, -1):
        heapify(dados, n, i)
    for i in range(n - 1, 0, -1):
        dados[i], dados[0] = dados[0], dados[i]
        heapify(dados, i, 0)
    tempo_ms = (perf_counter() - inicio) * 1000
    return dados, comparacoes, tempo_ms
