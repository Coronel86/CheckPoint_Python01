secreto = 2
palpite = 0

while True:
    palpite != secreto:
    palpite = int(input("Digite o seu palpite: "))

    if palpite != secreto:
        print("Você errou! Tente novamente.")

        break
      
    soma = soma + palpite

    print(f"Tentativas"{soma}"Parabéns! Você acertou.")