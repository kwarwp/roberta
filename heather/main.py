# roberta.heather.main.py
"""     xxxxx

.. codeauthor:: Hortencia e Lilian

Changelog
---------
.. versionadded::    
       - xxx

"""

from circus.circus import circus
def desafio0():
    TOPO_ESQUERDA = "LS"
    TOPO_DIREITA = "LO"
    TOPO_CENTRO = "JN"
    MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "JO", "FN", "JL"
    FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA =  "GS", "JS", "GL"

    # O comando abaixo voce vai entender no próximo desafio
    circus(1, [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
        MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]])
        
def desafio1():
    MASMORRA = [[ "LS", "JN", "HN", "JN", "HN", "KO"],
                [ "HO", "AN", "FN", "FN", "BN", "IL"],
                [ "JO", "DO", "AO", "CL", "DO", "JL"],
                [ "IO", "AO", "DS", "DN", "CL", "HL"],
                [ "GS", "JS", "HS", "HS", "JS", "GL"]
                ]

def desafio2():
    MASMORRA = {'Cahuitz': 'LS', 'Cauha': 'JN', 'Coycol': 'LS',
                'Huatlya': 'JO', 'Micpe': 'FN', 'Nenea': 'GS',
                'Pallotl': 'GO', 'Tetlah': 'LO', 'Zitllo': 'GL'}



    circus(3, MASMORRA, 3)

# faça aqui a sua implementação do desafio
if __name__ == "__main__":
    desafio2()
    #circus(<ponha aqui o número do desafio e descomente a linha>, <parâmetro indicado>)
