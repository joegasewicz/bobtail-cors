"""
Quick Start
===========

Installation::

    pip install bobtail-cors

Basic Usage::

    from bobtail_cors import BobtailCORS

    app = Bobtail(routes=routes)

    app.use(BobtailCORS())


To restrict cross domain access so no domain other than http://nottoboard.com
can access the resource in a cross-origin manner::

    # Declare your CORS options
    options = {
            "origin": "http://nottoboard.com",
            "headers": "Authorization, Content-Type",
            "methods": "GET",
    }
    app.use(BobtailCORS(options=options))

"""
from typing import Dict
from bobtail import AbstractMiddleware, Request, Response, Tail


class BobtailCORS(AbstractMiddleware):
    """
    BobtailCORS
    :kwargs:
    :key options: A Python dict of key values representing each CORS
                  option.
                  - origin
                  - headers
                  - methods
    """

    _options: Dict = {
        "origin": "*",
        "headers": "Authorization, Content-Type",
        "methods": "GET,POST,DELETE,PUT,PATCH",
    }

    def __init__(self, **kwargs):
        try:
            self._options = {
                **self._options,
                **kwargs["options"],
            }
        except KeyError:
            pass

    def run(self, req: Request, res: Response, tail: Tail) -> None:
        res.set_headers({
            "Access-Control-Allow-Origin": self._options["origin"],
            "Access-Control-Allow-Headers": self._options["headers"],
            "Access-Control-Allow-Methods": self._options["methods"],
        })
        tail(req, res)
