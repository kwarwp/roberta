# roberta.ruzwana.main.py
from circus.circus import circus

TOPO_ESQUERDA = "LS"
TOPO_DIREITA = "LO"
TOPO_CENTRO = "JN"
MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "JO", "FN", "JL"
FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA =  "GS", "JS", "GO"

# O comando abaixo voce vai entender no próximo desafio
circus(1, [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO,
        MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]])
if __name__ == "__main__":
	desafio0()