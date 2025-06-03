# _**Event Link**_
> **Last Updated:** June 3rd, 2025

## Project Summary
**Event Link** is a self-developed web application designed to help individuals and student groups easily discover and register for local events. The platform serves as a centralized hub, eliminating the need to browse multiple platforms to find relevant events.

### Website Features
- View **past**, **current**, and **upcoming** events  
- RSVP directly from the **event list** or **event details** page  
- View RSVP count per event via the details page  
  - Past events are labeled and RSVP is disabled  
- Stores data such as names, emails, and event details in a database  
- Displays helpful messages when no events are available  
- Clean, modern UI optimized for user engagement  

> I came up with this idea for a class final where we needed to use all of our knowledge from what we learned in class to implement it all in one project. I wanted to create a main area for communities to share their events with others in one space without other users crossing to other platforms to find events that fit for them. 

---

### Coding Languages Used:
- **Python**
- **Django** (Python Framework)

---

## Getting Started
To run this project locally, follow the instructions below. The project is built using the Django web framework.

### Prerequisites
Ensure that **Python** is installed on your system. If not, refer to the [official Python installation guide](https://www.python.org/downloads/).

### Installation
Now we'll be installing Django properly which is the only installation, after python, needed for this project to work. 

1. **Installing Django**
Open your terminal or command prompt and run:
```
py -m pip install Django==5.2.1
```
Aftewards, you should be ready to go to run the project. If you want to run the website, continue with the installation section.

2. **Navigate to the Project Directory**
Change into the directory where the project is located:
```
cd [... full location line where project is being stored ...]\EventLink
```

3. **Run Migrations**
Initialize the database by running:
```
py manage.py makemigrations

py manage.py migrate
```

4. **Create a Superuser**
To access the Django admin dashboard:
```
py manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

5. **Launch the Development Server**
Once setup is complete, start the server:
```
py manage.py runserver
```
The application is now up and running!

## Usage
**Event Link** serves as an intuitive platform for students and local communities to find, RSVP to, and manage events within their network. The system also acts as an administrative tool for tracking hosted events.

## Contact
### Created by: Isaiah Adams
>LinkedIn: www.linkedin.com/in/isaiah-j-adams
>
>Email: IJAdams1@outlook.com

Hi there! I'm Isaiah, an undergraduate Computer Science major at Arkansas Tech University with a minor in Business Administration. My passion lies in developing meaningful software that connects people and solves real-world problems. Projects like this one allow me to apply classroom knowledge in a practical and impactful way, as I work toward a career in software engineering.

Feel free to reach out—I’d love to connect or answer any questions you may have.



