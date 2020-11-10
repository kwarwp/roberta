# roberta.parisa.main.py
from _spy.vitollino.main import Cena, INVENTARIO as inv 

IMG_1 = "https://www.searchpng.com/wp-content/uploads/2019/01/Tiger-PNG-1024x1024.png"
IMG_2 = "https://i.imgur.com/GleAY3f.jpeg"
IMG_3 = 'https://i.imgur.com/4oUluVP.jpeg'

def pontua():
    inv.score(casa=1, carta=2, move=3, ponto=4, valor=5, _level=1)
    
cena_pontos = Cena(vai=pontua)

cena_dois = Cena(img = IMG_2, esquerda=cena_pontos, xy=(0, 0))
cena_tres = Cena(img = IMG_3, xy=(0, 0))

cena_um = Cena(img = IMG_1, esquerda=cena_dois,direita=cena_tres,nome="Tigre",
               score=dict(ponto=0, valor=0, carta=None, casa=None, move=None))
       
           #(self, casa, carta, move, ponto, valor, _level=1):
inv.inicia()             
cena_um.vai()
