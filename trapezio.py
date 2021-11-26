class Trapezio:

    def trapeziox():
        while True:
            try:
                
                print("Área do trapézio: (B + b) * h / 2")

                basemaior = int(input("Informe o valor da base maior: "))
                basemenor = int(input("Informe o valor da base menor: "))
                altura = int(input("Informe o valor da altura: "))
                print("Resultado:", ((basemaior + basemenor) * altura) / 2)

                print("")

                print(f"Operação:\nA = (B + b) * h / 2\nA = ({basemaior} + {basemenor}) * {altura} / 2\nA =", ((basemaior+basemenor) * altura) / 2)

                repetir = str(input("Você deseja fazer novamente? (sim/nao): "))
                if repetir.lower() == "nao":
                    print("\nObrigado por usar o programa! :)")

                    break

            except:
                print("\nErro!")
