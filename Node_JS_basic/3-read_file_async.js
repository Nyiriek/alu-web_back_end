const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }
      const res = [];
      let message;

      const cont = data.toString().split('\n');
      let students = cont.filter((str) => str);

      students = students.map((str) => str.split(','));

      const NUMBER_OF_STUDENTS = students.length ? students.length - 1 : 0;
      message = `Number_od_students: ${NUMBER_OF_STUDENTS}`;
      console.log(message);
      res.push(message);

      const fields = {};
      for (const i in students) {
        if (i !== 0) {
          if (!fields[students[i][3]]) fields[students[i][3]] = [];

          fields[students[i][3]].push(students[i][0]);
        }
      }

      delete fields.field;

      for (const key of Object.keys(fields)) {
        message = `Number of students in ${key}: ${
          fields[key].length
        }. List: ${fields[key].join(', ')}`;

        console.log(message);

        res.push(message);
      }
      resolve(res);
    });
  });
}

module.exports = countStudents;
