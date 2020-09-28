# roberta.callie.main.py
"""     xxxxx

.. codeauthor:: Marcelle Simas <simascelle@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""

numero=3

def verifica():
    if numero < 6: 
        print("numero é menor que seis")
    elif numero == 6:
        print("igualdade")
    else:
         print("numero não é menor que seis")
#verifica()

animais = ["leão","elefante","macaco","girafa", "borboleta"]

for x in animais:
    print(x)
    if x == "girafa":
         continue
    print(x)