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

## Software Design
### ERD
The original ERD I created featured an additional table on the database (other than users and posts table), which was a comment section. The original ERD is shown below. It features a one to many relationship between User and Post and a one to many between relation between Post and Comment as well as User to Comment. A user can have many posts and make many comments, but each post must have one user and each comment must have one user and one post. 

![First_erd](https://user-images.githubusercontent.com/73299366/103592952-54fc4780-4eec-11eb-9de1-604bd0230630.JPG)

The ERD shown below is the one I decided to move on with, which is a simple one to many relationship between User and Post. For the first sprint, this will do the job and should meet the mvp.

![Second_erd](https://user-images.githubusercontent.com/73299366/103592969-5fb6dc80-4eec-11eb-8e33-332d4f90279d.JPG)


### Trello Board

The trello board I created using trello.com is shown below. It shows all the user stories, backlog and all tasks either in in-progress , testing or complete.

![Trello](https://user-images.githubusercontent.com/73299366/103469160-16825380-4d59-11eb-8e5a-f97d27d46c4a.JPG)
