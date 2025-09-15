

# CMPS 2200 Assignment 1

**Name:** Natalie Gockerman


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes, this is true because 2^(n+1) = 2 * 2^n 
.  Take c = 2 and n0 = 1
.  For all n >= 1:2^(n+1) <= 2 * 2^n = c * 2^n
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No, because (2^2^n) / (2^n) = 2^(2^n)-n
.  As n -> infinity, the ratio approaches infinity, therefore it is not in O(2n).
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  No, because a positive power of n will always dominate any power of log n.
.  For this specifically, (n^1.01) / ((logn) ^2) = (e^1.01t) / (t^2)
.  As n -> infinity, the ratio approaches infinity, therefore n^1.01 is not O((logn)^2).
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes, this is true for similar reasoning to 1c
.  As we showed above, n^1.01 grows at least as fast (much faster) than (logn) ^2. 
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No, because (sqrt(n)) / ((log n)^3) = (e^(t/2)) / (t^3)
.  As t approaches infinity, the ratio approaches infinity, therefore sqrt of n is not O((logn)^3)
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes, because as we just proved, sqrt(n) will grow faster than (log n)^3.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  
.  The purpose of the function "foo(x)" is to return the x-th fibonacci number (x based off input).
.  It works firsby handling possible base cases of x = 0 or x = 1. In these cases the x-th fibonnaci number is just 0 or 1.
.  However, if neither of these are true the x-th fibonnaci number is equal to the sum of the 2 previous numbers.
.  To find this sum, the function calls itself recursively, adding the values for the 2 previous positions.
.  This will continue until it adds up all the positions beginning with the base cases 0 and 1.
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  
.  The work of this implementation is W(n )= Θ(n), because you handle each element once and each element has a work cost of O(1).
.  The span of this implementation is S(n) = Θ(n), because the loop iterations are sequential, not recursive or divided.
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  The work for this algorithm is W(n) = 2W(n/2) + O(1), or W(n) = Θ(n).
.  The span for this algorithm is S(n) = S(n/2) + S(n/2) + O(1) = 2S(n/2) + O(1), or S(n) = Θ(n), because the two halves when split run sequentially, not parallel. 
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  
.  The work would remain unchanged at W(n) = Θ(n).
.  The span, since running parallel this time, S(n) = S(n/2) + O(1) = Θ(log n).
.  
.  
.  
.  
.  
.  

