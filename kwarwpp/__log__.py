
{'date': 'Wed Sep 30 2020 13:07:48.708 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
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
    main(Jogo, STYLE)
  module <module> line 42
    return kwarwp_main(vitollino=vitollino, medidas=medidas, mapa=MAPA_INICIO, indios=(Kaiowa))
  module kwarwp.kwarwpp line 594
    return Kwarwp(vitollino=vitollino_proxy, medidas=medidas, mapa=mapa, indios=indios)
  module kwarwp.kwarwpp line 417
    self.indios = deque(indios or [Indio])
  module _collections line 48
    for elem in iterable:
TypeError: 'undefined' object is not iterable
'''},