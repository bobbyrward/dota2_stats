

def template_params(request, **kwargs):
    params = {
        'settings': request.registry.settings,
        'request': request,
    }

    params.update(kwargs)

    return params
