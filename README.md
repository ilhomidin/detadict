# detadict

__Goal:__ create dictionary that fully compatible with native python dictionary interface.

__Example:__
```python
from detadict import detadict

users = detadict()
users["John"] = {
  "id": 1,
  "sex": "male"
}
users["Katy"] = {
  "id": 2,
  "sex": "female"
}
```

__Requirements:__

🤦‍♂️ All you need to do is set the environment variable `DETA_PROJECT_KEY` with the Deta project key.

__Currently not supported__:

- Update of mutable values

```python
users["John"]["sex"] = "female"
print(users["John"])  # {"id": 1, "sex": "male"}
```

- `copy` and `setdefault` methods

```python
# raise NotImplementedError
users.copy()
users.setdefault("Bob", {})
```

__Installing__:
```bash
pip install detadict
```
