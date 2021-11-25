from circulo import Circulo
from quadrado import Quadrado
from retangulo import Retangulo
from losango import Losango

class Opcoes:

    def opcoesx():
        while True:
            try:
                print("[1] Quadrado\n[2] Retângulo\n[3] Losângo\n[4] Círculo\n")
                escolha = int(input("Insira sua escolha (1/2/3/4): "))
                if escolha == 1:
                    Quadrado.quadradox()
                
                elif escolha == 2:
                    Retangulo.retangulox()

                elif escolha == 3:
                    Losango.losangox()

                elif escolha == 4:
                    Circulo.circulox()

            except ValueError:
                print("Erro! O programa aceita apenas números!")
