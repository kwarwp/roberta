# roberta.lisa.main.py
"""     xxxxx

.. codeauthor:: Luiza <luizaanjo2007@gmail.com>


Changelog
---------
.. versionadded::    
       - xxx

"""
numero=8

def verifica():
    if numero > 10:
        print("Numero é maior que dez")
    elif numero == 10:
        print ("Opa! Igualdade")
    else:
        print("Numero não é maior que dez")
#verifica()

animais = ["bolsonaro", "gato", "zebra", "vaca", "cavalo", "porco"]

for x in animais:
    if x == "vaca":
        continue
    print (x)
        
        