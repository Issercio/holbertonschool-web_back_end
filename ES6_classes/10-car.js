const cloneSymbol = Symbol('cloneCar');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Clone method
  [cloneSymbol]() {
    return new this.constructor(this._brand, this._motor, this._color);
  }

  // We can provide a getter for cloneCar
  cloneCar() {
    return this[cloneSymbol](); // Use the Symbol to call the method
  }
}
