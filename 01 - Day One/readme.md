# Day 1: Report Repair (Sanity Check)
To read more about the story [click here](https://adventofcode.com/2020/day/1).
## The Task - Part One
Our given puzzle input is a list of random numbers.<br>
We need to find **exactly two numbers** that give `2020` if they are `added` to each other.<br>
If those numbers are found we then have to `multiply` them in order to get the solution number for the first part of the task.<br>
### Code
I have created a seperate text file for every day called `input.txt` where I paste my puzzle input.<br>
I first open the input and make a list of all numbers.<br>
```python
f = open("input.txt", "r")
puzzle_input = f.read().split("\n")
```
I now have a list of string numbers.<br>
In order to actually do some proper math on these numbers I want to transform the list of *string*-numbers into a list of actual numbers.<br>
```python
numbers = list(map(int, input))
```
Notice how the function ```map(int, input)``` transforms my strings into int(egers).<br>
`numbers = list(...)` will then return an array/list of the puzzle input. (Example: `[1337, 8, 9, 666, 7777]`)<br><br>

Now its time to loop over my numbers.<br>
Remember the task: Find two numbers that give 2020 when you add them to each other.<br>
```python
for i in numbers:
    for j in numbers:
        if i + j == 2020:
            solution1 = i * j
            break
```
Now the only thing left to do is to print solution1 to get the solution for the first part of the task.
 
## The Task - Part Two
We still have the same input of random numbers.<br>
We now need to find **three** numbers that give `2020` if you add them up.<br>
Then again `multiply` those three numbers for the second solution.
 
### The Code
There is nothing excitingly new to the code.<br>
We can simply add another nested loop to our existing loop.<br>
```python
for i in numbers:
    for j in numbers:
        for x in numbers:
            if i + j + x == 2020:
                solution2 = i * j * x
                break
```
The only thing to do is to print solution2 to get the solution for the second part of the task.<br>
This is all folks!<br>
