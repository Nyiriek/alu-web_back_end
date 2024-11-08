export default function getStudentsByLocation(arrayOfObjects, city) {
  const array = [];
  if (Array.isArray(arrayOfObjects) && typeof city === 'string') {
    return arrayOfObjects.filter((student) => student.location === city);
  }
  return array;
}
