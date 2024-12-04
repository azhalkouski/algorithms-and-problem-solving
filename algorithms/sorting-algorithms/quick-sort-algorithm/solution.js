// Worst case - O(n^2) time
// Average case - O(nlogn) time
// O(n) space
function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[arr.length - 1];

  const leftArr = [];
  const rightArr = [];
  
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > pivot) {
      rightArr.push(arr[i]);
    } else {
      leftArr.push(arr[i]);
    }
  }

  return quickSort(leftArr).concat(pivot).concat(quickSort(rightArr));
}


console.log(quickSort([-6, 20, 8, -2, 4]).toString() === "-6,-2,4,8,20");
console.log(quickSort([-6, 20, -2, 4, 8]).toString() === "-6,-2,4,8,20");