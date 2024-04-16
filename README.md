# Workout Planner
This is a low fidelity wireframe/prototype of a workout planner.  It is being designed to allow a user to submit an exercise, and retrieve exercises. Currently just black, and white it serves more as a guide to designers, and future developers of the project.  It is very simple on purpose.  

## File Structure
- **Routes:** Python files to retrieve and submit data.
- **Static:** Stylesheets, JS, and IMG directories
- **Templates:** HTML files

## Initial Concept
![site-architecture](https://github.com/manningstinson/workout-planner/assets/104523090/0720a264-5a22-4081-a99d-1631f8ae8ee7)
![site-architecture](https://github.com/manningstinson/workout-planner/assets/104523090/6fd7c4f5-c16a-438c-80b7-ee02db0fe40f)


## Navigation & Footer
The project incorporated a base.html file that serves as a template for the header, and footer sections. Each HTML file inherited the navigation from the base.html file

## Submit Exercise
The submit exercise page will allow a user to submit an exercise that will be added to a MySQL database. 

## Retrieve Exercise 
The retrieve exercise page will allow a user to retrieve several exercises based on a specific search criteria.

## Challenges
A small sample project was created approximately 2 months ago, and served as a basis for this hacksprint project.  Unfortunately, there were issues with deployment to digital ocean, and difficulty connecting to the database. 

Environment variables were initially setup to mask the database connection details, along with a .gitignore file.  We experienced issues with a Method not found error, when an entry got submitted to the database.  This was the first time working with an external provider, APP engine, and componenets.  

## Wiki
A wiki is being created to document the development process.  Currently empty, but will added to as the project progresses.
You can access the Of course! Here's the Markdown link for the page:

[Workout Planner Wiki](https://github.com/manningstinson/workout-planner/wiki) 

## Demo
You can access the project here.  This is a development server. It is currently hosted on [DigitalOcean](https://www.digitalocean.com/).

https://monkfish-app-xq5zg.ondigitalocean.app/

## Authors
[Manning Stinson](https://github.com/manningstinson) <br>
[Brandon Montezuma](https://github.com/bmontezuma) <br>
[Kevin Vang](https://github.com/kvang2)
