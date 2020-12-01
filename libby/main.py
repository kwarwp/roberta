# roberta.libby.main.py
"""     xxxxx

.. codeauthor:: Livia Machado <liviamcampos98@gmail.com>

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
    #Funcao chamada no clique
    print("Você clicou no botão!") # evento associado ao clique: mensagem, cena, sala,módulo...


cena1.vai() # instancia a cena
botao_livro= Elemento(LIVRO, tit="título_do_elemento",
                           style=dict(height=50,widht=56, left=450, top=300), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = cena1,
                           vai = funcao_de_acao_do_botao)
cena1.vai()