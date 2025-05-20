process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Create readable stream from stdin
process.stdin.on('data', (data) => {
  // Convert Buffer to string and remove trailing newline characters
  const name = data.toString().trim();
  process.stdout.write(`Your name is: ${name}\n`);

  // If input is coming from a pipe rather than terminal
  if (!process.stdin.isTTY) {
    process.stdout.write('This important software is now closing\n');
    process.exit();
  }
});

// Handle end of input when piped
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
  process.exit();
});
