# imc

In-memory Caching for Python function return values

This allows you to ask the cache for the functions returned value many times, but the function will only actaully run the function if the cache has expired

See the example below for a detailed explanation

## Example

The below code has a function that performs a complex computation (`complicatedFunction`), which relies heavily on the CPU. The function is passed into a `cache` object, and the expiry delta set to 20 seconds.

Then, a loop is called, which asks the cache for the returned value from the complex function every 5 seconds. This loop happens 10 times, which means `complicatedFunction` will only be called three times throughout the loop, once at the start of the loop, once at 20 seconds in, when the cache expires, and then once again 20 seconds later, after the cache expires for a second time. The loop stops before another 20 seconds is reached

All the other times `function_cache.get()` is called in the loop, a value will still be returned, but it will just be the stored value, it will not a newly computed value

```python
from imc import cache, timedelta
from time import sleep

def complicatedFunction():
    # Super complex code here
    return calculatedValue

function_cache = cache(complicatedFunction, timedelta(seconds=20))

for count in range(10):
    data = function_cache.get()
    sleep(5)
```

## Installation

**`pip install imc`**

## [Documentation](Docs.md)

## Why?

One use case for this (as shown in the example) is if you have a function that relies on heavy CPU / GPU / Memory usage. The `cache` class will allow you to store the returned variable from that function, and only run the calculation if a certain time has passed since it was last computed
