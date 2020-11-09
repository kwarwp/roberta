# roberta.parisa.main.py
from _spy.vitollino.main import Cena, Inventario as inv 

IMG_1 = "https://www.searchpng.com/wp-content/uploads/2019/01/Tiger-PNG-1024x1024.png"
IMG_2 = "https://i.imgur.com/GleAY3f.jpeg"
IMG_3 = 'https://i.imgur.com/4oUluVP.jpeg'

cena_dois = Cena(img = IMG_2, xy=(0, 0))
cena_tres = Cena(img = IMG_3, xy=(0, 0))
cena_um = Cena(img = IMG_1, esquerda=cena_dois,direita=cena_tres,nome="Tigre",
               score=dict(ponto=0, valor=0, carta=None, casa=None, move=None))

          #(self, img=IMAGEM, esquerda=NADA, direita=NADA, meio=NADA,
              #vai=None, nome='', xy=(0, 0), score=NOSC, **kwargs)
inv.inicia()             
cena_um.vai()
