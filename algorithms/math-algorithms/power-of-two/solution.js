/**
 * O(logn) time
 * O(1) space
 * @param {number} n positive integer
 */
function isPowerOfTwo(n) {
  // zero is NOT a positive integer
  if (n === 1 || n === 2) {
    // 2^0 is 1
    // 2^1 is 2
    return true;
  }

  while(n >= 2) {
    if (n % 2 !== 0) {
      return false;
    } else {
      n = n / 2;
    }
  }

  return true;
}

console.log(isPowerOfTwo(1) === true);
console.log(isPowerOfTwo(2) === true);
console.log(isPowerOfTwo(5) === false);
console.log(isPowerOfTwo(8) === true);
console.log(isPowerOfTwo(9) === false);