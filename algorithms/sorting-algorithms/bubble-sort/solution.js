// O(n^2)
function bubbleSort(arr) {
  let beenSwapped;

  do {
    beenSwapped = false;

    for (let j = 0; j < arr.length - 1; j++) {
      if (arr[j] > arr[j+1]) {
        const temp = arr[j+1];
        arr[j+1] = arr[j];
        arr[j] = temp;

        beenSwapped = true;
      }
    }
  } while (beenSwapped);
  // if no swaps during prev round, array is sorted;
  // break interation number ${i+1}

  return arr;
}

console.log(bubbleSort([-6, 20, 8, -2, 4]).toString() === "-6,-2,4,8,20");
console.log(bubbleSort([-6, 20, -2, 4, 8]).toString() === "-6,-2,4,8,20");