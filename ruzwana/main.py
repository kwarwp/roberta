# roberta.ruzwana.main.py
from circus.circus import circus

TOPO_ESQUERDA = "LS"
TOPO_DIREITA = "LO"
TOPO_CENTRO = "JN"
MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "JO", "FN", "JL"
FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA =  "GS", "JS", "GL"

# O comando abaixo voce vai entender no próximo desafio
circus(1, [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
        MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]])

def desafio1():    
    MASMORRA = [[ "LS", "JN", "HN", "JN", "HN", "LO"],
                [ "HO", "AN", "FN", "FN", "BN", "IL"],
                [ "JO", "DO", "AO", "BL", "DO", "JL"],
                [ "IO", "AO", "DS", "DN", "AN", "AN"],
                [ "GS", "AN", "AN", "AN", "AN", "AN"]
                ]

    circus(2, MASMORRA,2)

if __name__ == "__main__":
	desafio1()
    
