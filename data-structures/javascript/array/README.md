An array is an __ordered__ collection of values.

Insert / remove at end - O(1)
Insert / remove at beginning - O(n) - becasue all indexes have to be reset.
Access - O(1)
Search O(n) - as the element can be the last in the array.

Puch / pop - O(1)
Shift / unshift / concat / slice / splice - O(n)
forEach / map / filter / reduce - O(n)

If while solving a problem you have a forEach loop and its callback has another
for loop inside it, you will have quadratic complexity, which is __bad__.