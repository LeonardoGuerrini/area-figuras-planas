class Circulo:

    def circulox():
        while True:
            try:
                print("Área do círculo: A = Pi * r²")
                raio = int(input("Informe o raio do círculo: "))
                print("Resultado:", 3.14 * (raio * raio))

                repetir = input("Você deseja fazer novamente? (sim/nao): ")
                if repetir.lower() == "nao":
                    print("\nObrigado por usar o programa! :)")
                    exit()

            except ValueError:
                print("Erro! O programa aceita apenas números!")
