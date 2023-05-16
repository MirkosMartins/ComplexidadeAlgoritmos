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

alist = ['intermodalismo', 'azoinar', 'tostão', 'nitro', 'inflorescência', 'comprazimento', 'tentativa', 'amoestar', 'poesia', 'conta', 'supletivo', 'avante', 'vestidura', 'arbitragem', 'fouce', 'hizo',
         'borgonhês', 'presumptivo', 'reabastecedor', 'equilibrar', 'dolosamente', 'liberador', 'reviramento', 'alambique', 'acredital', 'obstrução', 'embarcação', 'decodificador', 'aglutininas', 'pessoas', 'pineal',
         'glicosúria', 'remailer', 'bairrista', 'monstrozinho', 'desnaturado', 'disselhe', 'tri-campeã', 'disserão', 'loudel', 'iletrado', 'motociclístico', 'orçar', 'degenerativo', 'observancia', 'geoestacionário',
         'preferencia', 'cambialmente', 'unido', 'inositadamente', 'caos', 'constringir', 'jambu', 'núcelo', 'telejogo', 'corpora', 'telégrafo', 'endoscópio', 'vestibular', 'ilusório', 'vinil', 'micropartido', 
         'hip-hop','grandiloquência', 'desmineralização', 'ex-executivo', 'tolamente', 'supposto', 'autocrático', 'faltar', 'crocitar', 'autotanque', 'momentaneamente', 'argentar', 'eurocepticismo', 'morrão', 
         'perfuração','peleguismo', 'inflacionário', 'ilustradora', 'extra-muro', 'institucionalidade', 'demissionismo', 'repentista', 'sulfureto', 'detento', 'enfolhado', 'ro-ro', 'vacum', 'detalhista', 
         'maritimista', 'cel','não-realizar', 'windsurfista', 'tesourada', 'exemplificativamente', 'exógeno', 'atte', 'estremadamente', 'escurecer','peneira', 'ex-arcebispo', 'wizard', 'sanctorum', 'alevita',
         'médico-paciente', 'intrometter','escovar', 'beco', 'digitalmente', 'rectroescavadora', 'am', 'isótopo', 'tamanca', 'apertado', 'óio', 'tresdobrar', 'domesticar', 'diminuir', 'vilão', 'farricoco',
         'avantesma', 'afásico', 'anti-semita','entrae', 'garfo', 'pregado', 'louquinho', 'ensolarado', 'ferocidade', 'top-model', 'vacatio', 'céptico', 'repovoamento', 'auto-dissolver', 'bugiganga', 'percorrer',
         'should', 'prendeo', 'universitaria', 'colorido','transfuga', 'rótulo', 'argumentativamente', 'ciganada','esfalfamento', 'promettar', 'escampar', 'inverídico', 'enlace', 'apr', 'qual', 'além-mar', 
         'bestinha', 'aliciador', 'limoeiro', 'conversão','quiosque', 'malferido', 'grenho', 'bulhão', 'lastrear', 'touchdown', 'sintrense', 'corniaberto', 'hhh', 'acometimento', 'grã-fino', 'espumante',
         'louuor', 'sur', 'franchisado', 'fraco', 'nebrino','sacho', 'chaque', 'torc', 'brotar', 'público','cedilha', 'subholding', 'terceiro-oficial', 'mourisco', 'dramatículo', 'vale', 'maviosamente', 
         'monotonamente', 'moquear', 'queimar', 'enunciado','desmultiplicar', 'desfalecidamente', 'internacionalista', 'certezinha', 'não-associar', 'monotorização', 'ajoelhado', 'mingar', 'tetraneto', 'propria']
quickSort(alist)
print(alist)