# Cheatsheets

This article is a collection of cheat sheets that you can use as you solve problems and prepare for interviews. You will find:

- Time complexity (Big O) cheat sheet
- General Data Structure/Algorithm flowchart (when to use each)
- Stages of an interview cheat sheet

---

## Time Complexity (Big O) Cheat Sheet

### Arrays (Dynamic Array/List)

Given `n = arr.length`:

| Operation                                 | Time Complexity    |
|--------------------------------------------|--------------------|
| Add/remove at the end                      | O(1) (amortized)   |
| Add/remove at arbitrary index              | O(n)               |
| Access/modify at arbitrary index           | O(1)               |
| Check if element exists                    | O(n)               |
| Two pointers (e.g., sliding window)        | O(n * k)           |
| Build prefix sum                           | O(n)               |
| Sum of subarray (given prefix sum)         | O(1)               |

---

### Strings (Immutable)

Given `n = s.length`:

| Operation                                 | Time Complexity    |
|--------------------------------------------|--------------------|
| Add/remove character                       | O(n)               |
| Access at arbitrary index                  | O(1)               |
| Concatenate two strings                    | O(n + m)           |
| Create substring                           | O(m)               |
| Two pointers                               | O(n * k)           |
| Build string (join, string builder, etc.)  | O(n)               |

---

### Linked Lists

Given `n = number of nodes`:

| Operation                                            | Time Complexity    |
|------------------------------------------------------|--------------------|
| Add/remove (given pointer before location)          | O(1)               |
| Add/remove (given pointer at location, doubly linked)| O(1)               |
| Add/remove at arbitrary position (no pointer)       | O(n)               |
| Access at arbitrary position (no pointer)           | O(n)               |
| Check if element exists                              | O(n)               |
| Reverse between position i and j                     | O(j - i)           |
| Detect a cycle (fast/slow pointers or hash map)      | O(n)               |

---

### Hash Table / Dictionary

Given `n = number of keys`:

| Operation                         | Time Complexity    |
|------------------------------------|--------------------|
| Add/remove key-value               | O(1)               |
| Check if key exists                | O(1)               |
| Check if value exists              | O(n)               |
| Access/modify value by key         | O(1)               |
| Iterate over keys/values           | O(n)               |

> Note: O(1) assumes ideal hash function. Hashing strings takes O(m) where m is the string length.

---

### Set

Given `n = number of elements`:

| Operation                | Time Complexity    |
|--------------------------|--------------------|
| Add/remove element        | O(1)               |
| Check if element exists   | O(1)               |

---

### Stack

If implemented using dynamic array:

| Operation                          | Time Complexity    |
|-------------------------------------|--------------------|
| Push                                | O(1)               |
| Pop                                 | O(1)               |
| Peek (top)                          | O(1)               |
| Access/modify at arbitrary index    | O(1)               |
| Check if element exists             | O(n)               |

---

### Queue

If implemented using doubly linked list:

| Operation                          | Time Complexity    |
|-------------------------------------|--------------------|
| Enqueue                             | O(1)               |
| Dequeue                             | O(1)               |
| Peek (front)                        | O(1)               |
| Access/modify at arbitrary index    | O(n)               |
| Check if element exists             | O(n)               |

---

### Binary Tree (DFS/BFS)

Given `n = number of nodes`:

| Operation                             | Time Complexity    |
|----------------------------------------|--------------------|
| DFS/BFS                               | O(n * k), usually k = O(1) |

---

### Binary Search Tree

Given `n = number of nodes`:

| Operation                     | Time Complexity          |
|-------------------------------|--------------------------|
| Add/remove                     | O(log n) avg / O(n) worst|
| Check if element exists        | O(log n) avg / O(n) worst|

> Worst case: tree is skewed (like a linked list).  
> Average case: balanced tree.

---

### Heap / Priority Queue

Given `n = number of elements`:

| Operation              | Time Complexity    |
|------------------------|--------------------|
| Add element             | O(log n)           |
| Delete min              | O(log n)           |
| Find min                | O(1)               |
| Check if element exists | O(n)               |

---

### Binary Search

| Operation          | Time Complexity    |
|--------------------|--------------------|
| Binary search      | O(log n)           |

---

### Miscellaneous

| Operation                                 | Time Complexity          |
|--------------------------------------------|--------------------------|
| Sorting                                    | O(n log n)               |
| DFS/BFS on graph                           | O(n * k + e)             |
| DFS/BFS space (graph)                      | O(n + e)                 |
| Dynamic programming (time)                 | O(n * k)                 |
| Dynamic programming (space)                | O(n)                     |

---

## Input Size vs Time Complexity

