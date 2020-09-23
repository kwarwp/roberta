# roberta.naomi.main.py
"""     xxxxx

.. codeauthor:: Angelica <.........@gmail.com>
.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""
#NSLO
from circus.circus import circus

def desafio1():
    TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA    = "LS", "JN", "LO"
    MEIO_ESQUERDA, CENTRO, MEIO_DIREITA         = "JO", "FN", "JL"
    FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA = "GS", "JS", "GL"

    # O comando abaixo voce vai entender no próximo desafio
    circus(1, [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
            MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]])
            
            
def desafio2():
    MASMORRA = [[ "LS", "JN", "HN", "JN", "HN", "LO"],
                [ "HO", "AN", "FN", "FN", "BN", "IL"],
                [ "JO", "DO", "AO", "BL", "DO", "JL"],
                [ "IO", "AO", "DS", "DN", "CL", "HL"],
                [ "GS", "JS", "HS", "HS", "JS", "GL"]
                ]
    circus(2, MASMORRA)

def desafio3():
    MASMORRA = {'Cahuitz': 'JS', 'Cauha': 'JN', 'Coycol': 'LS',
                'Huatlya': 'JO', 'Micpe': 'JL', 'Nenea': 'GS',
                'Pallotl': 'GL', 'Tetlah': 'LO', 'Zitllo': 'FN'}
    circus(3, MASMORRA)
    
def desafio4():
    MASMORRA = {'Cahuitz': 'LO', 'Cauha': 'LS', 'Coycol': 'JS',
                'Huatlya': 'JL', 'Micpe': 'GS', 'Nenea': 'JN',
                'Pallotl': 'JO', 'Tetlah': 'FN', 'Zitllo': 'GL'}
    circus(4, MASMORRA)
    
def desafio5():
    MASMORRA = {'Cahuitz': "LS", 'Cauha': "JN", 'Coycol': "LO",
                'Huatlya': "JO", 'Micpe': "FN", 'Nenea': "JL",
                'Pallotl': "GS", 'Tetlah': "JS", 'Zitllo': "GL"}
    circus(5, MASMORRA)

if __name__ == "__main__":
    desafio5()