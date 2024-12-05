// O(nlogn)
function mergeSort(arr) {
  if (arr.length < 2) {
    return arr;
  }

  const mid = Math.floor(arr.length / 2);
  const leftArr = arr.slice(0, mid);
  const rightArr = arr.slice(mid);

  return merge(mergeSort(leftArr), mergeSort(rightArr));
}

function merge(sortedLeft, sortedRight) {
  const sorted = [];

  while (sortedLeft.length && sortedRight.length) {
    if (sortedLeft[0] <= sortedRight[0]) {
      sorted.push(sortedLeft.shift());
    } else {
      sorted.push(sortedRight.shift());
    }
  }

  return [...sorted, ...sortedLeft, ...sortedRight];
}


console.log(mergeSort([-6, 20, 8, -2, 4]).toString() === "-6,-2,4,8,20");
console.log(mergeSort([-6, 20, -2, 4, 8]).toString() === "-6,-2,4,8,20");
console.log(mergeSort([-6, 20, -2, 4, 7, 8]).toString() === "-6,-2,4,7,8,20");
console.log(mergeSort([-6, 20, 8, -2, 4, 7, 8]).toString() === "-6,-2,4,7,8,8,20");