from circulo import Circulo
from losango import Losango
from quadrado import Quadrado
from retangulo import Retangulo
from trapezio import Trapezio
from triangulo import Triangulo


class Opcoes:

    def opcoesx():
        while True:
            try:
                escolha = input('''
**************************

[ c ] Calcular área
[ s ] Sair do programa

**************************
                
[Sua resposta]: ''')

                if escolha.lower() == "s":
                    print("\nObrigado por usar o programa! :)")

                    break
                
                elif escolha.lower() == "c":
                    area = input('''\n\n

************************************************

Escolha a figura que deseja calcular a área:

[ q ] Quadrado
[ r ] Retângulo
[ t ] Triângulo
[ l ] Losângo
[ z ] Trapézio
[ c ] Círculo

************************************************

[Sua resposta]: ''')

                    if area.lower() == "q":
                        Quadrado.quadradox()
                    
                    elif area.lower() == "r":
                        Retangulo.retangulox()

                    elif area.lower() == "t":
                        Triangulo.triangulox()
                    
                    elif area.lower() == "l":
                        Losango.losangox()

                    elif area.lower() == "z":
                        Trapezio.trapeziox()

                    elif area.lower() == "c":
                        Circulo.circulox()

            except:
                print("\nErro!")
