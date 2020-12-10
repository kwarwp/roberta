
from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

Imagem_Biblioteca_porta="https://media.istockphoto.com/vectors/closed-door-drawing-vector-id865663698"
Imagem_Biblioteca_porta2="https://image.freepik.com/vetores-gratis/porta-aberta-dos-desenhos-animados-entrada-do-corredor-do-apartamento-entrada-do-escritorio_53562-8532.jpg"
Imagem_Biblioteca_dentro="https://secult.es.gov.br/Media/secult/BPES/IMG_7650.JPG"

STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

Biblioteca_entrada=Cena(Imagem_Biblioteca_porta)
Biblioteca_entrada.vai()

