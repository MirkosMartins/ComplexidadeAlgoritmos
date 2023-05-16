def quicksort(lista):
    if len(lista) <= 1: 
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x < pivo]
        maiores = [x for x in lista[1:] if x >= pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)


palavras = ["uva", "banana", "morango", "campeonato", "campo", "canais", 
"canal", "candidato", "cantor", "cantora", "cantores", "capa", "capacidade",
"cultural", "curitiba", "cursos", "data", "dados", "decreto", "defesa", "demografia", "densidade", 
"departamento", "deputados", "derrota", "descoberta", "desenvolvimento", "desempenho", "determinado",
"diagrama", "dezembro", "escolas", "espanhol",
"esportes", "faculdade", "famoso", "ferramentas", "filosofia", "florestas", "folhas", "fortaleza",
"frase", "frequentemente", "fundador", "futebol", "gabriel", "galeria", "ganhar",
"gelo", "general", "geografia", "global", "governador", "gravadora", "grego", "grupos", "guerra", 
"guitarrista", "habitantes", "homenagem", "hospital", "humanos", "idade",
"jesus", "jogadores", "jornalista", "jovem", "igrejas", "ilha", "imagens", "imprensa", "independente", 
"industrial", "infantaria", "instituto", "inverno", "irlanda", "janeiro", "jardim", "jesus",
"julho", "juventude", "lago", "leis", "liberdade", "locais", "lugares", "machado", "medalhas", "militares", 
"modelos", "mulheres", "nacional", "natureza", "necessidade",
"nenhum", "nomeado", "nordeste", "noticia", "novembro", "objetivo", "oceano", "oficialmente", "online",
"origem", "ouro", "orquestra", "outubro", "padre", 
"pais", "palavras", "papel", "parceria", "parlamento", "pedidos", "performance", "personagens", "pesquisas",
"piloto", "planeta", "poderes", "possibilidade", "praia", "prazo", "prefeitura", "primeira", "problemas", 
"produtor", "professores", "projetos", "provas", "publicado", "quadrinhos", "qualidade", "quem", "quinta", "rainha",
"realidade", "recentemente", "regional", "rios", "romance", "rural", "saber", "samba", "segundos", "sinal", "sociais",
"soldados", "suficiente", "tabela", "teatro", "tempos", "tinha", "torneio", "times", "torres", "trabalhar",
"transporte", "treinador", "tribunal", "troca", "turismo", "turno", "unidade", "universidade", "uruguai", "utilizada",
"vale", "velho", "viagem", "viver", "vandalismo", "verdadeiro", "vocalista", "volume", "walter", "website",
"chamada", "chefe", "chicago", "chile", "cidade", "civil", "clubes", "colocar", "comando", "companhia", "compositor",
"computador", "concurso", "conflito", "conhecer", "conquistou", "consiste", "construir", "contexto", "coreia", "zafari",  "zero"]  

palavras_ordenadas = quicksort(palavras)
print(palavras_ordenadas)


