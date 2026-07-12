/**
 * @typedef {object} ExampleItem
 * @property {string} id Stable item identifier.
 * @property {string} displayName Human-readable name.
 */

/**
 * Normalizes and validates an item.
 *
 * Runtime validation remains required because JSDoc annotations do not validate
 * external values.
 *
 * @param {unknown} value Untrusted input value.
 * @returns {ExampleItem}
 * @throws {TypeError} When the input does not match the expected shape.
 */
export function parseExampleItem(value) {
  if (
    typeof value !== "object" ||
    value === null ||
    Array.isArray(value)
  ) {
    throw new TypeError("The item must be an object.");
  }

  const record = /** @type {Record<string, unknown>} */ (value);

  if (typeof record.id !== "string" || record.id.trim() === "") {
    throw new TypeError("The item id must be a non-empty string.");
  }

  if (
    typeof record.displayName !== "string" ||
    record.displayName.trim() === ""
  ) {
    throw new TypeError(
      "The item displayName must be a non-empty string.",
    );
  }

  return Object.freeze({
    id: record.id,
    displayName: record.displayName,
  });
}
