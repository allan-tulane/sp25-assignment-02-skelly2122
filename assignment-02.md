# CMPS 2200 Assignment 2

**Name:** Samuel Kelly

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior
in practice. As with previous
assignments, some of of your answers will go in `main.py` and `test_main.py`. You
should feel free to edit this file with your answers; for handwritten
work please scan your work and submit a PDF titled `assignment-02.pdf`
and push to your github repository.


## Part 1. Asymptotic Analysis

Derive asymptotic upper bounds of work for each recurrence below.

* $W(n)=2W(n/3)+1$

At each level, we split into 2 subproblems of size n/3
Work at root: 1
Level 1 has 2 nodes, each doing work 1, total: 2
Level 2 has 2² = 4 nodes, each working on size n/3², total: 4
At level i, we have 2^i nodes each doing work 1, total: 2^i
Tree height: When n/3^h = 1, so h = log₃(n)
Total nodes: 1 + 2 + 2² + ... + 2^(log₃(n)) ≈ 2^(log₃(n)+1) ≈ 2·n^(log₃(2))
Therefore, W(n) = Θ(n^(log₃(2))) = Θ(n^0.631)
The work is dominated by the leaf level since 2 > 3^0
 
* $W(n)=5W(n/4)+n$

Work at root: n
Level 1: 5 nodes, each doing n/4 work, total: 5n/4
Level i: 5^i nodes, each doing n/4^i work, total: 5^i·(n/4^i) = n·(5/4)^i
Since (5/4) > 1, work increases with each level
When n/4^h = 1, height h = log₄(n)
Final level has most work: n·(5/4)^(log₄(n)) = n·5^(log₄(n))/4^(log₄(n)) = n·5^(log₄(n))/n = 5^(log₄(n)) = n^(log₄(5))
Therefore, W(n) = Θ(n^(log₄(5))) = Θ(n^1.161)

* $W(n)=7W(n/7)+n$

Work at root: n
Level i: 7^i nodes, each doing n/7^i work, total: n
Each level does same amount of work
Height: log₇(n) levels
Total work: n·log₇(n) = Θ(n log n)

* $W(n)=9W(n/3)+n^2$

Work at root: n²
Level i: 9^i nodes, each doing (n/3^i)² work, total: 9^i·(n/3^i)² = n²·(9/3²)^i = n²·(1)^i = n²
All levels have equal work n²
Height: log₃(n) levels
Total work: n²·log₃(n) = Θ(n² log n)

* $W(n)=8W(n/2)+n^3$

Work at root: n³
Level i: 8^i nodes, each doing (n/2^i)³ work, total: 8^i·(n/2^i)³ = n³·(8/2³)^i = n³·(8/8)^i = n³
Each level does same work n³
Height: log₂(n) levels
Total work: n³·log₂(n) = Θ(n³ log n)


* $W(n)=49W(n/25)+n^{3/2}\log n$

Work at root: n^(3/2)·log n
Level i: 49^i nodes, each doing (n/25^i)^(3/2)·log(n/25^i) work
Simplifying: 49^i·(n/25^i)^(3/2)·log(n/25^i)
≈ n^(3/2)·(49/25^(3/2))^i·(log n - i·log 25)
49/25^(3/2) = 49/125 < 1, so work decreases with depth
Root work dominates
Therefore, W(n) = Θ(n^(3/2) log n)



* $W(n)=W(n-1)+2$*
 
Linear decrease in problem size, not branching
Work at each level: 2
Levels from n to 1, so n levels total
Total work: 2n = Θ(n)

* $W(n)= W(n-1)+n^c$, with $c\geq 1$

