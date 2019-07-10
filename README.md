# Code Institute Cook Book

This project is designed to as a platform on which to demonstrate my data centric backend development skills. 


## Demo

A live demo of the website can be found [here](https://github.com/francisillingworth/milestone-project-3)


## UX

The Code Insitute Cook Book is a web application that allows a user to find/edit and delete recipes that already exist in a NoSQL Mongo database or add their own new recipes to the database which can then be found/edited/deleted with the search functions. The website does this in a simple intuative way with easy navigation, minimal fields and clear direction regarding requirements to proceed with the task you are trying to do.  

The design uses faded and light background colours so not to distract the user but also provide an asthetically pleasing webpage. Meanwhile any aspect of the page that has an effect (such as the edit, submit, delete buttons) all use bright colours to make them stand out and also provide insight into their purpose (e.g all delete buttons are red with a trashcan icon in providing clear meaning despite the button not actually containing the word delete). 

Recipes are displayed as an accordian list. When initially viewed this list will show each recipe by its name, cuisine type, author and cook time. Upon clicking a recipe this opens the accordian to reveal
a new accordian list with "ingredients" and "method" as the 2 list items. These new accordians can then be expanded to display their content. I have designed this list display so that for a specific recipe each accordian will stay open if another is clicked and they will close if a new recipe accordian is chosen. The idea here is so the full list of recipes remains compact but it also means that relevant information to a recipe can be kept open while opening another aspect to the same recipe(i.e the list of ingredients can be kept open along side the open method as this will be useful to the user).

### User Stories

##### Adding a recipe

From the home page you can proceed to the add recipe form by clicking the clearly defined "Add Recipe" button or using the "Add Recipe" navbar tab (as you can anywhere across the website). The form has 6 fields to complete. Each is clearly labelled and are required fields so the form can't be submitted unless they are complete. The Cuisine Type field is a dropdown menu where you can choose from the cuisine types already in the database. If this is not already in the database so not showing in the  menu you can add a new cuisine type by clicking on the clearly labelled link below this field. This link leads to a page where a new cuisine can be added to the database and once this form is submitted the website will redirect you back to the add recipe page. The submit button is clearly marked at the bottom of the page. By clicking this the form will update the database and the user will be redirected to the All Recipes page where you can view your recipe.



##### Finding a recipe

From the home page you can proceed to the "Find Recipe" page by clicking the clearly defined "Find Recipe" button or using the "Find Recipe" navbar tab (as you can anywhere across the website). The page is effectivily a form where a user can choose from 2 different fields (cuisine type and author) to filter the full list of recipes by, these can be used alone or together however if used together you get all the results from each filter as opposed to them working together for a more advanced search. If the form is submitted without choosing any parameters no recipes with be displayed. Once the parameters are chosen the form is submitted by clicking the clearly labelled "Find Recipe" button beneath the form. This will redirect the user to the "Results Page" displaying all results.



##### Editing/Deleting a recipe

Recipes are diplayed on 2 pages. The "All Recipes" page and the "Results Page" (you would be redirected her after submitting the find a recipe form on the "Find Recipe" page). Recipies are displayed as an accordian where the recipe name, cuisine type, author and cook time are all displayed without opening. Located to the right of each this information there are 2 clearly labelled buttons, Edit and Delete (Delete has no text but is easily recognisable due to the trashcan icon and red colour). To delete a recipe a user would simply click the delete item and the recipe will be removed premenatly from the database. To edit a recipe the user would click the edit button. This will redirect the user to an identical page to the "Add Recipe" page with the exception that the fields will already be filled in with the current recipe information. All fields are required so once the desired fields have been edited the user would just click the "Update Recipe" button. The user will then be redirected back to the "All Recipes" page. If the user decides that they no longer wish to edit the recipe they can click the "Cancel" button found next to the update button which will redirect the user back to the "All Recipes".


## Features

#### Existing Features

Add recipe - Allows users to add new recipe to data base by completing Add Recipe Form 

Edit recipe - Allows users to update existing recipes on database by editing the existing fields of a recipe and submitting the changes

Delete recipe/cuisine type - Allows users to delete a recipe or cuisine type by clicking a delete button on the selected recipe/cuisine type.

Add cuisine type - Allows users to add new cuisine type to data base by completing Add cuisine form. 

Edit cuisine type - Allows users to update existing cuisine types on database by editing the name and submitting the changes.

Find recipe - Allows users to seach for recipes by cuisine type or author by chosing values from two separate dropdown lists.


#### Features Left to Implement

I would like to add share functionality so poeple can share favourite recipes via social media/email etc.  

I would like to have a login feature so people can like or rate recipes. This wouldnt work at the moment as without user logins someone could vote as many times as they want.

I would like to add additional filtering functionality such as by cook time 

I would like to add functionality where the filters work together to provide a more comprehensive search feature. Currently the filters pull up all recipes that relate to just that filter causing duplicates and results that are not in line with the other selected filters. Hence the form currently requests to only apply one filter at a time.

## Technologies Used

HTML - Used for basic structure of webpage as was so structuring lists and forms on the webpage.

CSS - Used for basic styling of HTML elements

JQuery - Used to add meat to the HTML elements e.g accodian lists

Python - Used for all functionality - CRUD

Flask - micro framework used to run application

Mongo - Mongo was used for my NoSQL Database due to its ease of use anb my wish to practice working with NoSQL (I recognise MySQL would have been a better database design for this project had it been of anything other than a skills development tool).

.
## Testing

There was no automated testing used for this project. Each function has been tested thouroughly manually. There are 5 main functions across the web.

1 - Add recipe
Go to the "Add Recipe" Page Try to submit a recipe with one or more of the fields incomplete - The form will not submit and an error message will display on the screen showing the user which fields require revisiting.

2 - Edit recipe
Go to the "Edit Recipe" page and try to submit a recipe with one or more of the fields incomplete - The form will not submit and an error message will display on the screen showing the user which fields require revisiting.
Go to the "Edit Recipe" page and edit a field in the edit recipe form - Click update recipe. Find the recipe using either on the "All Recipes" page or via the "Find Recipe" page using the correct filters. The original recipe will now be updated to include the changes

3 - Delete recipe/cuisine type 
Find a recipe on the "All Recipes" page or a cuisine on the "Cuisines" page and click the delete button -  Now try to find the recipe using either on the "All Recipes" page or via the "Find Recipe" page using the correct filters. The recipe will now be no longer show as it has been removed from the database. If you chose to delete a cuisine this will no longer show on the "Cuisines" page and willalso no longer show in any of the cuisine dropdowns across the whole website. 

4 - Add cuisine type
Go to the "Add Cuisine" page and submit without adding a value to the form. The form will not submit and an error message will display on the screen showing the user why the form hasnt submitted.
Go to the "Add Cuisine" page and type in a new cuisne, then submit the form - The new cuisine type will now show in all Cuisine Type dropdown menus across the website.

5 - Edit cuisine type
Go to the "Edit Cuisine" page and submit the form after removing all text from the cuisine field. The form will not submit and an error message will display on the screen showing the user why the form hasnt submitted.
Go to the "Edit Cuisine" page and edit a cuisne, then submit the form - The updated cuisine type will now show in all Cuisine Type dropdown menus across the website and the old cuisine type will no longer appear.

6 - Find recipe 
Go to the "Find Recipe" page and select a filtering parameter then click find recipes. A list of all recipes matching the chosen parameters will show. If no parameters an empty list shows on the results page with a "back to search" button. If more than one parameter is chosen all results for each parameter will show. 



## Deployment


The website is hosted by Heroku and is deployed from the master branch. 
You can also git clone the code to run it locally on your machine via this link [Milestone Project 3 Git Hub Link](https://github.com/francisillingworth/milestone-project-3) .



This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits
The nav bar, forms and accordians were taken from Materialize.

Background image is from https://cooking.nytimes.com/guides/46-how-to-use-an-instant-pot

All recipes were taken from https://www.bbcgoodfood.com/
