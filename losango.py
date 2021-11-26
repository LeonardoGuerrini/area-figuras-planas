class Losango:

    def losangox():
        while True:
            try:

                print("Área do losângo: A =  D * d / 2")

                diagmaior = int(input("Informe o valor da diagonal maior: "))
                diagmenor = int(input("Informe o valor da diagonal menor: "))
                print("Resultado:", (diagmaior * diagmenor) / 2)

                print("")

                print(f"Operação:\nA = D * d / 2\nA = {diagmaior} * {diagmenor} / 2\nA =",(diagmaior*diagmenor) / 2)

                repetir = str(input("Você deseja fazer novamente? (sim/nao): "))
                if repetir.lower() == "nao":
                    print("\nObrigado por usar o programa! :)")
                    
                    break

            except:
                print("\nErro!")
