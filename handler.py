import hug


@hug.get('/sync/{who}')
def sync_get(who):
    return {'message': 'Hello %s' % who}


@hug.get('/sync/query')
def sync_get(who):
    return {'message': 'Hello %s' % who}


@hug.post('/sync/post')
def sync_get(body):
    return {'message': 'Hello world', 'body': body}


@hug.get('/async/{first}/{second}')
def async_get(first, second):
    print('%s %s' % (first, second))
    return True
