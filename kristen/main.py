# roberta.kristen.main.py
"""     xxxxx

.. codeauthor:: Lilian <lilianes93@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""

from _spy.vitollino.main import Cena, STYLE

STYLE ["width"] = 1000
STYLE ["height"] = 1000

FLORESTA = "https://image.freepik.com/vetores-gratis/folhagem-de-floresta-tropical-paisagem_23-2148271243.jpg"
BORBOLETA = "https://store-images.s-microsoft.com/image/apps.2544.13768621950225582.167ba0c8-6eb8-47bb-96fe-278c89bf0dc9.ea440c13-fd1d-4705-b62c-9bfd9054b8b3?w=672&h=378&q=80&mode=letterbox&background=%23FFE4E4E4&format=jpg"
INDIO = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fbr.pinterest.com%2Fpin%2F725712927435250494%2F&psig=AOvVaw0D47WV7tiAY8ct2rEipO5n&ust=1600214923381000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPCd-qPv6esCFQAAAAAdAAAAABAD.jpg"
OCA = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.gratispng.com%2Fpng-4qxfp4%2F&psig=AOvVaw2F3RhnMhNl96R10vfCtcxs&ust=1600214952070000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDivLDv6esCFQAAAAAdAAAAABAD.png"

nome_da_cena_meio = Cena(INDIO)
nome_da_cena_direita = Cena(BORBOLETA)
nome_da_cena_esquerda = Cena(OCA)
nome_da_cena = Cena(INDIO, esquerda=nome_da_cena_esquerda, direita=nome_da_cena_direita, meio=nome_da_cena_meio)
                 
nome_da_cena.vai()