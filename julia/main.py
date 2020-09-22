# roberta.julia.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""     XXXXX

.. codeauthor:: Camila Silveira <camila.souzasilv@gmail.com>

Changelog
---------
.. versionadded::
       - XXX
       
"""
from _spy.vitollino.main import Cena, Style

STYLE ["width"] = 900
STYLE ["heigth"] = "900px"

FLORESTA = "https://macmagazine.uol.com.br/wp-content/uploads/2015/04/16-floresta.jpg"

floresta_verde = Cena(FLORESTA)

floresta_verde.vai()
