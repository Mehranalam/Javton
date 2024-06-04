# Javton

> A simple library to integrate JavaScript interpreter with Python

a library to integrate a JavaScript interpreter with Python from scratch involves several steps. The most common approach is to use an existing JavaScript runtime like Node.js or Duktape and interact with it from Python. Below is an example implementation using the subprocess module to interact with a Node.js process.


```python
from javton import javton_app

interpreter = javton_app()

result = interpreter.execute('1 + 1')
print(result)  # Output should be: {'result': 2}

result = interpreter.execute('const sum = (a, b) => a + b; sum(5, 3);')
print(result)  # Output should be: {'result': 8}
```

#### install

```bash
pip install javton
```
