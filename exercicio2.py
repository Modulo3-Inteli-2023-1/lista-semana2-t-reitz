#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def is_anagram(word1, word2):
    letters1 = list(word1)
    letters2 = list(word2)

    if sorted(letters1) == sorted(letters2):
        return True
    else:
        return False


# Teste a sua função aqui (caso ache necessário)


a = is_anagram("pedra", "padre")
print(a)







