# roberta.grace.main.py"""   
"""     xxxxx

.. codeauthor:: mariaclara < mari4cla@gmail.com >

Changelog
---------
.. versionadded::    
       - xxx
"""


from _spy.vitollino.main import Cena,STYLE



STYLE["width"] = 900 # width = 300 (default)
STYLE["heigth"] = "900px" # min-height = "300px"

FLORESTA= 'https://cptstatic.s3.amazonaws.com/imagens/enviadas/materias/materia24412/floresta-cpt.jpg'
MUNDO= 'https://www.estadosecapitaisdobrasil.com/wp-content/uploads/2015/04/mapa-mundi.png'
ARCO= 'https://static.vecteezy.com/system/resources/previews/000/292/669/non_2x/vector-a-beautiful-rainbow-on-white-background.jpg'
LAPIS= "https://http2.mlstatic.com/adesivo-parede-quarto-infantil-lapis-de-cor-onda-colorida-D_NQ_NP_913239-MLB31144572917_062019-F.jpg"

#arco - cena(ARCO)
#lapis - cena(LAPIS)

#floresta_verde - cena(floresta, direita - mundo, esquerda - arco, meio - lapis) 

def ambiente():
      floresta_verde = Cena(FLORESTA, direita = Cena(MUNDO), esquerda = Cena(ARCO), meio = Cena(LAPIS))
      mundo = Cena(MUNDO, esquerda = floresta_verde) 
      floresta_verde.vai()


ambiente()










