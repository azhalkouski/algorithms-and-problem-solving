__Problem__
Given an array of integers, sort the array.

1. Virtually split the array into a sorted and an unsorted parts.
2. Assume that the first element is already sorted and remaining elements are unsorted.
3. Select an unsorted element and compare with all elements in the sorted part.
4. If the elements in the sorted part are smaller than the selected element, proceed to
  the next element in the unsorted part.
5. Insert the selected element at the right index.
6. Repeat till all the unsorted elements are placed in the right order.