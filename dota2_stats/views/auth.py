import json

from pyramid.view import view_config


@view_config(
    context='velruse.AuthenticationComplete',
    renderer='templates/login_result.jinja2'
)
def on_login_success(request):
    context = request.context
    result = {
        'profile': context.profile,
        'credentials': context.credentials,
    }
    return {
        'result': json.dumps(result, indent=4),
    }


@view_config(
    context='velruse.AuthenticationDenied',
    renderer='templates/login_result.jinja2'
)
def on_login_failure(request):
    return {
        'result': 'denied',
    }
