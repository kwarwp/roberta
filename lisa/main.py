# roberta.lisa.main.py
"""     xxxxx
.. codeauthor:: Luiza <luizaanjo2007@gmail.com>
.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

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
                    [ "HO", "AN", "AN", "AN", "AN", "IL"],
                    [ "JO", "DO", "AN", "AN", "AN", "JL"],
                    [ "IO", "ON", "AN", "AN", "AN", "HL"],
                    [ "GS", "JS", "HS", "HS", "JS", "GL"]
                    ]

    circus(2, MASMORRA,2)


                # faça aqui a sua implementação do desafio
if __name__ == "__main__":
    desafio1()
            #circus(<ponha aqui o número do desafio e descomente a linha>, <parâmetro indicado>)

        
