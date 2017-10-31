# Udacity Full Stack Web Developer Project 3 - Logs Analysis Project

## Background
This is the third project from Udacity's course (Full Stack Web Developer). The aim of this project is to familiar with the SQL query with python. The database file does not commit to the repository. Please download the database file from Udacity for the full functionality.
## Environment
1.	PostgreSQL 9.5.9
2.	Python 3.5.2
## How to run the program
### main.py
The main program is **main.py**. You can directly execute **main.py** to generate the result.
```bash
python main.py
```
The output file (**output.txt**) is located at the same directory. All the source codes are located in the **query.py**.
### query.py
#### 1. class defined
*class* query.**Logs**(*database*)
This class creates an object to iterate the database provided. *database* parameter is defined as the name of database in PostgreSQL.
#### 2. Logs object
Logs instance has the following methods:
**Logs**.popularArticles(*number*)
This method returns an array containing the most popular articles in database in descending order. The returned articles are the tuple with the structure (name of article, number of access). *number* limits the number of results in the array. By default, it is defined as the maximum number of the articles in database, i.e. no limit.
**Logs**.popularAuthors(*number*)
This method returns an array containing the most popular authors in database in descending order. The returned authors are the tuple with the structure (name of author, number of access). *number* limits the number of results in the array. By default, it is defined as the maximum number of the authors in database, i.e. no limit.
**Logs**.errorReport()
This method returns an array containing the date that occur error with more than 1% in all request. The returned tuple has the structure (date, percentage of error).
## Acknowledge
Thank Udacity to provide guidance in the development.