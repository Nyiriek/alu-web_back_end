export default function setFromArray(arrayOfObjects) {
  const array = [];
  if (Array.isArray(arrayOfObjects)) {
    return new Set(arrayOfObjects);
  }
  return array;
}
