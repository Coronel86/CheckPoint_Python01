secreto = 10
palpite = 0
tentativas = 0
limite = 7

while True:
    palpite = int(input("Digite o seu palpite do número ' 1 até 100 ' : "))
    tentativas += 1

    if palpite == secreto:
        print(f"Parabéns! Você acertou número: {secreto}. Após: {tentativas} tentativas")
        break
    
    elif tentativas >= limite:
        print(f"Você errou! Atingiu o limite de '7' tentativas.")
        break

    elif palpite < secreto:
        print("Você errou! Dica: O número secreto é MAIOR.")
    else:
        print("Você errou! Dica: O número secreto é MENOR.")

    continue