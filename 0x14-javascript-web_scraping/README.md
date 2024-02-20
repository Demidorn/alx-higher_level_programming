# 0x14. JavaScript - Web scraping
Scripting  API  JavaScript

### Resources
__Read or watch:__
- [Working with JSON data](https://intranet.alxswe.com/rltoken/ONv-sSv-FA87Mc5rMZmO6A)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.alxswe.com/rltoken/zm0h7FqpQCZZpPZqxxwLxA)
- [request module](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)
- [Modern JS](https://intranet.alxswe.com/rltoken/j2PStAUtVPdXKwrrFxpt0g)
---
# Requirements
> **General**
> - Allowed editors: vi, vim, emacs
> - All your files will be interpreted on Ubuntu 20.04 LTS using*node (version 14.x)*
> - All your files should end with a new line
> - The first line of all your files should be exactly `#!/usr/bin/node`
> - **A README.md** file, at the root of the folder of the project, is mandatory
> - Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
> - All your files must be executable
> - The length of your files will be tested using wc
> - You are not allowed to use *var***


## More Info
**Install Node 14**
```
{
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
}
```
**Install semi-standard**
__[Documentation](https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg)__
``` bash
$ sudo npm install semistandard --global
```
**Install request module and use it**
[Documentation](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)
```
{
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
}
```

| No | Task | Descriptio |
| -------- | :------------: | :---------- |
| **Readme**| Write a script that reads and prints the content of a file. | - The first argument is the file path<br>
- The content of the file must be read in *utf-8*<br>
- If an error occurred during the reading, print the error object |
| **Write me** | Write a script that writes a string to a file. | - The first argument is the file path<br>
- The second argument is the string to write<br>
- The content of the file must be written in utf-8<br>
If an error occurred during while writing, print the error object. |
| **Status code** | Write a script that display the status code of a *GET* request. | - The first argument is the URL to request __(GET)__<br>
- The status code must be printed like this: code: *<status code>*<br>
- You must use the module request |
| **Star wars movie title**|Write a script that prints the title of a <br>Star Wars movie where the episode number <br>matches a given integer. | - The first argument is the movie ID<br>
-You must use the Star wars API with the endpoint <br> `https://swapi-api.alx-tools.com/api/films/:id`<br>
- You must use the module request |
| **Star wars Wedge Antilles** | Write a script that prints the number of <br>movies where the character *“Wedge Antilles”* is present. | - The first argument is the API URL of the *Star wars<br> API: https://swapi-api.alx-tools.com/api/films/*<br>
- Wedge Antilles is character ID __18__ - your script <br>**must** use this ID for filtering the result of the API<br>
- You must use the module request |
| **Loripsum** | Write a script that gets the contents of a webpage <br>and stores it in a file. | - The first argument is the URL to request<br>
- The second argument the file path to store the<br>body response<br>
- The file must be UTF-8 encoded<br>
- You must use the module request |
| **How many completed?** | Write a script that computes the number of tasks<br> completed by user id. | - The first argument is the API URL: <br>`https://jsonplaceholder.typicode.com/todos`<br>
- Only print users with completed task<br>
- You must use the module *request* |
| **Who was playing in this movie?** | Write a script that prints all characters of a Star Wars movie: | - The first argument is the Movie ID - example: <br>__3__ = “Return of the Jedi”<br>
- Display one character name by line<br>
- You must use the *Star wars API*<br>
- You must use the module *request* |
| **Right order** | Write a script that prints all characters of a Star Wars movie: | - The first argument is the Movie ID - example<br>: *3* = “Return of the Jedi”<br>
- Display one character name by line in the same order of<br> the list “characters” in the */films/* response<br>
- You must use the Star wars *API*<br>
- You must use the module *request* |

**Author [Demidorn](https://github.com/Demidorn/alx-higher_level_programming/0x14-javascript-web_scraping)
