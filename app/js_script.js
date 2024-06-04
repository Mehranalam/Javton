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

/*
This script uses Node.js to evaluate JavaScript code. 
It reads the code from stdin and writes the result or error to stdout.
*/