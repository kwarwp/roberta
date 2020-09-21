# roberta.ruzwana.main.py
from _spy.circus.circus import circus
def desafio():
	TOPO_ESQUERDA = "LS"
	TOPO_DIREITA = "AN"
	TOPO_CENTRO = "AN"
	MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "AN", "AN", "AN"
	FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA =  "AN", "AN", "AN"

# O comando abaixo voce vai entender no próximo desafio
	circus(1, [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO, MEIO_DIREITA], [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]])
       
if __name__ == "__main__":
	desafio()