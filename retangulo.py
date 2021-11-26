class Retangulo:
    
    def retangulox():
        while True:
            try:
                
                print("Área do retângulo: A = b * h")

                base = int(input("Informe o valor da base: "))
                altura = int(input("Informe o valor da altura: "))
                print("\nResultado:", base * altura) # resultado

                print("")

                print(f"Operação:\nA = b * h\nA = {base} * {altura}\nA =",base*altura)

                repetir = str(input("\nVocê deseja fazer novamente? (sim/nao): "))
                if repetir.lower() == "nao":
                    print("\nObrigado por usar o programa! :)")

                    break

            except:
                print("\nErro!")
