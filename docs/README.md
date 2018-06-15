# Module `imtfc`

## **Function decorator** : `@imtfc_cache(  *args, **kwargs )`

`@imtfc_cache` accepts any arguments that `datetime.timedelta` also accepts. These arguments are passed into a `timedelta` object, and this is used as the expiry time for the cache

### Implementation example

```python
@imtfc_cache(seconds=30)
def wrapped_function():
  # Code here
```

## **method** : `wrapped_function.purge_cache()`

This clears the cache

### Implementation example

```python
@imtfc_cache(seconds=30)
def wrapped_function():
  # Code here

wrapped_function.purge_cache()
```
