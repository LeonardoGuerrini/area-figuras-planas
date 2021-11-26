class Circulo:

    def circulox():
        while True:
            try:

                print("Área do círculo: A = Pi * r²")

                pi = 3.14
                raio = int(input("Informe o valor do raio: "))
                print("Resultado:", pi * (raio * raio))

                print("")

                print(f"Operação:\nA = Pi * r²\nA = {pi} * {raio}²\nA =", pi * (raio * raio))

                repetir = str(input("Você deseja repetir? (sim/nao): "))
                if repetir.lower() == "nao":
                    print("\nObrigado por usar o programa! :)")

                    break

            except:
                print("\nErro!")
