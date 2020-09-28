

"""     xxxxx

.. codeauthor:: Angelica Zumpichiatti <angelicazumpichiatti@yahoo.com.br>

Changelog
---------
.. versionadded::    
       - xxx
"""     
numero_um=1
numero_dois=2
letras = "Oi! Tudo bom?"

operacao = numero_um + numero_dois

print(operacao)

operacao_sub = numero_um - numero_dois

print(operacao_sub)

multiplica = numero_um * numero_dois

print(multiplica)

from _spy.vitollino.main import Cena.STYLE
STYLE["width"] = 900 
STYLE["heigth"] = "900px" 

FLORESTA = "https://cdn4.ecycle.com.br/cache/images/2018-07/50-650-floresta-amazonica.jpg"
MUNDO = "https://exame.com/wp-content/uploads/2016/09/size_960_16_9_terral9.jpg"
ARCO = "https://observatoriog.bol.uol.com.br/wordpress/wp-content/uploads/2019/07/Yoast-rainbow-songs-for-kids.jpg"
LAPIS = "https://produtosassistivos.com.br/wp-content/uploads/2018/08/mcr0011-lapis-de-cor-grosso-136.jpg"

mundo = Cena (MUNDO)
arco = Cena (ARCO)
lapis = Cena (LAPIS)

floresta_verde = Cena(FLORESTA, direita = mundo, esquerda = arco, meio = lapis)
floresta_verde.vai()

cena_direita = Cena(ARCO)
cena_esquerda = Cena (LAPIS)
cena_fundo = Cena(MUNDO, esquerda = cena_esquerda, direita = cena_direita)
cena_esquerda.direita = cena_fundo
cena_direita.esquerda = cena_fundo
cena_fundo.vai()

from _spy.vitollino.main import Cena, STYLE

FLOR = "http://obviousmag.org/em_cada_esquina/assets_c/2019/11/25bae4_o-que-fazer-quando-a-flor-do-girassol-morre-thumb-500x333-180378.jpg"
ARARA = "https://animais.culturamix.com/blog/wp-content/gallery/Araras-Azuis%3A-Belas-e-Raras-1/Araras-Azuis-1.jpg"
BORBOLETA = "https://pt.bcdn.biz/Files/2017/7/25/52524f4f-9ebb-48fe-9bd8-64fef7445aee.jpg"
STYLE["width"] = 900
STYLE["heigth"] = "900px"

cena_direita = Cena(FLOR)
cena_esquerda =Cena(ARARA)
cena_fundo = Cena(BORBOLETA, esquerda=cena_esquerda, direita=cena_direita)

cena_esquerda.direita = cena_fundo
cena_direita.esquerda = cena_fundo
cena_fundo.vai()

from _spy.vitollino.main import Cena
VARIAVEL = "https://veja.abril.com.br/wp-content/uploads/2016/05/ciencia-borboleta-danaus-plexippus-monarca-20130408-07-original1.jpeg"
def ambiente ():
    borboleta = Cena (VARIAVEL)
    borboleta.vai ()
ambiente ()


numero = 20
def verifica ():
    if numero > 5:
        print ("numero é maior que cinco")
    elif numero == 5:
        print ("Opa! Igualdade")
    else
        print ("número não é maior que cinco")
        
verifica ()