**The module `imtfc` contains one class which is a function decorator: `cache`**

---

**class**

`@imtfc_cache (  *args, **kwargs )`

`@imtfc_cache` accepts any arguments that `datetime.timedelta` also accepts. These arguments are passed into `timedelta`, and this is used as the expiry time for the cache
