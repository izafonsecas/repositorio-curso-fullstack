print("🔮ORÁCULO DA SABEDORIA PYTHON🔮")
print("Pergunte sobre um tema de programação e eu tentarei te ajudar ✨")
print()

tema = input("Digite um assunto (ou uma pergunta curta): ").lower()

match tema:
    case "variáveis" | "variavel" | "variáveis em python":
        print("📦 Variáveis são 'caixinhas com nome' onde você guarda valores.")
        print("Ex.: idade = 18  |  nome = 'Iza'  |  nota = 9.5")

    case "if" | "condicional" | "se" | "if else":
        print("🧠 IF/ELSE serve para tomar decisões.")
        print("Ex.: se idade >= 18, então pode dirigir; senão, não pode.")

    case "python":
        print("Python é uma linguagem ótima para começar: simples, poderosa e versátil.")
        print("Dá pra fazer automações, web, dados, scripts e muito mais.")

    case _:
        print("🤔 Ainda estou aprendendo esse tema...")
        print("Mas posso tentar te ajudar se você explicar melhor ou der um exemplo!")
        print("📌 Dica: tente temas como 'variáveis', 'if', 'loops', 'listas' ou 'funções'.")