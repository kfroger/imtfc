# imtfc

In-Memory Time-based Function Caching for Python 3

Similar to [`@functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache), this allows you to cache the return value of a function

`@imtfc_cache` is different as it only caches the most recent value, and renewing the cache depends on a time limit

It essentially allows you to store the returned variable from a function, and only allows that function to be executed again if a certain time has passed since it was last executed

See the example below for a more visual explanation

## Example

```python
from imtfc import imtfc_cache
from time import sleep

@imtfc_cache(seconds=20)
def complicatedFunction():
    # Super complex code here
    return calculatedValue

for count in range(100):
    data = complicatedFunction()
    sleep(5)
```

Step by step:

- Import what we need
- Define a function, `complicatedFunction`, that relies heavily on the CPU, and returns a value
- Decorate `complicatedFunction` using the `imtfc_cache` decorator and use a cache expiry time of 20 seconds
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
