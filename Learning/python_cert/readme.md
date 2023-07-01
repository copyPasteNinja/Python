### Octal Numbers

## its part of the exam but not widely used

## when number starts with 0O or 0o then thats octal value

## can use 0 to 7

print(0o123)

## hexadecimal numbers

print(0x123)

### Operators

    # Can't divide by 0 #

```division = 5 / 7
plus = 4 + 4
subtraction = 5 - 2
multiplication = 5 \* 5
```

## integer division

```int_num = 7 // 2
print(int_num)
```

## modulus division

```left_over_num = 7 % 4
print(left_over_num)
```

## power operator

```
power_sum = 2 \*\* 3
print(power_sum)
```

## Float

```
float_sum = 2 + 3.0
print(float_sum)
```

Extra: How does modulo division % work?
I’ve noticed that some students have problems understanding how modulo division works. Here is an easy-to-follow example that I once provided to a student in a private message. If you have a problem with modulo, have a look at it.

---

Let’s say that you work in a car company, and you produce wheels for cars. Your boss comes and says: “We need to quickly assembly as many cars as we can. We need the wheels that you produce in sets of 4. How many cars can we produce with the wheels that you have at the moment?”
You know that 1 car needs 4 wheels. Now, if you have 5 wheels in total in your factory, you will be able to create only 1 set of 4 wheels for 1 car, and you will then have 1 wheel left (5 = 4 _ 1 + 1). This “1 wheel left” is the remainder. And it’s also the result of modulo division. 5 % 4 = 1.
If you have 7 wheels, you can still only create 1 set of 4 wheels, and you will be left with 3 wheels (7 = 4 _ 1 + 3). The “3 wheels left” is the remainder. 7 % 4 = 3.
If you have 10 wheels, you can create 2 sets of 4 wheels, and you will be left with 2 wheels (10 = 4 \* 2 + 2). The “2 wheels left” is the remainder. 10 % 4 = 2.
If you only have 3 wheels in total, how many cars can you assemble? Zero. 3 wheels is not enough even for a single car, so you can produce 0 sets, and you will be left with 3 wheels. 3 % 4 = 3.
In general, if you have x % y, and the second number y is greater than the first number x, the result will always be x:
7 % 16 = 7
7 % 20 = 7
5 % 10 = 5
20 % 30 = 20

## Exercise - 2

Variables and Operators
In a fictional country named Lowtaxland, the income tax is 5%. In another fictional country, Ripoffland, the income tax is 43%. You are given a sample variable named income with the value of 250,000.

1. Create two additional variables: lowtaxland_rate with the value of 0.05 (which is the same as 5%) and ripoffland_rate with the value of 0.43 (which is the same as 43%).
2. Print to the output the following:
   Your income is {income} and you would pay {tax amount in Lowtaxland} income tax in Lowtaxland or {tax amount in Ripoffland} income tax in Ripoffland. You would save {difference between the tax amounts} by paying taxes in Lowtaxland!
   Your solution must replace the curly brackets (e.g. {income}) with the actual values (e.g. 250000). The values must be calculated correctly. The tax amount should be calculated as {income _ lowtaxland_rate} for Lowtaxland, and {income _ ripoffland_rate} for Ripoffland, respectively.

# Reassigning Values

```
age = 22
print(age)
age = age + 5
print(age)
```

    ### shortcut ^

```
age = 22
age += 5 ## also works with "-, \*, /, +"
print(age)
```

## string things

```
string = "hokus" + "pokus"
print(string)

string = "hokus"
print(string \* 5)
```

## string concatenation

```
print('23' + '3')
```

## input function

```
print("What is your name?")
user_name = input() #input function always returns str
print('Hello there ' + user_name)

user_name = input("What is your name?: ")
print('Hello there ' + user_name)
```

## Exercise - 3

Practising input()
Ask the user to provide their login and native language. Use the following prompts:
Enter your login: << remember to add a space at the end of this prompt!
Enter your native language: << remember to add a space at the end of this prompt!
Then, show the user the following message:
Your login is {login provided} and you speak {language provided}
For example, if the user provides the login h_potter and language British English, show:
Your login is h_potter and you speak British English
Watch out for typos: you must show the output in this particular format!

# A bit of technical theory

**Computer program** = a collection of instructions executed by a computer.

**Instruction list** = the set of instructions the given computer can execute; written in the form of machine code

**Complication**

- Compiles source code only once
- anyone can run the executable file

**Interpretation**

- interpret source code everytime you run programs
- everyone needs the interpreter to run

**Python interpreter behaviour**

- lexis - pre-defined keywords that cannot be used as variables
- syntax - the arrangement of keywords and phrases that make up python lanugage
- semantics - reference of what is True, if a function takes 1 arg, you can only give 1 arg
