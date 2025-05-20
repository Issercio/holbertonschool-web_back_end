const http = require('http');
const fs = require('fs');

const args = process.argv;
const dbPath = args[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      const headers = lines[0].split(',');
      const fieldIndex = headers.indexOf('field');

      const students = {};
      const validLines = lines.slice(1).filter((line) => line.trim() !== '');

      for (const line of validLines) {
        const values = line.split(',');
        const field = values[fieldIndex];
        const name = values[0];

        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(name);
      }

      let output = `Number of students: ${validLines.length}`;
      for (const [field, names] of Object.entries(students)) {
        output += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
      }

      resolve(output);
    });
  });
}

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    countStudents(dbPath)
      .then((output) => {
        res.end(`This is the list of our students\n${output}`);
      })
      .catch(() => {
        res.end('This is the list of our students\nCannot load the database');
      });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not found');
  }
});

app.listen(1245);
module.exports = app;
