class Losango:

    def losangox():
        while True:
            try:
                print("Área do losango: A = (D+d) / 2")
                diagmaior = int(input("Informe a diagonal maior: "))
                diagmenor = int(input("Informe a diagonal menor: "))
                print("Resultado: ", (diagmaior * diagmenor) / 2)

                repetir = input("Você deseja fazer novamente? (sim/nao): ")
                if repetir.lower() == "nao":
                    print("\nObrigado por usar o programa! :)")
                    exit()

            except ValueError:
                print("Erro! O programa aceita apenas números!")
