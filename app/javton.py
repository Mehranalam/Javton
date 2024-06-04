import subprocess
import json

class javton_app:
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

interpreter = javton()

result = interpreter.execute('1 + 1')
print(result)

interpreter.close()