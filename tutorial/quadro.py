# roberta.tutorial.quadro.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""     xxxxx

.. codeauthor:: Emanuelle Simas <ellesimas@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""
numero=5

def verifica():
    if numero > 5:
        print("Numero é maior que cinco")
    elif numero == 5:
        print("Opa! Igualdade")
    else:
        print("Numero não é maior que cinco")
#verifica()

animais = ["macaco","águia","pardal","leão", "cachorro"]

for x in animais:
    #print(x)
    if x == "leão":
        break
    print(x)

