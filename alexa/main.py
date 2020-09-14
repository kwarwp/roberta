# roberta.alexa.main.py

"""     xxxxx

.. codeauthor:: Monica Novellino <monicanovellino@gmail.com>

Changelog
---------
.. versionadded::    
       - 1.0

"""

from _spy.vitollino.main import Cena, STYLE

STYLE["width"] = 900 # width = 300 (default)
STYLE["heigth"] = "900px" # min-height = "300px"

floresta = "https://www.oeco.org.br/wp-content/uploads/2019/08/floresta-Kjell-Eson.jpg"
floresta_verde = Cena(floresta)
floresta_verde.vai()

