# FastAPI

 
 Credit to my Instructor Anton Appelblom for a job well done in teaching PYTHON to our class.
 

 FASTAPI Project creating my first RESTful-API app - Book Library app following the CRUD functions.
I eventually decided to use FastAPI instead of Django. I used first a fake database to test if the routes are working as it should be thru Swagger UI. Once everything was set up I then created a real database and connect it to the app. Lastly I successfully seeded a Json file containing sample data to the database. 

1. create a new virtual environment
		python -m venv env

	activate environment
		env\Scripts\activate
		
2.install required packages

	pip install fastapi uvicorn[standard] sqlalchemy databases[sqlite] python-multipart

3. Make the project directories

	FASTAPI directory

4. Create the first connection 
main.py

#main.py file and import the necessary packages:


create the CRUD (Create, Read, Update, Delete) functionality for the book library app.


5. Create the following files inside the project directory:

main.py
: This will be the main file where you will create the FastAPI app.

database.py
: This file will contain the code for connecting to the SQLite database.

models.py
: This file will define the SQLAlchemy models for the Book and Author objects.

schemas.py
: This file will define the Pydantic schemas for the Book and Author objects.

seed.py
: This file will contain the code to seed the database with initial data.

seed.json: This file will contain sample data for the app.
