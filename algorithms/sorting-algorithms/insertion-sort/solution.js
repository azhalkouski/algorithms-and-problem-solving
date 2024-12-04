// O(n^2)
function insertionSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    const numberToInsert = arr[i];
    let lastSortedIdx = i - 1;

    while (lastSortedIdx >= 0 && arr[lastSortedIdx] > numberToInsert) {
      arr[lastSortedIdx + 1] = arr[lastSortedIdx];
      lastSortedIdx -= 1;
    }

    arr[lastSortedIdx + 1] = numberToInsert;
  }

  return arr;
}


console.log(insertionSort([-6, 20, 8, -2, 4]).toString() === "-6,-2,4,8,20");
console.log(insertionSort([-6, 20, -2, 4, 8]).toString() === "-6,-2,4,8,20");