# Event Link 
> **Last Updated:** June 2, 2025

## Project Summary
_Event Link_ is a self made website thats tailored for groups of students/individuals to sign up for their local events. 

### Website Features
- Able to see past, present, and upcoming events
- Quickly RSVP with events on the events page or RSVPing with an event from the more details page
- Seeing how many users has RSVP with events from more details page with a speciific event
  + Displays text for past events informing users that RSVP is unavailable since the event has pasted
- Stores information within a database such as individuals names and emails as well as every event created
- Displays detailed text when there are no upcoming events and/or no past events within the system
- A clean and modern site design that catchs the users engagement

I came up with this idea for a class final where we needed to use all of our knowledge from what we learned in class to implement it all in one project. I wanted to create a main area for communities to share their events with others in one space without other users crossing to other platforms to find events that fit for them. 

### Coding Languages Used:
- Python
- Django (Python Framework)

## Getting Started
With this project using Django for the framework, you have to make sure that it's installed properly. 

### Prerequisites
You should have python already installed on your designated device. You can find an installation guide on Python's official website to install if you haven't already. 

### Installation
Now we'll be installing Django properly which is the only installation, after python, needed for this project to work. 

1. Installing django. Open command prompt on your device and input this code: 
```
py -m pip install Django==5.2.1
```
Aftewards, you should be ready to go to run the project. If you want to run the website, continue with the installation section.

2. While still in command prompt, change your directory to where the project is located. Make sure that is one file outside the event link folder.
   
Heres an example of what your line should look like:
```
cd [... full location line where project is being stored ...]\EventLink
```

3. Now we'll be making migrations to ensure that the database as been created for the system.

Use the first line. After, it has been ran, use the second one. 
```
py manage.py makemigrations

py manage.py migrate
```

4. Inorder for you to access the database, we need to create superuser. Input the line of code and follow the directions once entered.
```
py manage.py createsuperuser
```
5. Once the super user has been created, you are now ready to run the site using this line.
```
py manage.py runserver
```
Now you have fully installed the project's nessessary requirements and are ready to use it to it's full potential. 

## Usage
The project be used as a simple area for students to find local events within their school as well as a managing system to keep records of every event being hosted.

## Contact
### Created by: Isaiah Adams
If you reached this far, Hello! I'm a undergraduate student at Arkansas Tech University whose studying in Computer Science as well as a minor in Business Administration. A goal of mine is to continue to create amazing projects like this one to not only showcase my current skills in coding but to also build the foundation for my aspiring career in software engineering. 

I've included my email and other social links to get in contact with me if you have any questions.

[LinkedIn ](www.linkedin.com/in/isaiah-j-adams) - Email: IJAdams1@outlook.com



