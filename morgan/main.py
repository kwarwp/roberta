# roberta.morgan.main.py



from circus.circus import circus 
def desafio0():
    TOPO_ESQUERDA = "LS"
    TOPO_DIREITA= "LO"
    TOPO_CENTRO= "JN"
    MEIO_ESQUERDA, CENTRO, MEIO_DIREITA = "JO", "FN", "AN"
    FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA = "AN", "AN","AN"
    # O comando abaixo você vai entender no próximo desafio

    circus(1, [[TOPO_ESQUERDA, TOPO_CENTRO, TOPO_DIREITA], [MEIO_ESQUERDA, CENTRO, MEIO_DIREITA], 
              [FUNDO_ESQUERDA, FUNDO_CENTRO, FUNDO_DIREITA]])



if __name__ == "__main__":
    desafio0()
