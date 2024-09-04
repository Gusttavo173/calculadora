def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y if y != 0 else "Erro! Divisão por zero."

def modulo(x, y):
    return x % y if y != 0 else "Erro! Divisão por zero."

def exponenciacao(x, y):
    return x ** y

def sair():
    print("Saindo da calculadora...")
    return None

operacoes = {
    '1': soma,
    '2': subtracao,
    '3': multiplicacao,
    '4': divisao,
    '5': modulo,
    '6': exponenciacao,
    '7': sair
}

def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Módulo (resto)")
        print("6 - Exponenciação")
        print("7 - Sair")
        escolha = input("Digite o número da operação: ")
        if escolha == '7':
            operacoes[escolha]()
            break
        if escolha in operacoes:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = operacoes[escolha](num1, num2)
            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida. Tente novamente.")

calculadora()
