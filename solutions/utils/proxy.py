def proxyCall(obj, method, args):
    return getattr(obj, method)(*args)