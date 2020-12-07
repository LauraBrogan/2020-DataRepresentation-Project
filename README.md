**2020 Data Representation Project**
 
***********************************************
<p align="justify">This repository contains my project A. Wed Application Project, for the Data Representation Moudule at GMIT.
I commenced work on 08 November 2020 and completed the task by the due date.

I struggeld in the early days of the project trying to get my to work correctly. This kinda put me off the project a bit initially.  I kept putting off this project because of my difficutlies at the early stage until I decided on a strategy to over come this and meet the deadline.  I have completed it although it maybe a bit basic. 

From completeing this project and overcoming my initial difficulties, in creating code, I can see that when creating any project of this nature, you must take small steps and work from the basis up and test as you go. When you can get one or two simple things to work you can build on them to create a more advanced project.</p>

[See here for the Project Instructions 2020](https://github.com/andrewbeattycourseware/dataRepresenation2020/blob/master/Project/Project%20Description.pdf)

## Introduction

In this project I create a basic Flask server that has a REST API, to perform CRUD operations, with one database tabee and the accompanying web interface, using AJAX calls to perform these CRUD operation.   I had intended on using two tables and had created them in mysql but only used the one as I had difficulty with getting this code to work. 

## My Respoitory Contains the following files:
-staticpages(index.html)

-.gitignore

-license

-PersonDao.py

-Project description.pdf

-READMe.md - which is this file

-dbconfigtemplate.py

-initdb.sql

-requirements.txt

-restserver.py

-testpersonDAO.py

-testSelect.py

## My Repositiory can be download from git hub 
1. Go to Git Hub using the following link [Click Here:](https://github.com/LauraBrogan/2020-DataRepresentation-Project)
2. Click the download button

## What Each File Contains:

**staticpages(index.html)**
This is my web interface which uses AJAX to perform the CURD operations.  It is the user interface for the database.

**PersonDao.py**
This file contains the data access object for my database. 

**dbconfigtemplate.py**
This is a copy of the dbconfig.py file that I created locally to run the server and connect to mysql, this will allow other user to bring this template to there local machine.

**initdb.sql**
This is the code used to create my table in mysql.

**requirement.txt**
This document contains the application installed in the vertual environment to run the flask server.
 
**restserver.py**
This file contains my code for the basic Flask Server that has a RESTA PI to perform CRUD operations.

**testpersonDAO.py**
This python file was used for testing the PersonDao.py as I went through the creation process of the PersonDAO.

**testSelect.py**
When python testSelect.py is ran on hte command line interface it returns all the items in the databased to the command line on cmd.exe

## References:
I used GMIT Video Lectures by Andrew Beatty and class notes to complete this work.

***Laura Brogan 07/12/2020*** 

