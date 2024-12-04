/**
 * O(n) time
 * @param {number[]} arr - input array
 * @param {number} t - target element
 * @returns index of target element, -1 otherwise
 */
function linearSearch(arr, t) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === t) {
      return i;
    }
  }

  return -1;
}

console.log(linearSearch([-5, 2, 10, 4, 6], 10) === 2);
console.log(linearSearch([-5, 2, 10, 4, 6], 6) === 4);
console.log(linearSearch([-5, 2, 10, 4, 6], 11) === -1);
