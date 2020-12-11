
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

Imagem_Biblioteca_porta="https://media.istockphoto.com/vectors/closed-door-drawing-vector-id865663698"
Imagem_Biblioteca_porta2="https://image.freepik.com/vetores-gratis/porta-aberta-dos-desenhos-animados-entrada-do-corredor-do-apartamento-entrada-do-escritorio_53562-8532.jpg"
Imagem_Biblioteca_dentro="https://secult.es.gov.br/Media/secult/BPES/IMG_7650.JPG"

STYLE["width"] = 500 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

Biblioteca_entrada=Cena(Imagem_Biblioteca_porta)
Biblioteca_entrada.vai()

Biblioteca_porta=Cena(Imagem_Biblioteca_porta2)

Biblioteca_dentro=Cena(Imagem_Biblioteca_dentro)

Imagem_botao="https://images-na.ssl-images-amazon.com/images/I/71nQDXqkyDL.png"

def desafio_porta1 (event = None):
    Biblioteca_porta.vai()
    
BOTAO= Elemento(Imagem_botao, tit="click",w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                cena = Biblioteca_entrada)
                                
BOTAO.elt.bind("click", desafio_porta1)

def desafio_porta2 (event = None):
    Biblioteca_dentro.vai()
    
BOTAO2= Elemento(Imagem_botao, tit="click",w=30,h=36,  x=450, y=300, # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                cena = Biblioteca_porta2)
                                
BOTAO.elt.bind("click", desafio2_porta2)



