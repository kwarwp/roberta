"""     xxxxx

.. codeauthor:: Livia Machado <liviamcampos98@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""


from _spy.vitollino.main import Cena, Elemento, STYLE, Texto

#IMAGENS

imagem_quarto = 'https://i.pinimg.com/originals/66/88/9a/66889a5a4db243c94e3c0623df56e664.jpg'
imagem_livro = 'https://livrariaconcreta.com.br/wp-content/uploads/2017/01/Hardcover-Book-MockUp-LIVRO-VERMELHO.png'
imagem_livroaberto = 'https://images.vexels.com/media/users/3/157260/isolated/preview/d48b34b2e855b69b29d5565edda69536-vetor-de-livro-aberto-em-branco-by-vexels.png'

#CENAS

cena1 = Cena(imagem_quarto)
STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

#ELEMENTOS

LIVRO_ABERTO = Elemento(imagem_livroaberto, tit="título_do_elemento",
                           style=dict(height=60,widht=60, left=600, top=20), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = cena1)
LIVRO= Elemento(LIVRO, tit="título_do_elemento"),
                           style=dict(height=50,widht=56, left=450, top=250), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = cena1,
                           vai = funcao_de_acao_do_botao
                           
#FUNCOES

def funcao_de_acao_do_botao(event = None):
    texto_surpresa = Texto(cena1, txt ="Mensagem que você deseja passar!")
    texto_surpresa.vai()
def chama_elemento(*args):
    LIVRO= Elemento(LIVRO, tit="título_do_elemento",
                           style=dict(height=50,widht=56, left=450, top=250), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = cena1,
                           vai = funcao_de_acao_do_botao)
    LIVRO_ABERTO.entra(cena1)


texto_ = Texto(cena1, txt = "Mensagem desejada", foi = chama_elemento) # o método foi() esconde o popup

#RODA 

cena1.vai()
texto_.vai()
LIVRO.elt.bind("click", funcao_de_acao_do_botao)