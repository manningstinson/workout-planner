
![workout-planner-concept](https://github.com/manningstinson/workout-planner/assets/104523090/05b6a497-c456-47f0-a7ea-10e057dd5023)

# Workout Planner
This is a low fidelity wireframe/prototype of a workout planner.  It is being designed to allow a user to submit an exercise, and retrieve exercises. Currently just black, and white it serves more as a guide to designers, and future developers of the project.  It is very simple on purpose.  

## File Structure
- **Routes:** Python files to retrieve and submit data.
- **Static:** Stylesheets, JS, and IMG directories
- **Templates:** HTML files

## Initial Concept
![site-architecture](https://github.com/manningstinson/workout-planner/assets/104523090/6fd7c4f5-c16a-438c-80b7-ee02db0fe40f)

## Navigation & Footer
The project incorporated a base.html file that serves as a template for the header, and footer sections. Each HTML file inherited the navigation from the base.html file. 

## Submit Exercise
The submit exercise page will allow a user to submit an exercise that will be added to a MySQL database. 

## Retrieve Exercise 
The retrieve exercise page will allow a user to retrieve several exercises based on a specific search criteria.

## Exercise Content | Animations 
[Installation](#installation)<br>
[Usage](#usage)<br>
[Documentation](#documentation)<br>
[Contributing](#contributing)<br>
[License](#license)<br>

## Using Unreal Engine

To download Unreal Engine please follow the link.
[Unreal Engine](https://www.unrealengine.com/en-US/free-download/game-development-engine?utm_source=BingSearch&utm_medium=PaidSearch&utm_campaign=pr*UE_sp*UnrealEngine_an*Internal_ct*Google_cn*GameEngine-US_ta*Keywords_pl*LinkClicks_co*US&utm_id=1311718477789983&utm_term=game%20engine&utm_content=554622408&utm_creative=81982458167678)

[Youtube](https://www.youtube.com/) links for videos used.\
[Plank](https://youtu.be/xtnempgJM_U)\
[Bicept Curl](https://youtu.be/NrVe2ZAsSj8)\
[Squat](https://youtu.be/Z80l3gt0dNk)

## Challenges
A small sample project was created approximately 2 months ago, and served as a basis for this hacksprint project.  Unfortunately, there were issues with deployment to digital ocean, and difficulty connecting to the database. 

Environment variables were initially setup to mask the database connection details, along with a .gitignore file.  We experienced issues with a Method not found error, when an entry got submitted to the database.  This was the first time working with an external provider, APP engine, and componenets. 

It is much different than working with a traditional sandbox as each file change can impact the build process. New errors that were encountered were 

**405 errors - METHOD NOT FOUND
500 Internal Service Errors **.   
These errors can be puzzling as it doesn't exactly tell you where the error occured. A change in one file, can cause a build to fail so reading, and understanding the runtime logs is important. 

## Wiki
A wiki is being created to document the development process.  Currently empty, but will added to as the project progresses.
You can access it here.

[Workout Planner Wiki](https://github.com/manningstinson/workout-planner/wiki) 

## Demo
You can access the project here.  This is a development server. It is currently hosted on [DigitalOcean](https://www.digitalocean.com/).

https://monkfish-app-xq5zg.ondigitalocean.app/

## Authors
[Manning Stinson](https://github.com/manningstinson) <br>
[Brandon Montezuma](https://github.com/bmontezuma) <br>
[Kevin Vang](https://github.com/kvang2)
