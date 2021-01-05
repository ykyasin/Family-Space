#   **Family-Space**

## Contents
* [Introduction ](#introduction )
   * [Objective](#objective)
   * [My Project Proposol ](#my-project-proposol )
* [Software Architecture ](#software-architecture )
   * [Project Tracking ](#project-tracking)
   * [Entity Relationship Diagram](#entity-relationship-diagram)
   * [Continuous Integration Pipeline](#continuous-integration-pipeline)
   * [Risk Assessment](#risk-assessment)
* [CRUD Functionality](#crud-functionality)
   * [Login Page](#login-page)
   * [Main Page](#main-page)
* [CI Server](#ci-server)
* [Testing](#testing)
   * [Unit Testing](#unit-testing)
   * [Integration Testing](#integration-testing)
   * [Test Results](#test-results)
* [Future Improvements](#future-improvements)
* [Author](#author)


## Introduction 
### Objective

This is an individual project in order to meet the SFIA requirements. The objective of this project is as follows: 

> "To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training." 

The concepts gained from this project is as follows: 
* Project management (Specifically the agile methodology)
* Python coding and testing
* The use of GitHub
* Basic Linux
* Python Web Development using the Flask framework
* Continuous integration with Jenkins
* Understanding and utilising Cloud concepts using GCP 


### My Project Proposol 
The project idea that I decided to go with is a family blog website, titled: Family-Space. The idea behind this project is to create an online social hub for familiy members, similar to say a family Whatsapp group chat. In Family-Space, members will be able to create user accounts and make posts for everyone else to see. For the CRUD functionality aspect, a member would be able to create a user which will be saved on the database and can then update their account names if need be, this will update their information on the database. Users will also be able to create posts which will be stored on the database. Each user can also create posts which will be stored on the database and can be viewed by other users on their main page. Each user can also delete any of their posts whenever they wish, which will be wiped off the database. And finally, each user can delete their own accounts, which will subsequently wipe out all their posts.

Also please note that as part of the users information, I have decided to use only a name as an input instead of two fields containing a first name and a surname. As the goal is to simply have a working CRUD application that meets the requirements, I decided to simplify it here to work on the more important bits. However, extra information can be added in future sprints to allow users to do more on the website. 

## Software Architecture 

### Project Tracking 
For project tracking, I decided to use Trello board ([click here to access it](https://trello.com/b/FjcXT6ji/family-space)). The reason I chose Trello is because it is an aesthetically pleasing, lightweight tool ideal for this type of project. I have set it up such that there is several lists each containing cards related to that list. Each card may contain colour coded labels which represent what that particular card is related to. I have also decided to use the MoSCow approach, which are also shown on the cards as labels. The lists I've made are as follows: 

* Project Resources - Containing relevant links
* User stories - Each card in the format "As a [User]..., I want... [Feature], so that... [Details]"
* Backlog - 
* In-Progress - This list contains any tasks that is currently being worked on
* Testing - This list contains features that need to be tested
* Complete - Contains all tasks that are complete
* Issues - Each card here represents an issue which I struggled with

![Trello](https://user-images.githubusercontent.com/73299366/103594241-fe910800-4eef-11eb-8c7e-d92fcff145f1.JPG)

### Entity Relationship Diagram
The original ERD I created featured an additional table on the database (other than users and posts table), which was a comment section. The original ERD is shown below. It features a one to many relationship between User and Post and a one to many between relation between Post and Comment as well as User to Comment. A user can have many posts and make many comments, but each post must have one user and each comment must have one user and one post. 

![First_erd](https://user-images.githubusercontent.com/73299366/103592952-54fc4780-4eec-11eb-9de1-604bd0230630.JPG)

The ERD shown below is the one I decided to move on with, which is a simple one to many relationship between User and Post. For the first sprint, this will do the job and should meet the MVP.

![Second_erd](https://user-images.githubusercontent.com/73299366/103592969-5fb6dc80-4eec-11eb-8e33-332d4f90279d.JPG)

### Continuous Integration Pipeline
![Ci_Pipeline](https://user-images.githubusercontent.com/73299366/103595546-a0662400-4ef3-11eb-9a26-09ad8a2478ef.JPG)

The image above shows the CI pipeline for this project. Development is started by getting work from the trello board. Once the task is complete, the code is pushed on to Github which triggers a a webhook. Jenkins then automates the tests and shows the coverage report on the console, which can then be seen by the developer to work on any failed tests. After successful tests, the jenkins server then automatically runs a testing environment for any dynamic testing. 

### Risk Assessment
The first image below is the original risk assessment made before any serious work on the application had began. The second one shows the final risk assessment, which has a few more entries which I realised whilst working on the project.

Original risk assessment: 
![First_Risk](https://user-images.githubusercontent.com/73299366/103595638-d7d4d080-4ef3-11eb-8cb9-75a797be5f0a.JPG)

Final risk assessment:
![Second_Risk](https://user-images.githubusercontent.com/73299366/103595659-e15e3880-4ef3-11eb-99be-5fcea22be88c.JPG)

## CRUD Functionality 
This section will discuss the basic workings of the website and the front-end design. For the login functionality, I have decided to simply use a dropdown menu with user names found in the database and a login button. 

### Login Page

The two below images show that when a name is added in the name field and the "Add new member" button is clicked, the name will be show in the drop down menu. The way this worked is that once the button is clicked, a new user is generated in the database with the name written in the field, which will subsequently be shown in the dropdown menu due to the name now being in the database.

First the name is written and the "Add new member" button is clicked:

![login_page_2](https://user-images.githubusercontent.com/73299366/103596066-f5566a00-4ef4-11eb-9d40-ded29d54fc14.JPG)

Then the name now appears in the dropdown menu:

![login_page_3](https://user-images.githubusercontent.com/73299366/103596073-f8e9f100-4ef4-11eb-947f-4366b60756ce.JPG)

### Main Page
After logging in, you will be directed to the main page which will show all your posts and anyone elses. The first image below shows that you are logged in as Adnan, and you see a post by another user Yusuf. To make a post, you type in the "How you feeling?" field and click post.
![main_page_2](https://user-images.githubusercontent.com/73299366/103596110-1028de80-4ef5-11eb-9364-77730fc47304.JPG)

The page will refresh and Adnan's post will show below Yusuf's. All posts made by you will have a delete button after it, if the delete button is clicked, only that particular post will be deleted. 
![main_page_3](https://user-images.githubusercontent.com/73299366/103596113-11f2a200-4ef5-11eb-8670-4b0964cdcdb2.JPG)

In this page you can also change the name on your account. Below shows the page after clicking the "Change account name" button, which generates a field for you to fill a name in.
![main_page_4](https://user-images.githubusercontent.com/73299366/103596117-1454fc00-4ef5-11eb-9196-f36b7e215bf7.JPG)

After filling it in and clicking the "Change" button, you will notice that the name in the main page has changed. This is because the name of the user has been updated in the database.
![main_page_5](https://user-images.githubusercontent.com/73299366/103596124-174fec80-4ef5-11eb-8903-b83cad2c6b49.JPG)

Also, after clicking on the "Delete your account" button, you will be asked if you are sure. If yes, you will be redirected to the login page with your user having been deleted from the database. If no, then the page will simply refresh showing its original form.
![main_page_6](https://user-images.githubusercontent.com/73299366/103596129-1919b000-4ef5-11eb-8000-cb3e5a50447b.JPG)

The final thing to mention is the "Logout" button, this button simply redirects you back to the login page.

## CI Server
The below image shows the screenshot of my Family-Space project on Jenkins. Using Jenkins, I am able to have my code automatically tested everytime I make a commit and push it on to my Github. It does this using a Webhhook. 
![jenkins_project](https://user-images.githubusercontent.com/73299366/103598019-862f4480-4ef9-11eb-855f-4aaaaefe3140.JPG)

The Bash script used to allow for the testing and deployment of the app is show in the image below. The main things to be noted in the script is that it firsts installs the Python virtual environment, goes into the virtual environment, and then executes the pytest after installing requirements. After testing is done, the app is automatically run using systemd.

![Bash_script](https://user-images.githubusercontent.com/73299366/103598040-90514300-4ef9-11eb-868a-d81a9179d9c0.JPG)


## Testing
### Unit Testing
The first of testing done on the application is called unit testing. The route functions are tested via inputting specific scenarios and checking to see if they produce expected outputs by using assert. Testing in this manner helps us find out if any function is not working as intended. The unit tests are automatically run in Jenkins if a Git push is made to the repo (as shown in the bash script in the previous section). This will then produce a coverage report detailing coverage percentage, whether the tests were successful and which lines have yet to be tested.  Also, a html document can be made by adding a **_--cov-report html_** command to the line in which the pytest is run. These coverage reports can be seen in the results section below.

### Integration testing
To perform integration testing, selenium was used. Selenium allowed me to simulate situations in navigating through the websites, i.e. by entering information into fields and clicking buttons. Then asserts are made to see if the response of the testing produces expected results. The integration tests are also run automatically on Jenkins. 

### Test Results
![Coverage](https://user-images.githubusercontent.com/73299366/103598058-96472400-4ef9-11eb-8563-0d525e591cf5.JPG)

The above image shows the coverage report for my application. As shown, I have a coverage percentage of 77%, which is not ideal. This is because I was unable to test specific lines due to how the functiions were made. However, it should be noted that with dynamic testing I found that everything worked as they should and that the coverage is not 100% simply because I had trouble coding the tests for the specific lines shown in the missing section in the image. Beyond that, the tests that were done for both unit and integration testing have all passed.

The below image shows the same information as the one above, but as a html page.
![Coverage_html](https://user-images.githubusercontent.com/73299366/103598061-9810e780-4ef9-11eb-97d2-c48969b86672.JPG)

## Future Improvements
There are many improvements that can be made to the application. However, to name a few: 
* To implement my original ERD approach by including a comments table so that users an comment under posts
* Improve test coverage by implementing better code practices 
* By including more user details such as having emails as well as passwords
* To implement a more traditional login approach 
* To improve the front-end design of the website


## Author
Yusuf Yasin


