class Quadrado:

    def quadradox():
        while True:
            try:

                print("Área do quadrado: A = L²")

                lado = int(input("Informe o lado do quadrado: "))
                print("\nResultado:", lado * lado) # Resultado
                    
                print("")

                print(f"Operação:\nA = L²\nA = {lado}²\nA = {lado}*{lado}\nA =",lado*lado)

                repetir = str(input("\nVocê deseja fazer novamente? (sim/nao): "))
                if repetir.lower() == "nao":
                    print("\nObrigado por usar o programa! :)")

                    break

            except:
                print("\nErro!")
