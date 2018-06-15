# Module `imtfc`

## **Function decorator** : `@imtfc_cache(  *args, **kwargs )`

This is a class set up as a function decorator

`@imtfc_cache` accepts any arguments that [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#timedelta-objects) also accepts. These arguments are passed into a [`timedelta`](https://docs.python.org/3/library/datetime.html#timedelta-objects) object, and this is used as the expiry time for the cache

### Implementation example

```python
@imtfc_cache(seconds=30)
def wrapped_function():
  # Code here
```

## **Method** : `wrapped_function.purge_cache()`

This clears the cache

The wrapped function inherits this method

### Implementation example

```python
@imtfc_cache(seconds=30)
def wrapped_function():
  # Code here

wrapped_function.purge_cache()
```
