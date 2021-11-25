class Quadrado:

    def quadradox():
        while True:
            try:
                print("Área do quadrado: A = L²")
                lado = int(input("Informe o lado do quadrado: "))
                print("Resultado:", lado * lado)

                repetir = input("Você deseja fazer novamente? (sim/nao): ")
                if repetir.lower() == "nao":
                    print("\nObrigado por usar o programa! :)")
                    exit()

            except ValueError:
                print("Erro! O programa aceita apenas números!")
