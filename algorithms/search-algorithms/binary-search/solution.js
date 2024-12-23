// O(logn) time
function binarySearch(arr, t) {
  let left = 0;
  let right = arr.length -1;

  while (left <= right) {
    const middle = Math.floor((right + left) / 2);

    if (arr[middle] === t) {
      return middle;
    }

    if ( t < arr[middle]) {
      right = middle - 1;
    } else {
      left = middle + 1;
    }
  }

  return -1;
}


console.log(binarySearch([-5, 2, 4, 6, 10], 10) === 4);
console.log(binarySearch([-5, 2, 4, 6, 10], 6) === 3);
console.log(binarySearch([-5, 2, 4, 6, 10], 20) === -1);
console.log(" ");


// O(logn)
function recursiveBinarySearch(arr, t) {
  return search(arr, t, 0, arr.length - 1);
}

function search(arr, t, left, right) {
  if (left > right) {
    return -1;
  }

  const middle = Math.floor((left + right) / 2);

  if (arr[middle] === t) {
    return middle;
  }

  if (t < arr[middle]) {
    right = middle - 1;
  } else {
    left = middle + 1;
  }

  return search(arr, t, left, right);
}

console.log(recursiveBinarySearch([-5, 2, 4, 6, 10], 10) === 4);
console.log(recursiveBinarySearch([-5, 2, 4, 6, 10], 6) === 3);
console.log(recursiveBinarySearch([-5, 2, 4, 6, 10], 20) === -1);