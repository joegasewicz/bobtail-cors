# Bobtail CORS
CORS middleware for Bobtail

### Install
```
pip install bobtail-cors
```

### Usage
The default CORS set by 
```python
from bobtail_cors import BobtailCORS

app = Bobtail(routes=routes)

app.use(BobtailCORS())

```

If you require
```python
# Declare your CORS options
options = {
        "origin": "http://nottoboard.com",
        "headers": "Authorization, Content-Type",
        "methods": "GET",
}
app.use(BobtailCORS(options=options))
```