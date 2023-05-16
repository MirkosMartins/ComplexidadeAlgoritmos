def quickSort(listaPalavras):
    quickSortHelper(listaPalavras, 0, len(listaPalavras)-1)


def quickSortHelper(listaPalavras, first, last):
    if first < last:

        splitpoint = partition(listaPalavras, first, last)

        quickSortHelper(listaPalavras, first, splitpoint-1)
        quickSortHelper(listaPalavras, splitpoint+1, last)


def partition(listaPalavras, first, last):
    pivotvalue = listaPalavras[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and listaPalavras[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while listaPalavras[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = listaPalavras[leftmark]
            listaPalavras[leftmark] = listaPalavras[rightmark]
            listaPalavras[rightmark] = temp

    temp = listaPalavras[first]
    listaPalavras[first] = listaPalavras[rightmark]
    listaPalavras[rightmark] = temp

    return rightmark


'''
***** Atividade QuickSort *****
- Crie uma lista com 200 palavras (em português)
- Ordene a lista usando QuickSort (tem que ser um método/função separada)
- Calcule o polinômio característico dos métodos/funções
- Defina o Big O do programa COMPLETO

código adaptado de: https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OQuickSort.html
'''

# TODO: colocar 200 palavras diferentes em português na lista, não pode acentos
listaPalavras = ['acucar', 'cadeira', 'macaco', 'felicidade', 'celular', 'piano', 'jardim', 'chocolate', 'aviao', 'bola', 'laranja',
                 'guitarra', 'cachorro', 'mesa', 'arco-iris', 'livro', 'bicicleta', 'sorvete', 'sol', 'lua', 'computador', 'caneta', 'sapato', 'tesoura',
                 'nuvem', 'banana', 'geladeira', 'camisa', 'passaro', 'floresta', 'colher', 'elefante', 'televisao', 'abacaxi', 'futebol', 'meia', 'girafa',
                 'espelho', 'tigre', 'montanha', 'relogio', 'bolsa', 'filme', 'maca', 'oceano', 'chapeu', 'lapis', 'chave', 'amor', 'borboleta', 'nuvem',
                 'chuveiro', 'morango', 'travesseiro', 'fogo', 'neve', 'unicornio', 'espelho', 'melancia', 'nuvem', 'porta', 'cama', 'vaso', 'dinheiro',
                 'arvore', 'mel', 'aranha', 'tenis', 'barco', 'batata', 'piscina', 'estrela', 'rato', 'pipoca', 'papel', 'coelho', 'planeta', 'colher',
                 'foguete', 'parque', 'suco', 'rosa', 'cachecol', 'escada', 'leao', 'lapis', 'violao', 'pinguim', 'chapeu', 'sol', 'lagrima', 'livro',
                 'telefone', 'cadeado', 'biscoito', 'vela', 'quadro', 'abelha', 'escova', 'fogao', 'espelho', 'balao', 'folha', 'peixe', 'toalha',
                 'caneca', 'borboleta', 'escova', 'guarda-chuva', 'martelo', 'girassol', 'cobertor', 'tijolo', 'abajur', 'xicara', 'cachecol',
                 'chapeu', 'sanduiche', 'lampada', 'aspirador', 'escada', 'relogio', 'pa', 'pato', 'melancia', 'pincel', 'avestruz', 'lenco',
                 'berco', 'vassoura', 'cachorro-quente', 'passaro', 'chapeu', 'pen drive', 'foguete', 'coelho', 'esponja', 'livro', 'guarda-sol',
                 'bolo', 'dinossauro', 'cadeado', 'helicoptero', 'pote', 'caneta', 'colher', 'lagarta', 'quadro', 'bolacha', 'pincel', 'papel',
                 'pinguim', 'cartao', 'pote', 'buzina', 'frigideira', 'tigela', 'unicornio', 'teclado', 'elefante', 'castelo', 'pote', 'mel',
                 'oculos', 'abobora', 'buzina', 'patins', 'fada', 'agua', 'pipa', 'laco', 'colher', 'tapete', 'tigela', 'escorrega', 'mala', 'arco',
                 'rato', 'parafuso', 'carrinho', 'cavalo', 'perola', 'esmeralda', 'chave', 'lapis', 'arco', 'pianista', 'foguetao', 'alfinete',
                 'ima', 'alicate', 'capa', 'estrela', 'video', 'universo', 'bizarro', 'guitarra', 'falando', 'entender']
quickSort(listaPalavras)
print(listaPalavras)

# Polinômio: 6*log n + 86
# Big O: n * log n (melhor caso)
# Big O: n² (pior caso)
