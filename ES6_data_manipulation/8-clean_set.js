export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  return Array.from(set)
    .filter((value) => value.startsWith(startString) && value !== startString)
    .map((value) => value.slice(startString.length))
    .join('-');
}
