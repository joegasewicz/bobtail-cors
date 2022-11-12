[![Upload Python Package](https://github.com/joegasewicz/bobtail-cors/actions/workflows/python-publish.yml/badge.svg)](https://github.com/joegasewicz/bobtail-cors/actions/workflows/python-publish.yml)
[![Python package](https://github.com/joegasewicz/bobtail-cors/actions/workflows/python-package.yml/badge.svg)](https://github.com/joegasewicz/bobtail-cors/actions/workflows/python-package.yml)

# Bobtail CORS
CORS middleware for [Bobtail](https://github.com/joegasewicz/bobtail)

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