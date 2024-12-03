/**
 * O(n) Time
 * @param {number} n - natural number
 */
function isPrime_1(n) {
  if (n < 2) {
    // don't forget about negative numbers
    // a prime number is a natural number GREATER THAN 1
    return false;
  }

  for (let i = 2; i < n; i++) {
    if (n % i === 0) {
      return false;
    }
  }

  return true;
}



/**
 * O(n) Time
 * @param {number} n - natural number
 */
function isPrime_2(n) {
  if (n < 2) {
    return false;
  }

  // a mathematical optimization. The point is that 25 = 5 * 5. 5 and 5 make a pair 
  // of maximums. If one numer is going to be greater than 5, the other number MUST and
  // IS less then 5. So, it's enough to go up to the Math.sqrt(n) and it doesn't make
  // sense to go beyond.
  const sqrt = Math.sqrt(n);
  let i = 2;

  while (i <= sqrt) {
    if (n  % i === 0) {
      return false;
    }

    i++;
  }

  return true;
}

console.log(isPrime_1(1));
console.log(isPrime_1(5));
console.log(isPrime_1(4));
console.log("");
console.log(isPrime_2(1));
console.log(isPrime_2(5));
console.log(isPrime_2(4));
