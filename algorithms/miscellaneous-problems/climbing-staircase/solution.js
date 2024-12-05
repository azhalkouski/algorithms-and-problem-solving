/**
 * O(n) time
 * @param {number} n - length of the staircase
 */
function waysToClimbStaircase(n) {
  const ways = [1, 2];

  for (let i = 2; i < n; i++) {
    ways[i] = ways[i - 1] + ways[i - 2];
  }

  return ways[n - 1];
}

console.log(waysToClimbStaircase(1) === 1);
console.log(waysToClimbStaircase(2) === 2);
console.log(waysToClimbStaircase(3) === 3);
console.log(waysToClimbStaircase(4) === 5);
console.log(waysToClimbStaircase(5) === 8);
console.log(waysToClimbStaircase(6) === 13);