| Input Size | Acceptable Complexity                    | Notes                                        |
|-------------|-------------------------------------------|-----------------------------------------------|
| n ≤ 10      | O(n^2 * n!) or O(4^n)                   | Brute force, backtracking okay               |
| 10 < n ≤ 20 | O(2^n)                                  | Subsets, subsequences                        |
| 20 < n ≤ 100| O(n^3)                                  | Nested loops acceptable                      |
| 100 < n ≤ 1,000| O(n^2)                               | Double loops fine                            |
| 1,000 < n ≤ 10,000| O(n log n)                        | Efficient sorts, heap, binary search needed  |
| n ≈ 10^5    | O(n) or O(n log n)                      | Linear or linearithmic time only             |
| n ≈ 10^6    | O(n)                                    | Linear time required                         |

---

## Notes

- The above table helps estimate the appropriate time complexity based on input size.
- Always clarify input size constraints in interviews if not provided.

## Sorting Algorithms

All major programming languages have a built-in method for sorting. It is usually correct to assume that sorting costs  
O(n ⋅ log n), where *n* is the number of elements being sorted.

For completeness, here is a chart that lists common sorting algorithms and their complexities:

| Algorithm        | Best      | Average    | Worst      | Space | Stable |
|------------------|-----------|------------|------------|-------|--------|
| Bubble Sort      | O(n)      | O(n²)      | O(n²)      | O(1)  | Yes    |
| Selection Sort   | O(n²)     | O(n²)      | O(n²)      | O(1)  | No     |
| Insertion Sort   | O(n)      | O(n²)      | O(n²)      | O(1)  | Yes    |
| Merge Sort       | O(n log n)| O(n log n) | O(n log n) | O(n)  | Yes    |
| Quick Sort       | O(n log n)| O(n log n) | O(n²)      | O(log n)| No   |
| Heap Sort        | O(n log n)| O(n log n) | O(n log n) | O(1)  | No     |
| Timsort (Python) | O(n)      | O(n log n) | O(n log n) | O(n)  | Yes    |
| Radix Sort       | O(nk)     | O(nk)      | O(nk)      | O(n+k)| Yes    |
| Counting Sort    | O(n + k)  | O(n + k)   | O(n + k)   | O(k)  | Yes    |
| Bucket Sort      | O(n + k)  | O(n + k)   | O(n²)      | O(n)  | Yes    |

> Note: The sorting algorithm used by a programming language may vary.  
> Example: Python uses **Timsort** (a hybrid of Merge Sort and Insertion Sort). C++ leaves the implementation unspecified.

**Definition of a stable sort (from Wikipedia):**  
*“Stable sorting algorithms maintain the relative order of records with equal keys (i.e. values). That is, a sorting algorithm is stable if whenever there are two records R and S with the same key and with R appearing before S in the original list, R will appear before S in the sorted list.”*

---

## General Data Structures & Algorithms Flowchart



# Interview Stages Cheat Sheet

The following is a summary of the "Stages of an interview" article. If you have a remote interview, you can print this condensed version and keep it in front of you during the interview.

---

## Stage 1: Introductions

- Have a rehearsed 30-60 second introduction regarding your **education, work experience, and interests** prepared.
- **Smile and speak with confidence.**
- Pay attention when the interviewer talks about themselves and **incorporate their work into your questions later.**

---

## Stage 2: Problem Statement

- **Paraphrase the problem** back to the interviewer after they have read it to you.
- **Ask clarifying questions** about the input, such as the expected input size, edge cases, and invalid inputs.
- **Quickly walk through an example test case** to confirm you understand the problem.

---

## Stage 3: Brainstorming Data Structures & Algorithms (DS&A)

- **Always think out loud.**
- Break the problem down: figure out what you need to do, and think about what data structure or algorithm can accomplish it with a good time complexity.
- Be receptive to feedback — the interviewer is probably **hinting you towards the correct solution.**
- Once you have an idea, **explain it before coding.** Make sure the interviewer agrees it is a reasonable approach.

---

## Stage 4: Implementation

- **Explain your decisions as you implement.** For example, when declaring a set, explain its purpose.
- Write **clean code** that conforms to your language's conventions.
- Avoid duplicate code — use **helper functions or loops** if writing similar code multiple times.
- If you get stuck, **don't panic — communicate.**
- It's okay to start with a **brute force solution** (acknowledge it), then improve it by optimizing the slow parts.
- **Keep thinking out loud and engage with the interviewer.** This makes it easier for them to give hints.

---

## Stage 5: Testing & Debugging

- When walking through test cases, **keep track of variables** by writing them at the bottom of the file and updating them.
- **Condense trivial steps** (like prefix sums) to save time.
- If there are errors and the environment allows running code, **add print statements** and walk through a small test case, comparing expected vs. actual values.
- **Stay vocal and collaborative** if you run into problems.

---

## Stage 6: Explanations & Follow-ups

Be prepared to answer:

- What is the **time and space complexity**, both average and worst case?
- **Why did you choose** this data structure, algorithm, or logic?
- **Can the algorithm be improved?** (If they ask, the answer is usually yes — especially if it's slower than O(n).)

---

## Stage 7: Outro

- **Prepare questions** about the company.
- Be interested, **smile**, and ask **follow-up questions** based on the interviewer's responses.

---
