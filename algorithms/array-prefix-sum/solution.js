/**
 * @param {number[]} nums
 * @return {number[]}
 */

// THIS IS NOT PREFIX SUM
// O(n^2) time
// O(1) extra space complexity
var productExceptSelf_1 = function(nums) {
    return nums.map((el, i) => {
        return nums.reduce((acc, elem, idx) => {
            return i !== idx ? acc * elem : acc;
        }, 1);
    });
};


// THIS IS PREFIX SUM
// O(n) time
var productExceptSelf_2 = function(nums) {
  // `prefix sum` altorithm applied
  const answer = [];
  const prefix = [];
  const suffix = [];
  const numsLength = nums.length;

  let i = 1;
  let j = nums.length - 2;

  prefix[0] = 1;
  suffix[j+1] = 1;

  while (i <= numsLength - 1 && j >= 0) {
      prefix[i] = nums[i - 1] * prefix[i - 1];
      suffix[j] = nums[j + 1] * suffix[j + 1];

      i++;
      j--;
  }

  for (let i = 0; i < numsLength; i++) {
      answer[i] = prefix[i] * suffix[i];
  }

  return answer;
}

console.log(productExceptSelf_1([1,2,3,4]).toString() === '24,12,8,6');
console.log(productExceptSelf_1([-1,1,0,-3,3]).toString() === '0,0,9,0,0');

console.log(productExceptSelf_2([1,2,3,4]).toString() === '24,12,8,6');
console.log(productExceptSelf_2([-1,1,0,-3,3]).toString() === '0,0,9,0,0');