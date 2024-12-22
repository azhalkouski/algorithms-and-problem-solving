var majorityElement = function(nums) {
  // potential candidate
  let candidate = null;
  // votesCount
  let count = 0;

  for (let i = 0; i < nums.length; i++) {
      if (count === 0) {
          // if current count equals 0 it means we don't see a potential candidate yet
          candidate = nums[i];
          count++;
      } else if (nums[i] !== candidate) {
          count--;
      } else {
          count++;
      }
  }

  // step 2: make sure the candidate is the majority element
  let candidateVotesCount = 0;
  for (let i = 0; i < nums.length; i++) {
      if (nums[i] === candidate) {
          candidateVotesCount++;
      }
  }

  // now let's make sure that the candidate is the majority
  // majority means at least half the voters votes for the candidate
  const isMajorityCandidate = candidateVotesCount >= Math.round(nums.length / 2)
    ? true
    : false;

  return isMajorityCandidate ? candidate : null;
}

console.log(majorityElement([1,2,3,4,3,2,1,2,1]) === null);
console.log(majorityElement([1,2,3,4,3,2,1,2,1,1]) === null);
console.log(majorityElement([1,2,3,4,3,2,1,2,1,2]) === null);
console.log(majorityElement([3,2,3]) === 3);
console.log(majorityElement([1,2,3,1,1,1]) === 1);