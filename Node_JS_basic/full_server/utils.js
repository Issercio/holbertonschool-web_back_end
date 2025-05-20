import fs from 'fs/promises';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8')
    .then((data) => {
      const students = {};
      const lines = data.trim().split('\n');
      const noHeader = lines.slice(1);

      if (noHeader.length === 0) {
        reject(new Error('Cannot load the database'));
      }

      noHeader.forEach((line) => {
        const [firstName, , , field] = line.split(',');
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstName);
      });

      resolve(students);
    })
    .catch(() => reject(new Error('Cannot load the database')));
});

export default readDatabase;
