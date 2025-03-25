export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') {
      throw new TypeError('size must be a number');
    }
    if (typeof location !== 'string') {
      throw new TypeError('location must be a string');
    }
    this._size = size;
    this._location = location;
  }

  // Getter for 'size'
  get size() {
    return this._size;
  }

  // Getter for 'location'
  get location() {
    return this._location;
  }

  // Override valueOf method to return the size when cast to a Number
  valueOf() {
    return this._size;
  }

  // Override toString method to return the location when cast to a String
  toString() {
    return this._location;
  }
}
