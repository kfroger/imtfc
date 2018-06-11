from datetime import datetime, timedelta

class imtfc_cache(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    
    def __call__(self, original_function):
        self.cacheExpiryDelta = timedelta(*self.args, **self.kwargs)
        self.previousRequestTime = datetime.now() - self.cacheExpiryDelta

        def wrapper_function(*args, **kwargs):
            currentTime = datetime.now()
            currentDelta = currentTime - self.previousRequestTime
            if currentDelta >= self.cacheExpiryDelta:
                self.cachedReturn = original_function(*args, **kwargs)
                self.previousRequestTime = currentTime
            return self.cachedReturn

        return wrapper_function
