class Circulo:

    def circulox():
        while True:
            try:

                print("Área do círculo: A = Pi * r²")

                pi = 3.14
                raio = int(input("Informe o valor do raio: "))
                print("Resultado:", pi * (raio * raio))

                print("")

                print(
                    f"Operação:\nA = Pi * r²\nA = {pi} * {raio}²\nA =", pi * (raio * raio))

                if str(input("Deseja continuar (sim/nao):")).lower() in ['s', 'sim']:
                    print("\nContinuando...\n")

                else:
                    print("Obrigado por usar o programa! :)")

                    break

            except:
                print("\nErro!")
