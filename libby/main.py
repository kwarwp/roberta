# roberta.libby.main.py
"""     xxxxx

.. codeauthor:: Livia Machado <liviamcampos98@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""


from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
from cenas.imix import Inicial
#from cenas.ik import Passeio
from cenas.ik import Passeio

#Classes

'''class Estrutura():

    def __init__(self):
        self.fundo = Cena(imagem_quarto)
        self.fundo.vai()
        """ Primeiro modo de criar um botão. Utiliza a função vai() do vitollino"""
        self.livro= Elemento(imagem_livro, tit="Livro de Receita", x=0, y=100, w=100, h=100, cena1, vai=self.botao_17082020)
        """ Segundo modo de criar um botão"""
        self.livro.elt.bind("click", self.botao_17082020)
        
    def botao_17082020(self, event=None):
        """ Função que será chamado no clique do IMIX"""
        Inicial().chama(cena2)'''
        
        
#IMAGENS

imagem_quarto = 'https://i.pinimg.com/originals/66/88/9a/66889a5a4db243c94e3c0623df56e664.jpg'
imagem_livro = 'https://livrariaconcreta.com.br/wp-content/uploads/2017/01/Hardcover-Book-MockUp-LIVRO-VERMELHO.png'
imagem_livroaberto = 'https://images.vexels.com/media/users/3/157260/isolated/preview/d48b34b2e855b69b29d5565edda69536-vetor-de-livro-aberto-em-branco-by-vexels.png'

#CENAS
#tamanho padrão das cenas
STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

cena1 = Cena(imagem_quarto)

#cena2= Cena(imagem_livroaberto)
#STYLE["width"] = 960 #  width = 300 (default)
#STYLE["heigth"] = '600px' # min-height = "300px"

#FUNCOES

def funcao_de_acao_do_botao(event = None):
    cena2= Cena(imagem_livroaberto)
    STYLE["width"] = 300 # modificação local do tamanho da cena. se voltar para a outra cena, o outro valor volta por causa do escopo
    STYLE["heigth"] = '300px' # min-height = "300px"
    cena2 = Cena(imagem_livroaberto)
    cena2.vai()

LIVRO= Elemento(imagem_livro, tit="título_do_elemento",
                style=dict(height=50,widht=56, left=450, top=250), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                cena = cena1)
                #vai = funcao_de_acao_do_botao)

#def funcao_de_abrir_o_livro(event = None):
    #Funcao chamada no clique
#    print("Você clicou no botão!") # evento associado ao clique: mensagem, cena, sala,módulo...

#ELEMENTOS

#LIVRO= Elemento(imagem_livro, tit="título_do_elemento",
#                style=dict(height=50,widht=56, left=450, top=250), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
#                cena = cena1,
#                vai = funcao_de_abrir_o_livro)

#LIVRO_ABERTO = Elemento(imagem_livroaberto, tit="título_do_elemento",
#                        style=dict(height=60,widht=60, left=600, top=20), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
#                        cena = cena1)



#texto_ = Texto(cena1, txt = "Mensagem desejada", foi = chama_elemento) # o método foi() esconde o popup



#RODA 

cena1.vai()
LIVRO.elt.bind("click", funcao_de_acao_do_botao)

#texto_.vai()
#LIVRO.elt.bind("click", funcao_de_acao_do_botao)



