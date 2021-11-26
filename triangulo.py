class Triangulo:

    def triangulox():
        while True:
            try:

                print("Área do triângulo: A = b * h / 2")

                base = int(input("Informe o valor da base: "))
                altura = int(input("Informe o valor da altura: "))
                print("\nResultado:", (base * altura) / 2)  # Resultado

                print("")

                print(
                    f"Operação:\nA = b * h / 2\nA = {base} * {altura} / 2\nA =", (base*altura) / 2)

                if str(input("Deseja continuar (sim/nao):")).lower() in ['s', 'sim']:
                    print("\nContinuando...\n")

                else:
                    print("Obrigado por usar o programa! :)")

                    break

            except:
                print("\nErro!")
