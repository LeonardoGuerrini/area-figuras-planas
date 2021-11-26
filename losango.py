class Losango:

    def losangox():
        while True:
            try:

                print("Área do losângo: A =  D * d / 2")

                diagmaior = int(input("Informe o valor da diagonal maior: "))
                diagmenor = int(input("Informe o valor da diagonal menor: "))
                print("Resultado:", (diagmaior * diagmenor) / 2)

                print("")

                print(
                    f"Operação:\nA = D * d / 2\nA = {diagmaior} * {diagmenor} / 2\nA =", (diagmaior*diagmenor) / 2)

                if str(input("Deseja continuar (sim/nao):")).lower() in ['s', 'sim']:
                    print("\nContinuando...\n")

                else:
                    print("Obrigado por usar o programa! :)")

                    break

            except:
                print("\nErro!")
