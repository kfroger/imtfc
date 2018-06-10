from datetime import datetime, timedelta

class cache(object):
    def __init__(self, getFunction, expiryDelta):
        self.getFunction = getFunction
        self.cacheExpiryDelta = expiryDelta
        self.previousRequestTime = datetime.now() - expiryDelta
    
    def get(self):
        currentTime = datetime.now()
        currentDelta = currentTime - self.previousRequestTime
        if currentDelta >= self.cacheExpiryDelta:
            self.cachedReturn = self.getFunction()
            self.previousRequestTime = currentTime
        return self.cachedReturn
