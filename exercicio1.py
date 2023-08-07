#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def conta_palavras_unicas(string):
    unique_words = []
    words = string.split(" ")
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    
    return len(unique_words)



# Teste a sua função aqui (caso ache necessário)

a = conta_palavras_unicas("a b c d e f g h i")
print(a)







