/**
 * O(n) Time - O(n)
 * O(n) Space - O(n)
 * @param {number} n 
 */
function fibonacci(n) {
  if (n == 0) {
    return [];
  }

  if (n == 1) {
    return [0];
  }

  if (n == 2) {
    return [0, 1];
  }

  const sequence = [0, 1];
  for ( let i = 2; i < n; i++) {
    sequence[i] = sequence[i - 1] + sequence[i - 2];
  }

  return sequence;
}

console.log(fibonacci(0).toString() === "");
console.log(fibonacci(1).toString() === "0");
console.log(fibonacci(2).toString() === "0,1");
console.log(fibonacci(3).toString() === "0,1,1");
console.log(fibonacci(7).toString() === "0,1,1,2,3,5,8");