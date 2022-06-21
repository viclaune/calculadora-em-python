print("********** Calculadora Python **********")
print("Selecione o número da operação desejada:")
print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

escolha = int(input("Digite sua opção (1/2/3/4):"))

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

soma = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y

if escolha == 1:
    print(primeiro_numero, "+", segundo_numero, ' = ', soma(primeiro_numero, segundo_numero))
elif escolha == 2:
    print(primeiro_numero, "-", segundo_numero, ' = ', subtracao(primeiro_numero, segundo_numero))
elif escolha == 3:
    print(primeiro_numero, "*", segundo_numero, ' = ', multiplicacao(primeiro_numero, segundo_numero))
elif escolha == 4:
    print(primeiro_numero, "/", segundo_numero, ' = ', divisao(primeiro_numero, segundo_numero))
else:
    print("Escolha fora do range")