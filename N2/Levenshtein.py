def levenshtein(a, b, print_matrix=False, lowercase=True):
    # Lida com exceções
    if not isinstance(a, str):
        raise TypeError('First argument is not a string!')
    if not isinstance(b, str):
        raise TypeError('Second argument is not a string!')

    # Se uma das strings for vazia, a distância é o tamanho da outra
    if a == '':
        return len(b)
    if b == '':
        return len(a)
    #Maneira de ignorar diferenças de lower/upper case
    if lowercase:
        a = a.lower()
        b = b.lower()

    n = len(a)
    m = len(b)

    # Cria matriz com zeros
    lev = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Inicializa as bordas
    for i in range(n + 1):
        lev[i][0] = i
    for j in range(m + 1):
        lev[0][j] = j

    # Preenche a matriz
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = lev[i - 1][j] + 1
            deletion = lev[i][j - 1] + 1
            substitution = lev[i - 1][j - 1] + (1 if a[i - 1] != b[j - 1] else 0)
            lev[i][j] = min(insertion, deletion, substitution)

    #Opção para imprimir a matriz
    if print_matrix:
        for linha in lev:
            print(linha)

    # Retorna a distância 
    return lev[n][m]

def correcoes(palavra, dicionario, limite=2):
    sugestoes = []
    for termo in dicionario.values(): # itera pelos valores
        dist = levenshtein(palavra, termo)
        if dist <= limite:
            sugestoes.append((termo, dist)) #cria tupla com palavra distância

    sugestoes.sort(key=lambda x: x[1])  # ordena por menor distância
    return [s[0] for s in sugestoes]    # retorna só as palavras

dicionario = {
    1: "ebulição",
    2: "ebúrnea",
    3: "ebúrneas",
    4: "ebúrneo",
    5: "ebúrneos",
    6: "eclesiástica",
    7: "eclesiásticas",
    8: "eclesiástico",
    9: "eclesiásticos",
    10: "eclética",
    11: "ecléticas",
    12: "eclético",
    13: "ecléticos",
    14: "ecletismo",
    15: "ecletismos",
    16: "eclipsa",
    17: "eclipsá",
    18: "eclipsado",
    19: "eclipsai",
    20: "eclipsais",
    21: "eclipsam",
    22: "eclipsamo",
    23: "eclipsamos",
    24: "eclipsando",
    25: "eclipsar",
    26: "eclipsara",
    27: "eclipsará",
    28: "eclipsaram",
    29: "eclipsáramos",
    30: "eclipsarão",
    31: "eclipsaras",
    32: "eclipsarás",
    33: "eclipsardes",
    34: "eclipsarei",
    35: "eclipsareis",
    36: "eclipsáreis",
    37: "eclipsarem",
    38: "eclipsaremo",
    39: "eclipsaremos",
    40: "eclipsares",
    41: "eclipsaria",
    42: "eclipsariam",
    43: "eclipsaríamos",
    44: "eclipsarias",
    45: "eclipsaríeis",
    46: "eclipsarmo",
    47: "eclipsarmos",
    48: "eclipsas",
    49: "eclipsasse",
    50: "eclipsásseis"
}

#Aplicação simples
while True:
    opcao = input("Menu\n1-Corretor ortográfico\n2-Fim do programa\nOpção: ")
    if opcao == "1":
        palavra = input("Insira palavra: ")
        sugestoes = correcoes(palavra, dicionario)
        print("Sugestões de palavras próximas:", sugestoes)
    elif opcao == "2":
        print("Fim do programa!")
        break
    else:
        print("Opção inválida!")

	
	
