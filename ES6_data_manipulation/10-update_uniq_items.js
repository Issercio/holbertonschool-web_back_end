export default function updateUniqueItems(groceries) {
  if (!(groceries instanceof Map)) {
    throw new Error('Cannot process');
  }

  groceries.forEach((quantity, item) => {
    if (quantity === 1) {
      groceries.set(item, 100);
    }
  });
}
