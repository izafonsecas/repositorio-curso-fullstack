print("Acerte o número misterioso com o mínimo de tentativas!")
print()

numero = 2
tentativas = 0

chute = int(input("Digite um número: "))
tentativas += 1

while chute != numero:
    print("Errou! Tente novamente.")
    chute = int(input("Digite o número: "))
    tentativas += 1

print()
print("Parabéns! Você acertou!")
print(f"O número secreto era {numero}.")
print(f"Você precisou de {tentativas} tentativas para acertar.")