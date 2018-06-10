**The library `imc` contains one class: `cache`**

---

**class**

`cache (  getFunction, expiryDelta )`

`getFunction` must be a function. The return value of this is what is cached

`expiryDelta` must be an `imc.expiryDelta` object. This is the amount of time that the data should be cached for before being renewed

---

**method**

`cache.get`

Returns the cached return value from `getFunction`
