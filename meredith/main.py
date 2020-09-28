# roberta.meredith.main.py
"""     xxxxx

.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""

"""
Módulo é o arquivo .py que está escrito o códico atual.
atrib_a é o atibuto declarado no módulo atual. 
O valor após a igualdade é atribuição recebida pelo atributo. 
Atribuições que são respectivas de cada tal, para cada atributo.
"""
atrib_a = 10
atrib_b = 3

soma       = atrib_a + atrib_b
subtrai    = atrib_a - atrib_b
multiplica = atrib_a * atrib_b
divide     = atrib_a / atrib_b
potencia   = atrib_a ** atrib_b 
raiz       = atrib_a ** (1/atrib_b)
modulo     = atrib_a % atrib_b #Resto convencional
resto      = atrib_a // atrib_b #Maior divisor sem resto

#print (soma, subtrai, multiplica, divide, potencia, raiz, modulo, resto)

from _spy.vitollino.main import Cena, STYLE
STYLE["width"] = 900
STYLE["heigth"] = "900px"
'''
Caminho_esquerdo = Cena('http://getwallpapers.com/wallpaper/full/e/c/3/175329.jpg')
Caminho_direito  = Cena('https://i.pinimg.com/originals/f1/1a/18/f11a183f87fab48d6ac3024979fa2d9d.jpg')
Caminho_meio     = Cena('https://i.pinimg.com/736x/5f/bc/4b/5fbc4b8429bd52280463d9e5f3bc129d--character-creation-character-ideas.jpg')
Floresta         = Cena('https://i.ytimg.com/vi/dL9_IQv3eGE/maxresdefault.jpg',
                        esquerda=Caminho_esquerdo, direita=Caminho_direito, meio=Caminho_meio)
Floresta.vai()
'''
Img_floresta = 'https://i.ytimg.com/vi/dL9_IQv3eGE/maxresdefault.jpg'
Img_direita  = 'https://i.pinimg.com/originals/f1/1a/18/f11a183f87fab48d6ac3024979fa2d9d.jpg'
Img_esquerda = 'http://getwallpapers.com/wallpaper/full/e/c/3/175329.jpg'
Img_meio     = 'https://i.pinimg.com/736x/5f/bc/4b/5fbc4b8429bd52280463d9e5f3bc129d--character-creation-character-ideas.jpg'

caminho_direito  = Cena(Img_direita)
caminho_esquerdo = Cena(Img_esquerda)
Floresta = Cena(Img_floresta, esquerda=caminho_esquerdo)
caminho_esquerdo.direita = Floresta
caminho_direito.esquerda = Floresta
#Floresta.vai()

Maria_Maia = 4
print('id(Maria_Maia) =', id(Maria_Maia)) # id 140071085578048

Maria_Maia= Maria_Maia + 1
print('id(Maria_Maia_plus_um) =', id(Maria_Maia)) # id 140071085578080
print('id(5) =', id(5)) # id 140071085578080
                   