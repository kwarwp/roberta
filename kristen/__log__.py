
{'date': 'Mon Sep 14 2020 21:14:51.66 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 25
  borboleta = Cena(BORBOLETA, esquerda = floresta_verde
                                                          ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 14 2020 21:15:08.284 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 25
  borboleta = Cena(BORBOLETA, esquerda = florest_verde
                                                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 14 2020 21:15:27.340 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 28
  oca = Cena(BORBOLETA, 
            ^
SyntaxError: Unbalanced bracket (
'''},
{'date': 'Mon Sep 14 2020 21:15:47.951 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 27
    borboleta = Cena(MUNDO, esquerda = floresta_verde)
NameError: name 'MUNDO' is not defined
'''},