Work at level i (where we're solving for n-i): (n-i)^c
Total work: sum[(n-i)^c] for i from 0 to n-1
This is dominated by the largest terms
Sum of k^c from k=1 to n is Θ(n^(c+1))
Therefore, W(n) = Θ(n^(c+1))

* $W(n)=W(\sqrt{n})+1$

This creates a drastically shrinking problem size
Root work: 1
Level 1 (sqrt(n)): 1
Level 2 (sqrt(sqrt(n)) = n^(1/4)): 1
Level i: problem size n^(1/2^i)
We reach size 2 when n^(1/2^i) = 2, or 2^i = log(log n)
Total levels: log(log n)
Each level does work 1
Therefore, W(n) = Θ(log log n)


## Part 2. Algorithm Comparison

Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
    
  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
    
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?


Algorithm A\mathcal{A}
A: W(n) = 5W(n/2) + n


Root work: n
Level i: 5^i nodes, each with work (n/2^i), total: 5^i·(n/2^i) = n·(5/2)^i
Since 5/2 > 1, work increases with depth
Height: log₂(n)
Work is dominated by leaf level: n·(5/2)^(log₂(n)) = n·5^(log₂(n))/2^(log₂(n)) = n·5^(log₂(n))/n = 5^(log₂(n)) = n^(log₂(5))
Therefore, W(n) = Θ(n^(log₂(5))) = Θ(n^2.32)


Algorithm B\mathcal{B}
B: W(n) = 2W(n-1) + 1


This creates a wide tree with linear depth
Root work: 1
Level 1: 2 nodes, each with problem size n-1, work 2
Level 2: 2² = 4 nodes, each with problem size n-2, work 4
Level i: 2^i nodes, each doing work 1, total work 2^i
Height: n levels
Total work dominated by deepest level: 2^n
Therefore, W(n) = Θ(2^n)


Algorithm C\mathcal{C}
C: W(n) = 9W(n/3) + n²


Root work: n²
Level i: 9^i nodes, each with work (n/3^i)², total: 9^i·(n/3^i)² = n²·(9/9)^i = n²
Each level does work n²
Height: log₃(n) levels
Total work: n²·log₃(n) = Θ(n² log n)



I would choose Algorithm C\mathcal{C}
C because:


Algorithm A\mathcal{A}
A has complexity Θ(n^2.32), which grows faster than C\mathcal{C}
C's Θ(n² log n)

Algorithm B\mathcal{B}
B has exponential complexity Θ(2^n), which is impractical for all but the smallest inputs

While C\mathcal{C}
C has the n² log n factor, it grows more slowly than n^2.32 and much more slowly than 2^n

## Part 3: Parenthesis Matching

A common task of compilers is to ensure that parentheses are matched. That is, each open parenthesis is followed at some point by a closed parenthesis. Furthermore, a closed parenthesis can only appear if there is a corresponding open parenthesis before it. So, the following are valid:

- `( ( a ) b )`
- `a () b ( c ( d ) )`

but these are invalid:

- `( ( a )`
- `(a ) ) b (`

Below, we'll solve this problem three different ways, using iterate, scan, and divide and conquer.

**3a. iterative solution** Implement `parens_match_iterative`, a solution to this problem using the `iterate` function. **Hint**: consider using a single counter variable to keep track of whether there are more open or closed parentheses. How can you update this value while iterating from left to right through the input? What must be true of this value at each step for the parentheses to be matched? To complete this, complete the `parens_update` function and the `parens_match_iterative` function. The `parens_update` function will be called in combination with `iterate` inside `parens_match_iterative`. Test your implementation with `test_parens_match_iterative`.


.  
. 



**3b.** What are the recurrences for the Work and Span of this solution? What are their Big Oh solutions?

The iterative solution processes each element once and updates a single counter.

Work analysis:

Each element requires constant work to process, and we have n elements
Recurrence: W(n) = n × O(1)
Big Oh solution: W(n) = Θ(n)


Span analysis:

The operations are inherently sequential - we must process element i before element i+1
Recurrence: S(n) = n × O(1)
Big Oh solution: S(n) = Θ(n)



The iterative approach has linear work and linear span, making it efficient for sequential processing but not optimal for parallel execution.


**3c. scan solution** Implement `parens_match_scan` a solution to this problem using `scan`. **Hint**: We have given you the function `paren_map` which maps `(` to `1`, `)` to `-1` and everything else to `0`. How can you pass this function to `scan` to solve the problem? You may also find the `min_f` function useful here. Implement `parens_match_scan` and test with `test_parens_match_scan`

.  
. 



**3d.** Assume that any `map`s are done in parallel, and that we use the efficient implementation of `scan` from class. What are the recurrences for the Work and Span of this solution? 

For the scan solution:

Work analysis:

Mapping each element to 1, -1, or 0: W_map(n) = Θ(n)
Efficient scan on n elements: W_scan(n) = Θ(n)
Final reduction: W_reduce(n) = Θ(n)
Total work: W(n) = W_map(n) + W_scan(n) + W_reduce(n) = Θ(n)


Span analysis:

Mapping in parallel: S_map(n) = Θ(1)
Efficient scan creates a balanced binary tree with height log n: S_scan(n) = Θ(log n)
Reduction for minimum: S_reduce(n) = Θ(log n)
Total span: S(n) = S_map(n) + S_scan(n) + S_reduce(n) = Θ(log n)


**3e. divide and conquer solution** Implement `parens_match_dc_helper`, a divide and conquer solution to the problem. A key observation is that we *cannot* simply solve each subproblem using the above solutions and combine the results. E.g., consider '((()))', which would be split into '(((' and ')))', neither of which is matched. Yet, the whole input is matched. Instead, we'll have to keep track of two numbers: the number of unmatched right parentheses (R), and the number of unmatched left parentheses (L). `parens_match_dc_helper` returns a tuple (R,L). So, if the input is just '(', then `parens_match_dc_helper` returns (0,1), indicating that there is 1 unmatched left parens and 0 unmatched right parens. Analogously, if the input is just ')', then the result should be (1,0). The main difficulty is deciding how to merge the returned values for the two recursive calls. E.g., if (i,j) is the result for the left half of the list, and (k,l) is the output of the right half of the list, how can we compute the proper return value (R,L) using only i,j,k,l? Try a few example inputs to guide your solution, then test with `test_parens_match_dc_helper`.



.  
. 





**3f.** Assuming any recursive calls are done in parallel, what are the recurrences for the Work and Span of this solution? What are their Big Oh solutions?

Work analysis:

Recursively divides the list into halves
Recurrence relation: W(n) = 2W(n/2) + Θ(1)
Looking at the tree:

Root work: Θ(1)
Level i: 2^i nodes, each doing Θ(1) work, total: Θ(2^i)
Height: log₂(n)
Total work: Θ(1) + Θ(2) + Θ(4) + ... + Θ(2^(log₂(n))) = Θ(2^(log₂(n)+1)) = Θ(n)


Big Oh solution: W(n) = Θ(n)


Span analysis:

With parallel recursive calls:
Recurrence relation: S(n) = S(n/2) + Θ(1)
Each level adds constant work
Height: log₂(n)
Total span: Θ(log n)
Big Oh solution: S(n) = Θ(log n)



The divide and conquer solution provides the same work complexity as the other approaches (Θ(n)) but achieves logarithmic span (Θ(log n)), making it more efficient for parallel execution compared to the iterative approach's linear span.
