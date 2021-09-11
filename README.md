```python
from detadict import detadict

# simply create, without any configuration in the code
d = detadict()

# primitive types
d["fizz"] = "buzz"
d["two"] = 2
d["one_point_two"] = 1.2
d["true"] = True

# mutable lists support
d["ids"] = []
d["ids"].append(1)
d["ids"]  # [1]

# fully dict compatiblie
d.setdefault("users", {})
d["users"]["John"] = "Libovsky"
d["users"]  # {"John", "Libovsky"}
```
