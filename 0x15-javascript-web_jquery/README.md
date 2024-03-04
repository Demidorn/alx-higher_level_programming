# 0x15. JavaScript - Web jQuery
Front-end  JavaScript
## Requirements
**General**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Chrome (version 57.0)
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, <br>is mandatory
- Your code should be semistandard compliant with the *flag --<br>global $: semistandard *.js --global $*
- You must use JQuery version __3.x__
- You are not allowed to use var
- HTML should not reload for each action: DOM manipulation,<br>update values, fetch data…

More Info
Make sure you have jQuery if not *Import JQuery*
```<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>```

## Tasks
> 0. Write a JavaScript script that updates the text color of the <br><header> element to red *(#FF0000):*
>> - You must use document.querySelector to select the HTML tag
>> - You can’t use the JQuery API

> 1. Write a JavaScript script that updates the text color of the <br> *<header>* element to red *(#FF0000):*
>> - You can’t use document.querySelector to select the HTML tag
>> - You must use the JQuery API

> 2. Write a JavaScript script that updates the text color of the<br> *<header>* element to red *(#FF0000)* when the user<br> clicks on the tag DIV#red_header:
>> - You can’t use document.querySelector to select the HTML tag
>> - You must use the JQuery API

> 3. Write a JavaScript script that adds the class red to the<br> *<header>* element when the user clicks on the tag<br> *DIV#red_header*
>> - You can’t use document.querySelector to select the HTML tag
>> - You must use the JQuery API

> 4. Write a JavaScript script that toggles the class of the <br>*<header>* element when the user clicks on the tag <br>*DIV#toggle_header:*
>> - The <header> element must always have one class: red or<br> green, never both in the same time and never empty.
>> - If the current class is red, when the user click on __DIV#toggle_header__,<br> the class must be updated to green ; and the reverse.
>> - You can’t use document.querySelector to select the HTML tag
>> - You must use the JQuery API

> 5. Write a JavaScript script that adds a <li> element to a list<br> when the user clicks on the tag *DIV#add_item:*
>> - The new element must be: *<li>Item</li>*
>> - The new element must be added to UL.my_list
>> - You can’t use document.querySelector to select the HTML tag
>> - You must use the JQuery API

>> 6. Write a JavaScript script that updates the text of the<br> *<header>* element to New Header!!! when the user clicks on<br> *DIV#update_header*
>> - You can’t use document.querySelector to select the HTML tag
>> - You must use the JQuery API

> 7. Write a JavaScript script that fetches the character __name__ from this URL: *https://swapi-api.alx-tools.com/api/people/5/?format=json*
>> - The name must be displayed in the HTML tag *DIV#character*
>> - You can’t use document.querySelector to select the HTML tag
>> - You must use the JQuery API

> 8. Write a JavaScript script that fetches and lists the title for all <br>movies by using this URL: *https://swapi-api.alx-tools.com/api/films/?format=json*
>> - All movie titles must be list in the HTML tag *UL#list_movies*
>> - You can’t use document.querySelector to select the HTML tag
>> - You must use the JQuery API

> 9. Write a JavaScript script that fetches from https:<br>*//hellosalut.stefanbohacek.dev/?lang=fr* and displays the<br> value of hello from that fetch in the HTML tag *DIV#hello.*
>> - The translation of “hello” must be displayed in the <br>HTML tag *DIV#hello*
>> - You can’t use document.querySelector to select the HTML tag
>> - You must use the JQuery API
>> - Your script must work when it is imported from the *<head>* tag
