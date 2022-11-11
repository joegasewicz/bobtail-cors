class BobtailCORS(AbstractMiddleware):

    def __init__(self):
        pass

    def init(self, req: Request, res: Response, tail: Tail) -> None:
        res.set_headers({
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Authorization, Content-Type",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,PUT",
        })
        tail(req, res)