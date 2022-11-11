# Bobtail CORS
CORS middleware for Bobtail

### Install
```
pip install bobtail-cors
```

### Usage
```python
from bobttail_cors import BobtailCORS
app = Bobtail(routes=routes)

app.use(BobtailCORS())

```