// find the n'th Fibonacci number

// O(n^2) time; every call produces two more calls
function recursiveFibonacci(n) {
  if (n < 2) {
    // becase the first two numbers of the Fibonacci sequence are 0 and 1
    return n;
  }
  return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2);
};

console.log(recursiveFibonacci(0));
console.log(recursiveFibonacci(1));
console.log(recursiveFibonacci(6));