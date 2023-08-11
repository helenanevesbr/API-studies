# API-studies
### Corona VS Tech
#### Description
An application that list which companies are hiring in corona times, which companies are firing and which are in a hiring freeze.  
If a user wants to add a company, we're getting an email to decide if we want to add this company to our company list.
#### Goal
Build a Django rest API for CRUDE operations and an email sending mechanism.  
Then a continuous integration system that is going to run our tests each time that we make a push and failure build if one of our tests failed.
#### What I've learned
- Pyenv
### My DVG Blog
#### Description
A small blogging application with CRUD operations. Authors can write many posts. Posts can have many tags and can be either published or unpublished. 
#### Goal
Build the back end of this blog in Django, complete with an admin for adding new blog content, then expose the content data as a GraphQL API.
#### What I've learned
- Build the Django blog **data model** and **admin interface**
- Wrap data model in a **GraphQL API** using Graphene-Django
#### Resource
Tutorial from [Real Python](https://realpython.com/python-django-blog/)  

---
### Send Notes for Gifts
#### Description
A REST API to keep track of notes for people that may visit you throughout the year: the Tooth Fairy, the Easter Bunny, and Knecht Ruprecht.  
You want to be on good terms with all three of them. That’s why you’ll send them notes, to increase the chance of getting valuable gifts from them.

#### Goal
Create a basic Flask project and connect endpoints to a SQLite database. Then test API with Swagger UI API documentation.

#### What I've learned
- Handle **HTTP** requests with **Connexion**
- Define API endpoints using the **OpenAPI** specification
- Build API documentation with **Swagger UI**
- Configure a **SQLite** database for my Flask project
- Use **SQLAlchemy** to save Python objects to my database
- Leverage the **Marshmallow** library to serialize data
- Work with **multiple tables** in a database
- Create **one-to-many fields** in my database
- Leverage **nested schemas** with Marshmallow

#### Resource
Tutorial from [Real Python](https://realpython.com/flask-connexion-rest-api/)