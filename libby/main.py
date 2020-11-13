# roberta.libby.main.py
"""     xxxxx

.. codeauthor:: Livia Machado <liviamcampos98@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""


from _spy.vitollino.main import Cena
"""Importa a classe Cena do Vitollino"""

IMAGEM_QUALQUER = 'https://i.imgur.com/Wn43yRS.jpeg' # Extensões aceitas: png, jpg, jpeg e gif
IMAGEM_ESQUERDA = "https://i.imgur.com/8c5lNV5.jpg" # Extensões aceitas: png, jpg, jpeg e gif
IMAGEM_DIREITA = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
IMAGEM_MEIO = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif

nome_da_cena_direita = Cena(IMAGEM_DIREITA)
nome_da_cena_esquerda = Cena(IMAGEM_ESQUERDA)
nome_da_cena = Cena(IMAGEM_QUALQUER, # Parâmetro obrigatório
                esquerda=nome_da_cena_esquerda, # default = NADA = SalaCenaNula()
                direita=nome_da_cena_direita,  # default = NADA = SalaCenaNula()
                meio=Cena(IMAGEM_MEIO)) # default = NADA = SalaCenaNula()
nome_da_cena_esquerda.esquerda = nome_da_cena
from _spy.vitollino.main import Cena, Elemento
""" O botão é o elementoclicável de alguma cena.
"""
MINHA_CENA = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
MEU_ELEMENTO = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif

def funcao_de_acao_do_botao(event = None):
    #Funcao chamada no clique
    print("Você clicou no botão!") # evento associado ao clique: mensagem, cena, sala,módulo...

nome_da_cena = Cena(MINHA_CENA)
nome_da_cena.vai() # instancia a cena
nome_do_elemento = Elemento(MEU_ELEMENTO, tit="título_do_elemento",
                           style=dict(height=60,widht=60, left=600, top=20), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                           cena = nome_da_cena,
                           vai = funcao_de_acao_do_botao)
nome_da_cena.vai()