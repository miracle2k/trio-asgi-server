import trio

class App():
    def __init__(self, scope):
        self.scope = scope

    async def __call__(self, receive, send):        
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': b'Wait 5 seconds for the rest...\n',
            'more_body': True
        })        
        await send({
            'type': 'http.response.body',
            'body': b'And that is it. FIN.',
            'more_body': False
        })
