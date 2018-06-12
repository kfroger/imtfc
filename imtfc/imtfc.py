from datetime import datetime, timedelta

class imtfc_cache(object):
    def __init__(self, *args, **kwargs):
        # So we can use wrapper arguments later
        self.args = args
        self.kwargs = kwargs
    
    def __call__(self, original_function):
        # Set cache expiry
        self.cacheExpiryDelta = timedelta(*self.args, **self.kwargs)
        # This sets up variables we need for wrapper_function
        self.purge_cache()

        def wrapper_function(*args, **kwargs):
            currentTime = datetime.now()
            currentDelta = currentTime - self.previousRequestTime
            if currentDelta >= self.cacheExpiryDelta:
                self.cachedReturn = original_function(*args, **kwargs)
                self.previousRequestTime = currentTime
            return self.cachedReturn

        wrapper_function.purge_cache = self.purge_cache
        return wrapper_function
    
    def purge_cache(self):
        # We need to reset the time so that original_function will be called
        self.previousRequestTime = datetime.now() - self.cacheExpiryDelta
        self.cachedReturn = None
