# imtfc

In-Memory Time-based Function Caching for Python 3

Similar to [`@functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache), this allows you to cache the return value of a function

`@imtfc.imtfc_cache` is different as it only caches the most recent value, and renewing the cache depends on a time limit. Unlike `lru_cache`, function parameters do not have anything to do with the caching

It essentially allows you to store the returned variable from a function, and only allows that function to be executed again if a certain time has passed since it was last executed

See the example below for a more visual explanation

## Example

```python
from imtfc import imtfc_cache
from time import sleep

@imtfc_cache(seconds=6)
def double(x):
    return x*2

for num in range(10):
    doubled = double(num)
    print("num: " + str(num) + " - doubled: " + str(doubled))
    sleep(2)
```

Step by step:

- Import what we need
- Define a function, `double`, that will double `x`
- Decorate `double` using the `imtfc_cache` decorator and use a cache expiry time of 6 seconds
- Start a loop, which calls `double` on all the numbers in `range(10)`
- Wait for 2 seconds between each iteration of the loop

When `double` gets called, this is what happens inside the cache:

- If the cache has expired, run `double` directly and return the calculated value
- Else, return the previously calculated value that has been stored in memory

"Expired" means that, in this instance, 6 seconds have passed since the last time `double` was called

The output will looks like this (with added comments to explain what is happening):

```python
# Cache initialised, call double() on 0 and store the returned value in memory
num: 0 - doubled: 0
# It has not been 6 seconds since we last called double(), so return our last calculated value from memory
num: 1 - doubled: 0
num: 2 - doubled: 0
# It has now been 6 seconds, clear the cache and call double() on the new number, save this in memory
num: 3 - doubled: 6
num: 4 - doubled: 6
num: 5 - doubled: 6
# It has been another 6 seconds, call double() again on the current number and store the new value
num: 6 - doubled: 12
num: 7 - doubled: 12
num: 8 - doubled: 12
# Another 6 seconds have passed, do the same
num: 9 - doubled: 18
```

## Installation

**`pip install imtfc`**

## [Documentation](https://github.com/psidex/imtfc/blob/master/docs/README.md)

## Why?

One use case for this is if you have a function that relies on heavy CPU / GPU / Memory usage. If you are calling a function like this very frequently, you probably don't want to destroy your machines CPU / GPU / Memory usage by actually running the function

Another use case would be is if you run an API request on an event (such as a user loading a webpage). You don't want to execute this API request every time this event happens, otherwise you would just be spamming the API with requests. Instead, using this caching method, you still get normal API responses, but you will actually only be requesting from the API when the cache expires
