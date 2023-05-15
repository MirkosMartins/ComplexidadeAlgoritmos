def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

'''
***** Atividade QuickSort *****
- Crie uma lista com 200 palavras (em português)
- Ordene a lista usando QuickSort (tem que ser um método/função separada)
- Calcule o polinômio característico dos métodos/funções
- Defina o Big O do programa COMPLETO
'''

#TODO: colocar 200 palavras diferentes em português na lista, não pode acentos
alist = ['facil', 'cume', 'casa', 'novo', 'fogo', 'perto', 'mulher', 'ruim', 'cor', 'passar', 'amargo', 'carro', 'bom', 
'lindo', 'sol', 'colina', 'grande', 'obra', 'calma', 'tarde', 'jogar', 'negro', 'certo', 'doido', 'dar', 'dor', 'burro', 
'correr', 'sala', 'chefe', 'gente', 'comedia', 'longe', 'hora', 'boca', 'parar', 'homem', 'chocolate', 'raro', 'medo', 
'curva', 'pouco', 'abaixo', 'frio', 'doce', 'ser', 'calmado', 'nada', 'feliz', 'passado', 'criar']
quickSort(alist)
print(alist)