# Essa função retorna uma lista com os items ordenados em ordem crescente e/ou alfabética
# A função recebe apenas dados de tipo 'int', 'float' ou 'str.
# A função retorna uma string quando ocorre um erro, se não, reotna-se uma lista, como resultado

# tem uma forma melhor de saber se um dado é de um determinado tipo ou não?????


def ordenar(valores):
    """Recebe uma lista ordena essa lista e retorna a lista ordenada"""
    if not type(valores) == type([]):
        return "ERRO: O tipo de dado não é uma lista"

    elif len(valores) < 1:
        return "ERRO: Elementos insuficiêntes"

    elif len(valores) == 1:
        return valores

    else:
        for a in range(0, len(valores)):
            # Primeiro, verifica-se se todos os valores passados como parametros são de tipo 'int', 'float' e/ou 'str', se não, retorna-se um erro
            if type(valores[a]) != type(0) and type(valores[a]) != type("str") and type(valores[a]) != type(0.0):
                return f"ERRO: Apenas dados de tipo 'int', 'float' ou 'str' são aceitos, não {type(valores[a])}"
                break
    
        # Agora, vamos ordenar os valores...
        for a in range(0, len(valores)):
            for b in range(0, len(valores)-1):

                # Se o valor 'a' for uma string e o valor 'b' for diferente de uma string, quando tentarmos comparar se 'a' é maior que 'b', vamos obter um erro.
                # Por isso, devemos verificar se estamos comparando 'str' com 'str e 'int'/'float com 'int'/'float'

                if type(valores[b]) == type("str") and type(valores[b+1]) == type("str"):
                    if valores[b] > valores[b+1]:
                        valores[b], valores[b+1] = valores[b+1], valores[b]

                elif type(valores[b]) == type("str") or type(valores[b+1]) == type("str"): # ESTÁ DANDO FALSO QUANDO EU ESPERAVA POR VERDADEIRO (NÃO SEI POR QUE)
                    if type(valores[b]) == type("str"):
                        valores[b], valores[b+1] = valores[b+1], valores[b]

                elif valores[b] > valores[b+1]:
                    valores[b], valores[b+1] = valores[b+1], valores[b]
        
        return valores


print(ordenar(["k", "ds", "Python", "WWW", 345345, 2342, 543, 67.2, 64, 0, 2.3]))
