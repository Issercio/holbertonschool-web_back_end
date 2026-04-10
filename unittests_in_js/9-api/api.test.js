const request = require('request');
const { expect } = require('chai');

describe('Index page', function () {
  const url = 'http://localhost:7865/';

  it('should return status 200', function (done) {
    request.get(url, function (err, res, body) {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return correct message', function (done) {
    request.get(url, function (err, res, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', function () {
  const baseUrl = 'http://localhost:7865/cart/';

  it('should return status 200 and correct message for numeric id', function (done) {
    request.get(baseUrl + '12', function (err, res, body) {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return 404 for non-numeric id', function (done) {
    request.get(baseUrl + 'hello', function (err, res, body) {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });

  it('should return 404 for alphanumeric id', function (done) {
    request.get(baseUrl + '123abc', function (err, res, body) {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
