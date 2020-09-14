
{'date': 'Mon Sep 14 2020 20:51:25.319 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 15
  STYLE["height'] = "900px"
                      ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 14 2020 20:51:50.951 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
  module <module> line 12
    from _spy.vitollino.main import Cena, Style
ImportError: cannot import name 'Style'

ImportError
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 268
    action()
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 12
    from _spy.vitollino.main import Cena, Style
'''},