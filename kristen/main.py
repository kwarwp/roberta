# roberta.kristen.main.py
"""     xxxxx

.. codeauthor:: Lilian <lilianes93@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""
numero = -2

def verifica():
    if numero > 5:
        print("Numero é maior que cinco")
    elif numero == 5:
        print("Opa! Igualdade")
    else:
        print("Numero não é maior que cinco")

#verifica()

animais = ["macaco", "gato", "cachorro", "cavalo"]
'''
for x in animais:
    print(x) #inclui o gato
    if x=="gato":
        break
    #print(x) #exclui o leão
    
#print(animais)
'''

for x in animais:
    if x == "leao":
        continue
    print(x)
