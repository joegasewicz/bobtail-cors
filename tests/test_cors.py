from bobtail_cors.cors import BobtailCORS
from bobtail.request import Request
from bobtail.response import Response


class TestBobtailCORS:

    def test_run_default(self):
        req = Request("/", "GET")
        res = Response()
        b = BobtailCORS()
        b.run(req, res, lambda rq, rs: None)
        assert res.headers["Access-Control-Allow-Origin"] == "*"
        assert res.headers["Access-Control-Allow-Headers"] == "Authorization, Content-Type"
        assert res.headers["Access-Control-Allow-Methods"] == "GET,POST,DELETE,PUT,PATCH"

    def test_run_updated(self):
        o = {
            "origin": "https://noticeboard.com",
            "headers": "*",
            "methods": "GET",
        }
        req = Request("/", "GET")
        res = Response()
        b = BobtailCORS(options=o)
        b.run(req, res, lambda rq, rs: None)
        assert res.headers["Access-Control-Allow-Origin"] == "https://noticeboard.com"
        assert res.headers["Access-Control-Allow-Headers"] == "*"
        assert res.headers["Access-Control-Allow-Methods"] == "GET"

