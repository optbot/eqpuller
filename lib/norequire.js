(function() {
  'use strict';
  module.exports = throwError;

  function throwError() {
    var msg = 'eqpuller service should not be used in require statement';
    throw new Error(msg);
  }

  throwError();
})();
