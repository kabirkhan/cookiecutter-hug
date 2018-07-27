import hug
import api

@hug.cli()
@hug.get('/health')
@hug.local()
def health_check():
    return {'message': 'Status: Running'}


# @hug.extend_api('/{BASE_URL_ROUTE}')
@hug.extend_api()
def apis():
    return [api]
