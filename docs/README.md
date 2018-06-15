# Module `imtfc`

## **class** : `@imtfc_cache (  *args, **kwargs )`

`@imtfc_cache` accepts any arguments that `datetime.timedelta` also accepts. These arguments are passed into `timedelta`, and this is used as the expiry time for the cache

### Implementation example

```python
@imtfc_cache(seconds=30)
def wrapped_function():
  # Code here
```

## **method** : `wrapped_function.purge_cache()`

This clears the cache
