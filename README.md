#   **Family-Space**

## Introduction: 
### Objective

This is an individual project in order to meet the SFIA requirements. The objective of this project is as follows: 

> "To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training." 

The concepts gained from this project is as follows: 
- Project management (Specifically the agile methodology)
- Python coding and testing
- The use of GitHub
- Basic Linux
- Python Web Development using the Flask framework
- Continuous integration with Jenkins
- Understanding and utilising Cloud concepts using GCP


### My project proposol 
The project idea that I decided to go with is a family blog website, titled: Family-Space. The idea behind this project is to create an online social hub for familiy members, similar to say a family Whatsapp group chat. In Family-Space, members will be able to create user accounts and make posts for everyone else to see. For the CRUD functionality aspect, a member would be able to create a user which will be saved on the database and can then update their account names if need be, this will update their information on the database. Users will also be able to create posts which will be stored on the database. Each user can also create posts which will be stored on the database and can be viewed by other users on their main page. Each user can also delete any of their posts whenever they wish, which will be wiped off the database. And finally, each user can delete their own accounts, which will subsequently wipe out all their posts.

Also please note that as part of the users information, I have decided to use only a name as an input instead of two fields containing a first name and a surname. As the goal is to simply have a working CRUD application that meets the requirements, I decided to simplify it here to work on the more important bits. However, extra information can be added in future sprints to allow users to do more on the website.

## Software Architecture 

### Project Tracking - Trello Board
For project tracking, I decided to use Trello board ([click here to access it](https://trello.com/b/FjcXT6ji/family-space)). The reason I chose Trello is because it is an aesthetically pleasing, lightweight tool ideal for this type of project. I have set it up such that there is several lists each containing cards related to that list. Each card may contain colour coded labels which represent what that particular card is related to. I have also decided to use the MoSCow approach, which are also shown on the cards as labels. The lists I've made are as follows: 

* Project Resources - Containing relevant links
* User stories - Each card in the format "As a [User]..., I want... [Feature], so that... [Details]"
* Backlog - 
* In-Progress - This list contains any tasks that is currently being worked on
* Testing - This list contains features that need to be tested
* Complete - Contains all tasks that are complete
* Issues - Each card here represents an issue which I struggled with

![Trello](https://user-images.githubusercontent.com/73299366/103594241-fe910800-4eef-11eb-8c7e-d92fcff145f1.JPG)

### ERD
The original ERD I created featured an additional table on the database (other than users and posts table), which was a comment section. The original ERD is shown below. It features a one to many relationship between User and Post and a one to many between relation between Post and Comment as well as User to Comment. A user can have many posts and make many comments, but each post must have one user and each comment must have one user and one post. 

![First_erd](https://user-images.githubusercontent.com/73299366/103592952-54fc4780-4eec-11eb-9de1-604bd0230630.JPG)

The ERD shown below is the one I decided to move on with, which is a simple one to many relationship between User and Post. For the first sprint, this will do the job and should meet the MVP.

![Second_erd](https://user-images.githubusercontent.com/73299366/103592969-5fb6dc80-4eec-11eb-8e33-332d4f90279d.JPG)

### CI Pipeline

![Ci_Pipeline](https://user-images.githubusercontent.com/73299366/103595546-a0662400-4ef3-11eb-9a26-09ad8a2478ef.JPG)

### Risk Assessment
Original risk assessment
![First_Risk](https://user-images.githubusercontent.com/73299366/103595638-d7d4d080-4ef3-11eb-8cb9-75a797be5f0a.JPG)

Final risk assessment
![Second_Risk](https://user-images.githubusercontent.com/73299366/103595659-e15e3880-4ef3-11eb-99be-5fcea22be88c.JPG)

## CRUD functionality 
This section will discuss the basic workings of the website. 

## Login page
![login_page_1](https://user-images.githubusercontent.com/73299366/103596057-f1c2e300-4ef4-11eb-967f-aef122d205bd.JPG)
![login_page_2](https://user-images.githubusercontent.com/73299366/103596066-f5566a00-4ef4-11eb-9d40-ded29d54fc14.JPG)
![login_page_3](https://user-images.githubusercontent.com/73299366/103596073-f8e9f100-4ef4-11eb-947f-4366b60756ce.JPG)

## Main page
![main_page_1](https://user-images.githubusercontent.com/73299366/103596109-0e5f1b00-4ef5-11eb-9768-f057d31aadec.JPG)
![main_page_2](https://user-images.githubusercontent.com/73299366/103596110-1028de80-4ef5-11eb-9364-77730fc47304.JPG)
![main_page_3](https://user-images.githubusercontent.com/73299366/103596113-11f2a200-4ef5-11eb-8670-4b0964cdcdb2.JPG)
![main_page_4](https://user-images.githubusercontent.com/73299366/103596117-1454fc00-4ef5-11eb-9196-f36b7e215bf7.JPG)
![main_page_5](https://user-images.githubusercontent.com/73299366/103596124-174fec80-4ef5-11eb-8903-b83cad2c6b49.JPG)
![main_page_6](https://user-images.githubusercontent.com/73299366/103596129-1919b000-4ef5-11eb-8000-cb3e5a50447b.JPG)


