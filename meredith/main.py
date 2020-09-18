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
Floresta = Cena('https://i.ytimg.com/vi/dL9_IQv3eGE/maxresdefault.jpg',
                esquerda='http://getwallpapers.com/wallpaper/full/e/c/3/175329.jpg', # default = NADA = SalaCenaNula()
                direita='https://i.pinimg.com/originals/f1/1a/18/f11a183f87fab48d6ac3024979fa2d9d.jpg',  # default = NADA = SalaCenaNula()
                meio='https://i.pinimg.com/736x/5f/bc/4b/5fbc4b8429bd52280463d9e5f3bc129d--character-creation-character-ideas.jpg')
Floresta.vai()
