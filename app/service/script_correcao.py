import requests

url = "https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt"
resposta = requests.get(url)

letras_adjacentes = {
    "q": ["w", "a"],
    "w": ["q", "e", "a", "s"],
    "e": ["w", "r", "s", "d"],
    "r": ["e", "t", "d", "f"],
    "t": ["r", "y", "f", "g"],
    "y": ["t", "u", "g", "h"],
    "u": ["y", "i", "h", "j"],
    "i": ["u", "o", "j", "k"],
    "o": ["i", "p", "k", "l"],
    "p": ["o", "l"],

    "a": ["q", "w", "s", "z"],
    "s": ["a", "w", "e", "d", "z", "x"],
    "d": ["s", "e", "r", "f", "x", "c"],
    "f": ["d", "r", "t", "g", "c", "v"],
    "g": ["f", "t", "y", "h", "v", "b"],
    "h": ["g", "y", "u", "j", "b", "n"],
    "j": ["h", "u", "i", "k", "n", "m"],
    "k": ["j", "i", "o", "l", "m"],
    "l": ["k", "o", "p"],

    "z": ["a", "s", "x"],
    "x": ["z", "s", "d", "c"],
    "c": ["x", "d", "f", "v"],
    "v": ["c", "f", "g", "b"],
    "b": ["v", "g", "h", "n"],
    "n": ["b", "h", "j", "m"],
    "m": ["n", "j", "k"]
}

palavra = str(input("digite sua palavra: "))
dicionario = [i for i in resposta.text.splitlines()]

def errou_tecla_adjacente(palavra_digitada, dicionario, letras_adjacentes):
    palavras_semelhantes = [i for i in dicionario if len(i) == len(palavra_digitada)]
    possiveis = {}
    contador_alteracoes = 0
    digitada_original = list(palavra_digitada)

    for palavra in palavras_semelhantes: #percorre as palavras semelhantes usando a variavel palavra
        caracter = 0 
        digitada = digitada_original #transforma a palavra digitada em lista de caracteres
        contador_alteracoes = 0

        for letra in digitada: #percorre os caracteres da palavra digitada
            if letra == palavra[caracter]: 
                caracter += 1 #compara o caracter atual com o caracter da possivel palavra atual e se for igual pula pro proximo
            elif palavra[caracter] in letras_adjacentes[letra]:
                digitada[caracter] = palavra[caracter] #se for diferente mas estiver nas teclas proximas ele troca e pula para o proximo
                caracter += 1                  
                contador_alteracoes += 1 #conta quantas alteracoes foram feitas

        if "".join(digitada) == palavra: #apos comparar cada caracter ele verifica se formou uma palavra igual transforma em string e add na lista de possiveis
            possiveis["".join(digitada)] = contador_alteracoes
        
    return possiveis

def letra_mais(dicionario, palavra_digitada):
    palavras_semelhantes = [i for i in dicionario if len(i) == len(palavra_digitada) - 1]
    possiveis = []
    digitada = list(palavra_digitada)

    for letra in digitada:
        digitada = list(palavra_digitada)
        digitada.remove(letra)

        if "".join(digitada) in palavras_semelhantes:
            possiveis.append("".join(digitada))
            
    return possiveis

def lista_total(adjacentes, letras_extras):
    lista_total = {}
    lista_total["erro de letras adjacentes"] = adjacentes    
    lista_total["erro de letras a mais"] = letras_extras
 
    return lista_total

erros_adjacentes = errou_tecla_adjacente(palavra, dicionario, letras_adjacentes)
erros_letras_extras = letra_mais(dicionario, palavra)
lista_final = lista_total(erros_adjacentes, erros_letras_extras)

print(lista_final)


# -----LEMBRETE-----
#analisar todo o algoritmo desse codigo
#deixar mais legivel
#terminar a lista_total
#deixar-lo aplicavel para importar em outros codigos






















