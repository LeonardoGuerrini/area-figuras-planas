class Retangulo:

    def retangulox():
        while True:
            try:
                print("Área do retângulo: A = b * h")
                base = int(input("Informe o valor da base: "))
                altura = int(input("Informe o valor da altura: "))
                print("Resultado:", base * altura)

                repetir = input("Você deseja fazer novamente? (sim/nao): ")
                if repetir.lower() == "nao":
                    print("\nObrigado por usar o programa! :)")
                    exit()
                    
            except ValueError:
                print("Erro! O Programa aceita apenas números!")
