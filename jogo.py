import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "desenvolvimento", "jogo", "teste", "tentativas", "Leandro"]
    return random.choice(palavras)

def mostrar_forca(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

def jogar():
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    mostrar_forca(palavra, letras_corretas)
    
    while tentativas > 0:
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if letra in palavra:
            letras_corretas.append(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            print("Letra errada! Você tem {} tentativas restantes.".format(tentativas))
        
        mostrar_forca(palavra, letras_corretas)
        
        if all(letra in letras_corretas for letra in palavra):
            print("Parabéns! Você ganhou!")
            break
    
    if tentativas == 0:
        print("Suas tentativas acabaram. A palavra era:", palavra)

if __name__ == "__main__":
    jogar()