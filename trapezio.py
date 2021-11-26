class Trapezio:

    def trapeziox():
        while True:
            try:

                print("Área do trapézio: (B + b) * h / 2")

                basemaior = int(input("Informe o valor da base maior: "))
                basemenor = int(input("Informe o valor da base menor: "))
                altura = int(input("Informe o valor da altura: "))
                print("Resultado:", ((basemaior + basemenor) * altura) / 2)

                print("")

                print(f"Operação:\nA = (B + b) * h / 2\nA = ({basemaior} + {basemenor}) * {altura} / 2\nA =", ((
                    basemaior+basemenor) * altura) / 2)

                if str(input("Deseja continuar (sim/nao):")).lower() in ['s', 'sim']:
                    print("\nContinuando...\n")

                else:
                    print("Obrigado por usar o programa! :)")

                    break

            except:
                print("\nErro!")
