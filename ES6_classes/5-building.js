export default class Building {
  constructor(sqft) {
    // Validate input is a number
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }

    // Store sqft with underscore prefix
    this._sqft = sqft;

    // Ensure that this class cannot be directly instantiated if it's an abstract class
    if (new.target === Building) {
      throw new TypeError('Cannot instantiate abstract class Building directly');
    }
  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }

  // Abstract method that must be implemented by subclasses
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
