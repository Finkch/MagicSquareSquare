# MagicSquareSquare
A programatic approach to the unsolved 3x3 magic square squared problem

The magic square problem has an nxn board filled with distinct integers. The sum across each row, each column, and the two diagnals must all be equal. There are a few unsolved variants; this code tackles the 3x3 board where at least 7 of the items are distinct squares of integers.

The approach from this code is to iterate over a large swathe of numbers. A number is split into 9 distinct components, where at least 7 must be squares of integers. Once a sufficient set of numbers have been found, a brute force search is done to try and place them in a magic square. In short, it tries to work backwards.

One other trick this code uses is that it precomputes the squares of a lot of numbers and places them into an array. That way, the step that splits the number into 9 distinct components can use an O(1) lookup rather than a costly square root operation.
