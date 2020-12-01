# roberta.libby.main.py
"""     xxxxx

.. codeauthor:: Mariana Bittencourt <cmarianab3@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""


from _spy.vitollino.main import Cena, Elemento, STYLE, Texto


imagem_quarto = 'https://i.pinimg.com/originals/66/88/9a/66889a5a4db243c94e3c0623df56e664.jpg'
cena1 = Cena(imagem_quarto)
STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"
LIVRO = 'https://livrariaconcreta.com.br/wp-content/uploads/2017/01/Hardcover-Book-MockUp-LIVRO-VERMELHO.png'
def funcao_de_acao_do_botao(event = None):
    texto_surpresa = Texto(cena1, txt ="Mensagem que você deseja passar!")
    texto_surpresa.vai()


cena1.vai() # instancia a cena
botao_livro= Elemento(LIVRO, tit="título_do_elemento",
                           style=dict(height=500,widht=560, left=450, top=120), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = cena1,
                           vai = funcao_de_acao_do_botao)
cena1.vai()
nome_do_elemento.elt.bind("click", funcao_de_acao_do_botao)