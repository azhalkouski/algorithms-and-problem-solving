# algorithms-and-problem-solving

# Algorithm analysis
The absolute running time of an algorithm cannot be predicted, since it depends on
a number of factors.

- Programming language used to implement the algorithm
- The computer the program runs on.
- Other programs running at the same time
- Quality of the operating system
- Other factors.

We evaluate the performance of an algorithm __in terms of its input size__.

__Time complexity__ - Amount of time taken by an algorithm to run, as a function
of input size.
__Space complexity__ - Amount of memory taken by an algorithm to run, as a function
of input size.

If your app needs to be very quick and has plenty of memory to work with, you don't
have to worry about space complexity.

If you have very little memory to work with, you should pick a solution that is
relatively slower but needs less space.

## How to represent compolexity?
Asymptotic notations
- Mathematical tools to represent time and space complexity
1. Big-O Notation - Worst case complexity
2. Omega Notation - Best case comlexity
3. Theta Notation - Average case complexity

Basically, we are interested in Big-O notation becasue the worst case scenario is
something that gets noticed when things start to go not so well/fast or even crash
wheres when the things go well no users are actually concerned about how the system
works internally. So we want to understand how an algoritms performs in the worst
case scenario and how it affects the system's robustness and performance,
and the overall user experience.

## Big-O Notation
The Big-O Notation has two important characteristics
1. It is expressed in terms of the input
2. It focuses on the bigger picture without getting caught up in the minute details like
  constant factors.

### Big-O Time Complexity
```
function summation(n) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}
```
The program above has three steps to execute:
- let sum = 0; // executed once
- sum += i; // executed n times
- return sum; // executed once

Thus the overall time complexity is __n + 2__. We can drop that number `2` since `+2`
becomes insignificant when n = 1'000'000. Thus we say that the time complexity of
the above program is __O(n)__ which is called __linear complexity__.

Most of the time whenever you see a for loop you can safely say that the time
complexity is at least linear.

Here the same problem is solved with a __constant time complexity__:
```
function summation(n) {
  return (n * (n + 1)) / 2;
}
```
No matter how big `n` is, the algorithm will execute one line of code only once.
__O(1)__ - Constant

Other complexities:
__O(n^2)__ - quadratic. Example - two nested loops. If you have a complexity of
`3n^2 + 5n + 1` you can drop it to `3n^2` because it is the most significant part.
`3n^100'000` is so large that `5n` becomes insignificant.

__O(n^3)__ - Cubic. Example - three nested loops.
__O(logn)__ - Logarithmic. Input size is reduced by half on each iteration.


### Big-O Space Complexity
__O(1) - Constant.__ If the algorithm does not need extra memory, or the memory needed
does not depend on the input size. Example - sorting algorithms which sort withing
the array without untilizing additional arrays.
__O(n) - Linear.__ Extra space needed grows as the input size grows.
__O(logn) - Logarithmic__. Extra space needed grows but not at the same rate as the
input size

__Quadratic space complexity__ is something you should avoid!


__O(1)__ - Excellent
__O(logn)__ - Good
__O(n)__ - Fair
__O(nlogn)__ - Bad
__O(n^2)__ - Horrible


### General recommendation
Don't lose sight of the big picture. If you have a function which is executed 1'000
times per minute, sure, go agead and optimize it. But if the function is called like
once, rather than writing clever code, write code taht is simple to read and maintain.