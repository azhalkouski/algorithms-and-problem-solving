// given an integer `n`, find the factorial of that integer
// 5! = 1 * 2 * 3 * 4 * 5

// O(n) time
function recursiveFactorial(n) {
  // factorial of zero is 1
  if (n === 0) {
    return 1;
  }
  return n * recursiveFactorial(n - 1);
}

console.log(recursiveFactorial(0) === 1);
console.log(recursiveFactorial(1) === 1);
console.log(recursiveFactorial(2) === 2);
console.log(recursiveFactorial(3) === 6);
console.log(recursiveFactorial(4) === 24);
console.log(recursiveFactorial(5) === 120);
