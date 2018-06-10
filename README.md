# imc

In-memory Caching for Python function return values

This allows you to store the returned variable from a function, and only run the function if a certain time has passed since it was last computed

See the example below for a more visual explanation

## Example

```python
from imc import cache, timedelta
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
- Else, return the calculated value that has been stored in memory

"Expired" means that, in this instance, 20 seconds have passed since the last time `complicatedFunction` was called

## Installation

**`pip install imc`**

## [Documentation](Docs.md)

## Why?

One use case for this (as shown in the example) is if you have a function that relies on heavy CPU / GPU / Memory usage. The `cache` class will allow you to store the returned variable from that function, and only run the calculation if a certain time has passed since it was last computed
