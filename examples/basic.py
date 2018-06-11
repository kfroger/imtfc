"""
This is a basic example that shows the normal usage of imtfc_cache

currentTime will be called 10 times, each call with 2 seconds inbetween. This
means it will run over a 20 second peroid. During this period, since the cache
expiry time is set to 6 seconds, currentTime will update its return value 4
times:
- At the start of the loop
- 6 seconds in
- 12 seconds in
- 18 seconds in
"""

from datetime import datetime
from imtfc import imtfc_cache
from time import sleep

@imtfc_cache(seconds=6)
def currentTime():
    # Print current date & time
    return str(datetime.now())

for x in range(10):
    print(currentTime())
    sleep(2)
