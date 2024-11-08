export default function getStudentIdsSum(arrayOfObjects) {
  const array = [];
  if (Array.isArray(arrayOfObjects)) {
    return arrayOfObjects.reduce((acc, student) => acc + student.id, 0);
  }
  return array;
}
