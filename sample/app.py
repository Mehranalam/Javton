from javton import javton_app

interpreter = javton_app()

result = interpreter.execute('1 + 1')
print(result)  # Output should be: {'result': 2}

result = interpreter.execute('const sum = (a, b) => a + b; sum(5, 3);')
print(result)  # Output should be: {'result': 8}

result = interpreter.execute('invalidCode()')
print(result)  # Output should be: {'error': 'invalidCode is not defined'}

interpreter.close()