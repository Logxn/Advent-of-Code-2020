# Day 2: Password Philosophy
To read more about the story [click here](https://adventofcode.com/2020/day/1).
## The Task: Part One
Our given puzzle input is a list of `passwords` and the `policy` it must fulfill.
#### Example Input
```
4-5 r: rrrjr
```
Our password is `rrrjr`.<br>
The policy it needs to fulfill is `4-5 r`, meaning that the password **must** contain the character `r` at least `4` and at most `5` times.
### Our Mission
Count all valid passwords.
### The Code
I have created a seperate text file for every day called `input.txt` where I paste my puzzle input.<br>
I first open the input and make a list of all passwords and their respective policies.<br>
```python
f = open("input.txt", "r")
password_policies = f.read().split("\n")
```
Remember our example input `4-5 r: rrrjr` ?<br>
**Notice:** We can easly split this input into 3 parts.<br>
- The character ranges: `4-5`
- The policy character: `r`
- The password: `rrrjr`

<br>I then create **three** arrays called `password_ranges`, `policies` and `passwords` and populate them.
```python
password_ranges = []
policies = []
passwords = []

for line in password_policies:
    breakdown = line.split(" ")

    password_ranges.append(breakdown[0].split("-"))
    policies.append(breakdown[1].replace(":", "")) # We want to remove the semicolon behind our policy character
    passwords.append(breakdown[2])
```
now its time to build a....
#### ✨Validation Function✨
Our function will have 4 parameters:
- `policy`: The character we want to check
- `min`: The minimum of policy characters in the `password`
- `max`: The maximum of policy characters in the `password`
- `password`: The password we want to validate 
<br>In this function we will loop trough all characters in our `password`.<br>
If we have a character that matches the `policy`-character we want to count the number of occurrences.<br>
```python
count = 0

    for c in password:
        if c == policy:
            count += 1
```
The only thing left to do is to check if the policy characters are in range.
```python
if count >= int(min_count) and count <= int(max_count):
        return True
```
This is our final function:
```python
def check_validity(policy, min_count, max_count, password):
    count = 0

    for c in password:
        if c == policy:
            count += 1
    
    # Min-Max verification
    if count >= int(min_count) and count <= int(max_count):
        return True
    
    return False
```
For the final solution I loop trough all the passwords and provide the function with valid values.<br>
If the function returns `true` I will count +1 towards the solution.<br>
```python
for i in range(len(passwords)):
    policy = policies[i]
    min_count = password_ranges[i][0]
    max_count = password_ranges[i][1]
    password = passwords[i]

    verify = check_validity(policy, min_count, max_count, password)
    if verify == True:
        solution += 1
```
## The Task: Part Two (Coming soon...)
