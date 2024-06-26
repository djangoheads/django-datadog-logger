from asgiref.local import Local  # NOQA



local = Local()


def get_wsgi_request():
    return getattr(local, "request", None)


__all__ = ["local", "get_wsgi_request"]
