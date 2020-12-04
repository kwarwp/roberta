# roberta.libby.main.py
"""     xxxxx

.. codeauthor:: Livia Machado <liviamcampos98@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""


from _spy.vitollino.main import Cena, Elemento, STYLE, Texto
#from cenas.imix import Inicial
#from cenas.ik import Passeio
#from cenas.ik import Passeio

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
papel_rasgado = 'https://cdn.pixabay.com/photo/2019/03/18/15/10/torn-paper-4063317_960_720.png'
imagem_mapa ='https://comps.canstockphoto.com.br/cidade-mapa-pequeno-sub%C3%BArbio-vila-vetor-clip-arte_csp14479563.jpg'
#CENAS
#tamanho padrão das cenas
STYLE["width"] = 960 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

cena1 = Cena(imagem_quarto)
cena4 = Cena(imagem_mapa)

STYLE["width"] = 700 #  width = 300 (default)
STYLE["heigth"] = '600px' # min-height = "300px"

cena2= Cena(imagem_livroaberto)

STYLE["width"] = 394 #  width = 300 (default)
STYLE["heigth"] = '521px'

cena3= Cena(papel_rasgado)

#FUNCOES

def funcao_de_acao_do_botao(event = None):
    cena2.vai()
def funcao_de_acao_do_botao2(event = None):
    cena3.vai()

texto_1 = Texto(cena1, txt = "Encontre o livro")

LIVRO= Elemento(imagem_livro, tit="título_do_elemento",
                style=dict(height=50,widht=56, left=450, top=250), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                cena = cena1)
         
                
PAPEL_RASGADO = Elemento(papel_rasgado, tit="título_do_elemento", 
                         w=578, h=437, x=450, y=250, 
                         cena = cena2)

#resposta_desafio1= input('Qual é a resposta do desafio?')

def desafio1():
    possivel_resposta=""
    resposta1=input('Qual é a resposta do desafio?')
    resposta2=resposta1.lower()
    if resposta2 == 'va para a biblioteca' or 'vá para a biblioteca' :
        cena4.vai()
        parabens = Texto(cena4, txt = "Parabéns, você acertou!")
        parabens.vai()
#    elif resposta1== 'Vá para a biblioteca':
#        cena4.vai()
#        parabens.vai()
#    elif resposta1 == 'vá para a biblioteca':
#        cena4.vai()
#        parabens.vai()
#    elif resposta1 == 'Va para a biblioteca':
#        cena4.vai()
#        parabens.vai()
    else:
        tente_novamente=Texto(cena3, txt = "Tente novamente.")
        tente_novamente.vai()
#def resultado(A):
# O novo popupque será gerado quando o foi() do texto forchamado
#        dicionario = dict(A=('vc clicou no A')) # dicionário que guarda a devolutiva da opção escolhida
#        devolutiva = Texto(cena2, txt=dicionario[A])
#        devolutiva.vai()


#pergunta = Texto(cena3, txt = pergunta2, foi = resultado, A=input(pergunta2))


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
texto_1.vai()
LIVRO.elt.bind("click", funcao_de_acao_do_botao)
PAPEL_RASGADO.elt.bind("click", funcao_de_acao_do_botao2)
cena3.elt.bind("click", desafio1)




#texto_.vai()
#LIVRO.elt.bind("click", funcao_de_acao_do_botao)



