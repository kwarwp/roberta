
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