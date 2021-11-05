## FastAPI Book_library
### This repository contains code of API for small book_library and build on the top of FastAPI framework.
### This book_library allows user through API to get info about it's books, book title and book author.
### Also it allows to get list of book
### Besides in this repository implemented filtering, possibility to use default parameters and data validation 
#### After cloning this repository don't forget to give it *!
#### To run code just activate virtual enviroment
#### Install requirements from req.txt file 
#### And then to run your code use:
    uvicorn mani:app
##### or
    uvicorn main:app --reload
##### to use autorestart after changing code
##### also you can specify which port you want to use with command
    uvicorn main:app --reload --port 8080
#### If you want to look through autodocumentation please visit
    localhos:8000/docs 
#### and you'll be redirected to swagger documentation or use 
    localhost:8000/redoc 
#### for alternative version.

    

     