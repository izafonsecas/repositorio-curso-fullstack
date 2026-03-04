print("Quiz divertido para passar o tempo!✒️")
print("Responda as 4 perguntas e tente chegar na pontuação máxima")
print()

perguntas = [
    ["Qual é a linguagem que estamos estudando?", "python"],
    ["Qual comando imprime algo na tela?", "print"],
    ["Como se chama a estrutura de decisão 'se/senão' em Python?", "if"],
    ["Qual comando é usado para ler algo digitado pelo usuário?", "input"]
]

acertos = 0

for pergunta in perguntas:
    resposta_usuario = input(pergunta[0] + " ").lower()
    resposta_correta = pergunta[1].lower()

    if resposta_usuario == resposta_correta:
        print("Acertou!\n")
        acertos += 1
    else:
        print(f"Errou! A resposta certa era: {resposta_correta}\n")

print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")