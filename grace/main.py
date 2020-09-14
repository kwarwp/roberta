# roberta.grace.main.py"""     xxxxx

.. codeauthor:: mariaclara <mari4cla@gmail.com>

Changelog
---------
.. versionadded::    
       - xxx

"""
Define uma Sala ou uma Cena vazia.
    .. doctest::
        >>> cena = Cena(SalaCenaNula())  # A próxima cena
        >>> uma_cena = Cena(SalaCenaNula(), cena)  # Cena nula à esquerda, proxima no meio
        >>> uma_cena.vai_esquerda()  # tenta navegar para a cena à esquerda
        >>> # não vai, pois a cena é nula e não deixa que se navegue para ela
        >>> print(INVENTARIO.cena == cena)
        True
    Deve ser usado quando um parâmetro requer uma cena mas não deve ter uma cena válida ali.
    """

    numero_um = 1
    numero_dois = 2.3
    letras = "oi, bom dia"
    
    operacao = numero_um + letras
    
    print (operacao) 
    
    
    