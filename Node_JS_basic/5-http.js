const http = require('http');

const args = process.argv.slice(2);
const countStudents = require('./3-read_file_async');

const DATABASE = args[0];

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer(async (request, response) => {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');

  const { url } = request;

  if (url === '/') {
    response.write('Hello Holberton School!');
  } else if (url === '/students') {
    response.write('This is the list of our students\n');
    try {
      const students = await countStudents(DATABASE);
      response.end(`${students.join('\n')}`);
    } catch (error) {
      response.end(error.message);
    }
  }
  response.statusCode = 404;
  response.end();
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
