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
  
    """