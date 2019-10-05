def handler(context, event):
    response_body = f'Got {event.method} to {event.path} with "{event.body}"'

    context.logger.debug('This is a debug level message')

    return context.Response(body=response_body,
                            headers=None,
                            content_type='text/plain',
                            status_code=200)    