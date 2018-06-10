# imtfc

In-Memory Time-based Function Caching for Python 3

Similar to [`functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache), except `imtfc.cache` uses a time limit to decide whether or not to use the cached value (and whether or not to renew the cache), instead of the function parameters like `lru_cache` does

It essentially allows you to store the returned variable from a function, and only allows that function to be executed again if a certain time has passed since it was last executed

See the example below for a more visual explanation

## Example

```python
from imtfc import cache, timedelta
from time import sleep

def complicatedFunction():
    # Super complex code here
    return calculatedValue

function_cache = cache(complicatedFunction, timedelta(seconds=20))

for count in range(100):
    data = function_cache.get()
    sleep(5)
```

Step by step:

- Import what we need
- Define a function, `complicatedFunction`, that relies heavily on the CPU, and returns a value
- Create an instance of the `cache` object, using `complicatedFunction` as the function parameter, and use a cache expiry time of 20 seconds
- Start a loop, which requests `complicatedFunction`s value from the cache every 5 seconds

When the loop happens, this is what happens inside the cache object:

- If the cache has expired, run `complicatedFunction` directly and return the calculated value
- Else, return the previously calculated value that has been stored in memory

"Expired" means that, in this instance, 20 seconds have passed since the last time `complicatedFunction` was called

## Installation

**`pip install imtfc`**

## [Documentation](Docs.md)

## Why?

One use case for this (as shown in the example) is if you have a function that relies on heavy CPU / GPU / Memory usage. If you are calling a function like this very frequently, you probably don't want to destroy your machines CPU / GPU / Memory usage by actually running the function.

Another use case would be is if you run an API request on an event (such as a user loading a webpage). You don't want to execute this API request every time this event happens, otherwise you would just be spamming the API. Instead, using this caching method, you still get normal API responses, but you will actually only be requesting from the API when the cache expires
