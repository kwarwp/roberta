
{'date': 'Thu Sep 17 2020 21:03:23.845 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 22
  print(val[0].__add__(val[]) 
                                                                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Sep 17 2020 21:09:09.221 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 22
  print(val[0].__add__(val[1])
                                                                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Sep 17 2020 21:09:16.202 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 38
    numeros.opera_soma_tambem(1.3,1.5,1.6)
NameError: name 'numeros' is not defined
'''},
{'date': 'Thu Sep 17 2020 21:09:25.920 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 41
    print("O tipo do 'operacao_um' é:", type(operacao_um)) #NoneType
NameError: name 'operacao_um' is not defined
'''},
{'date': 'Thu Sep 17 2020 21:09:33.366 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 47
    opera_soma_pesos(antoni=40,lucia=30)
NameError: name 'opera_soma_pesos' is not defined
'''},
{'date': 'Thu Sep 17 2020 21:16:06.176 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 32
  """ """"
          ^
SyntaxError: EOL while scanning string literal
'''},
{'date': 'Thu Sep 17 2020 21:16:15.40 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
'error': '''(['antoni', 'lucia'], 70)
Traceback (most recent call last):
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
  module <module> line 51
    print(Numeros.val)
AttributeError: 'Numeros' object has no attribute 'val'
'''},