# Javton

Creating a library to integrate a JavaScript interpreter with Python from scratch involves several steps. The most common approach is to use an existing JavaScript runtime like Node.js or Duktape and interact with it from Python. Below is an example implementation using the subprocess module to interact with a Node.js process.

### Step 1: Set Up the Project Structure

Create a directory for your library. Inside it, create the following files:

```
js_interpreter/
|-- __init__.py
|-- interpreter.py
|-- js_script.js
```

### Step 2: Create a JavaScript File

In `js_script.js`, write a simple JavaScript script that can evaluate code passed to it.

```javascript
// js_script.js
const vm = require('vm');

process.stdin.on('data', (data) => {
  const code = data.toString();
  try {
    const result = vm.runInNewContext(code);
    process.stdout.write(JSON.stringify({ result }) + '\n');
  } catch (error) {
    process.stdout.write(JSON.stringify({ error: error.message }) + '\n');
  }
});
```

This script reads JavaScript code from stdin, evaluates it using the `vm` module, and writes the result to stdout.

### Step 3: Create the Python Wrapper

In `interpreter.py`, create a Python class that interacts with this Node.js script.

```python
import subprocess
import json

class JSInterpreter:
    def __init__(self, node_path='node', script_path='js_script.js'):
        self.node_path = node_path
        self.script_path = script_path
        self.process = subprocess.Popen(
            [self.node_path, self.script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

    def execute(self, code):
        self.process.stdin.write(code + '\n')
        self.process.stdin.flush()
        result = self.process.stdout.readline()
        return json.loads(result)

    def close(self):
        self.process.terminate()
        self.process.wait()

# Create an instance of JSInterpreter
interpreter = JSInterpreter()

# Test the execution of a JS code
result = interpreter.execute('1 + 1')
print(result)  # Output should be: {'result': 2}

# Close the interpreter process
interpreter.close()
```

### Step 4: Expose the Library

In `__init__.py`, import the necessary components to expose your library's functionality.

```python
from .interpreter.py import JSInterpreter
```

### Step 5: Usage Example

Create a separate script to use your library.

```python
# example_usage.py
from js_interpreter import JSInterpreter

interpreter = JSInterpreter()

# Execute some JavaScript code
result = interpreter.execute('1 + 1')
print(result)  # Output should be: {'result': 2}

# Execute more complex code
result = interpreter.execute('const sum = (a, b) => a + b; sum(5, 3);')
print(result)  # Output should be: {'result': 8}

# Handle error case
result = interpreter.execute('invalidCode()')
print(result)  # Output should be: {'error': 'invalidCode is not defined'}

# Close the interpreter process
interpreter.close()
```

### Step 6: Package and Distribute

If you want to distribute your library, you can create a `setup.py` file.

```python
from setuptools import setup, find_packages

setup(
    name='js_interpreter',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    description='A simple library to integrate JavaScript interpreter with Python',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/js_interpreter',
)
```

### Explanation

1. **JavaScript Script (`js_script.js`)**: This script uses Node.js to evaluate JavaScript code. It reads the code from stdin and writes the result or error to stdout.
2. **Python Wrapper (`interpreter.py`)**: This Python class interacts with the JavaScript script. It sends JavaScript code to the script's stdin and reads the result from stdout.
3. **Initialization (`__init__.py`)**: Exposes the `JSInterpreter` class for use.
4. **Usage Example**: Demonstrates how to use the `JSInterpreter` class to evaluate JavaScript code.

This setup allows you to integrate a JavaScript interpreter with Python without using any external libraries like `execjs`. Instead, it leverages Node.js to evaluate JavaScript code.
