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
    MASMORRA = [[ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "AN", "AN", "AN", "AN", "AN"],
                [ "AN", "JS", "AN", "AN", "AN", "AN"]
                ]

def desafio2():
    MASMORRA = {'Cahuitz': 'AN', 'Cauha': 'AN', 'Coycol': 'AN',
                'Huatlya': 'AN', 'Micpe': 'AN', 'Nenea': 'AN',
                'Pallotl': 'AN', 'Tetlah': 'AN', 'Zitllo': 'AN'}
def desafio3():
    MASMORRA = {'Cahuitz': 'AN', 'Cauha': 'AN', 'Coycol': 'AN',
                'Huatlya': 'AN', 'Micpe': 'AN', 'Nenea': 'AN',
                'Pallotl': 'AN', 'Tetlah': 'AN', 'Zitllo': 'AN'}


    circus(4, MASMORRA, 4)

# faça aqui a sua implementação do desafio
if __name__ == "__main__":
    desafio1()
    #circus(<ponha aqui o número do desafio e descomente a linha>, <parâmetro indicado>)
