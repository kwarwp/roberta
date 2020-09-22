
{'date': 'Mon Sep 21 2020 20:14:02.801 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 17
  #circus(<ponha aqui o número do desafio e descomente a linha>, <parâmetro indicado>)
                                                                                      ^
IndentationError: expected an indented block
'''},
{'date': 'Mon Sep 21 2020 20:14:11.881 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 17
  #circus(<ponha aqui o número do desafio e descomente a linha>, <parâmetro indicado>)
                                                                                      ^
IndentationError: expected an indented block
'''},
{'date': 'Mon Sep 21 2020 20:14:19.344 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 16
  if __name__ == "__main__":#circus(<ponha aqui o número do desafio e descomente a linha>, <parâmetro indicado>)
                                                                                                                ^
IndentationError: expected an indented block
'''},
{'date': 'Tue Sep 22 2020 12:35:49.481 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 43
    circus(3, MASMORRA)
NameError: name 'MASMORRA' is not defined
'''},
{'date': 'Tue Sep 22 2020 14:01:16.622 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 46
    desafio2()
  module <module> line 35
    circus(2, MASMORRA)
  module circus.circus line 179
    Aldeia(Jogo()).circus(desafio, solucao, desafio)
  module circus.circus line 158
    self.desafios[desafio](solucao)
  module circus.circus line 123
    c = [Piso(self.cena, 10*LADO+i*LADO, j*LADO, ai ) for j, linha in enumerate(solucao) for i, ai in enumerate(linha)]
  module circus.circus line 33
    az = azz[ai[1]]
KeyError: D
'''},
{'date': 'Tue Sep 22 2020 14:01:28.924 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 46
    desafio2()
  module <module> line 35
    circus(2, MASMORRA)
  module circus.circus line 179
    Aldeia(Jogo()).circus(desafio, solucao, desafio)
  module circus.circus line 158
    self.desafios[desafio](solucao)
  module circus.circus line 123
    c = [Piso(self.cena, 10*LADO+i*LADO, j*LADO, ai ) for j, linha in enumerate(solucao) for i, ai in enumerate(linha)]
  module circus.circus line 33
    az = azz[ai[1]]
KeyError: D
'''},