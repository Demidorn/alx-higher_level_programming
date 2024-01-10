# JavaScript - Objects, Scopes, and Closures

> ## Requirements
> ### General
>
> - Allowed editors: vi, vim, emacs
< - All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
> - All your files should end with a new line
> - The first line of all your files should be exactly #!/usr/bin/node
> - A README.md file, at the root of the folder of the project, is mandatory
> - Your code should be semistandard compliant. Rules of Standard + <br>semicolons on top. Also as reference: AirBnB style
> - All your files must be executable
> - The length of your files will be tested using wc
> - You are not allowed to use var
>
---
> ## More Info
>> ### Install Node 14
>>  ```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -```
>> ```bash _$ sudo apt-get install -y nodejs_```
>> ### Install semi-standard
[documentation](https://intranet.alxswe.com/rltoken/oc1-9XTUtCiIyZkdAFvoUQ)

>> ```bash
$ sudo npm install semistandard --global_```

## Table of Contents
1. [Objects](#objects)
   - [Creating Objects](#creating-objects)
   - [Accessing Object Properties](#accessing-object-properties)
   - [Modifying Objects](#modifying-objects)
   - [Object Methods](#object-methods)

2. [Scopes](#scopes)
   - [Global Scope](#global-scope)
   - [Local Scope](#local-scope)
   - [Block Scope](#block-scope)
   - [Lexical Scope](#lexical-scope)

3. [Closures](#closures)
   - [Definition](#definition)
   - [Creating Closures](#creating-closures)
   - [Use Cases](#use-cases)
   - [Common Pitfalls](#common-pitfalls)

##objects
Objects are a versatile and fundamental data type that allows you to store and organize data using key-value pairs. used to represent real-world entities or concepts and are a crucial part of the language. 

##scopes
A scope is a region of your code where a particular variable or function is defined and can be accessed. Scopes help manage the visibility and lifetime of variables and functions.

##closures
A closure is a function having access to the parent scope, even after the parent function has closed.


| ----- | --------------| ----------|
|TASKS | DESCRIPTION | SOLUTION |
| ------- |------------------ |----------------|
|TASK 0 |Write an empty class Rectangle <BR>that defines a rectangle |
|TASK 1 | Write a class Rectangle that defines a rectangle |- You must use the class notation for defining your class<br>- The constructor must take 2 arguments w and h<br>- Initialize the instance attribute width with the value of w<br>- Initialize the instance attribute height with the value of h
|task 2 | Write a class Rectangle that defines a rectangle |- You must use the class notation for defining your class<br>- You must use the class notation for defining your class<br>- Initialize the instance attribute width with the value of w<br>- Initialize the instance attribute height with the value of h<br>If w or h is equal to 0 or not a positive integer, create an empty object
|TASK 3 |Write a class Rectangle that defines a rectangle |- You must use the class notation for defining your class<br>- The constructor must take 2 arguments: w and h<br>- Initialize the instance attribute width with the value of w<br>- Initialize the instance attribute height with the value of h<br>- If w or h is equal to 0 or not a positive integer, create an empty object<br>- Create an instance method called print()<br>that prints the rectangle using the character X

git clone https://github.com/Demidorn/0x13-javascript_objects_scopes_closures.git
