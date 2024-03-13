from asgiref.local import Local

local = Local()


def get_wsgi_request():
    try:
        return local.request
    except AttributeError:
        return None


__all__ = ["local", "get_wsgi_request"]
