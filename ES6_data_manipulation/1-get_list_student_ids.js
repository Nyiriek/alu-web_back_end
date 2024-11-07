export default function getListStudentIds(arrayOfObjects) {
  const array = [];
  if (Array.isArray(arrayOfObjects)) {
    return arrayOfObjects.map((student) => student.id);
  }
  return array;
}
