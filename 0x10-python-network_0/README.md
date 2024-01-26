# 0x10. Python - Network #0
Bash  Python  Scripting  Back-end  API

## Resources
### __Read or watch:__

- HTTP [HyperText Transfer Protocol](https://intranet.alxswe.com/rltoken/rAon_EpQ6PGl8N0plySn4A)
- [HTTP Cookies](https://intranet.alxswe.com/rltoken/MhVCl_0oviQldWPn5oX-NQ)

## Requirements
### General
- Allowed editors: __vi__, __vim__, __emacs__
- A README.md file, at the root of the folder of the project, is mandatory
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your Bash scripts should be exactly 3 lines long (__wc -l file__should print 3)
- All your files should end with a new line
- All your files must be executable
- The first line of all your bash files should be exactly ```bash #!/bin/bash```
- The second line of all your Bash scripts should be a comment <br>explaining what is the script doing
- All curl commands must have the option __-s__ (silent mode)
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all your Python files should be exactly ```bash #!/usr/bin/python3```
- Your code should use the pycodestyle (version __2.8.*__)
- All your modules should be documented: ``` bash python3 -c 'print(__import__("my_module").__doc__)' ```
- All your classes should be documented: ``` bash python3 -c 'print(__import__("my_module").MyClass.__doc__)' ```
- All your functions (inside and outside a class) should be documented: ```bash python3 -c 'print(__import__("my_module").my_function.__doc__)'  ``` and ``` bash python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' ```
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the<br> module, class or method (the length of it will be verified)

# Tasks
### 0. cURL body size
Write a Bash script that takes in a URL, sends a request to that URL,<br> and displays the size of the body of the response
- The size must be displayed in bytes
- You have to use curl
Please test your script in the sandbox provided,<br> using the web server running on port 5000

### 1. cURL to the end
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
- Display only body of a 200 status code response
- You have to use curl
Please test your script in the sandbox provided, <br>using the web server running on port 5000

### 2. cURL Method
Write a Bash script that sends a DELETE request to the URL <br>passed as the first argument and displays the body of the response
- You have to use curl
Please test your script in the sandbox provided, using the<br> web server running on port 5000

### 3. cURL only methods
Write a Bash script that takes in a URL and displays all HTTP<br> methods the server will accept.
- You have to use curl
Please test your script in the sandbox provided, using the <br>web server running on port 5000

### 4. cURL headers
Write a Bash script that takes in a URL as an argument, sends a __GET__ reques<br>t to the URL, and displays the body of the response
- A header variable X-School-User-Id must be sent with the value __98__
- You have to use __curl__
Please test your script in the sandbox provided, using the <br>web server running on port 5000

### 5. cURL POST parameters
Write a Bash script that takes in a URL, sends a __POST__ request<br> to the passed URL, and displays the body of the response
- A variable email must be sent with the value __test@gmail.com__
- A variable subject must be sent with the value ___I will always be here for PLD___
- You have to use __curl__
Please test your script in the sandbox provided, using the <br>web server running on port 5000

### 6. Find a peak
**Technical interview preparation:**
- You are not allowed to google anything
- Whiteboard first
Write a function that finds a peak in a list of unsorted integers.
- Prototype: ```bash def find_peak(list_of_integers):```
- You are not allowed to import any module
- Your algorithm must have the lowest complexity <br>(hint: you don’t need to go through all numbers to find a peak)
- __6-peak.py__ must contain the function
- __6-peak.txt__  must contain the complexity of your algorithm: __O(log(n))__, __O(n)__, __O(nlog(n))__ or __O(n2)__
**Note:** there may be more than one peak in the list
