# roberta.danae.turtle.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    20.09
        Descreva o que você adicionou no código.

"""
from browser import document
import turtle
turtle.set_defaults(
 turtle_canvas_wrapper = document['pydiv'],
 canvwidth = 200,
 canvheight = 200
)
t = turtle.Turtle()
t.width(5)
for c in ['red', '#00ff00', '#fa0', 'rgb(0,0,200)']:
 t.color(c)
 t.forward(50)
 t.left(90)
#turtle.done()