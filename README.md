# Javton

> A simple library to integrate JavaScript interpreter with Python

a library to integrate a JavaScript interpreter with Python from scratch involves several steps. The most common approach is to use an existing JavaScript runtime like Node.js or Duktape and interact with it from Python. Below is an example implementation using the subprocess module to interact with a Node.js process.

<img style="border-radius: 20px;" src="javton.png"/>

```python
from javton import javton_app

interpreter = javton_app()

result = interpreter.execute('1 + 1')
print(result)  # Output should be: {'result': 2}

result = interpreter.execute('const sum = (a, b) => a + b; sum(5, 3);')
print(result)  # Output should be: {'result': 8}
```
> JavaScript or syntax errors in your **input**: ‍‍‍‍`{'error': 'text is not defined'}`

### install

```bash
pip install javton
```

### Sample
sum 2 number from javascript:
> Terminal place
```js
const number1 = 15;
const number2 = 5;
number1 + number2
20
```
in python codebase
```python
from javton import javton_app

interpreter = javton_app()

result = interpreter.execute("const number1 = 15;const number2 = 5;number1+number2")
print(result)

interpreter.close()
```

> output: `{'result': 20}`‍‍
