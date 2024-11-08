export default function cleanSet(set, startString) {
  if (!startString) {
    return '';
  }
  const array = Array.from(set);
  const filteredArray = array.filter((string) => string.startsWith(startString));
  return filteredArray.join('-');
}
