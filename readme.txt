Frontend and Backend are done separately. 

Frontend use the data from that api in the assignment. in frontend folder.

Backend uses Django and the data in database is for testing . not the data from the api the assignment offers.

So, Frontend and Backend are done separately.

backend in in backend folder. 



Frontend:

click index.html in frontend folder, will see the result.

see screenshot frontend and backend  in screenshots_see_here folder

Backend:  the following is for backend.

follow the steps to run:
1.  using django
2.pip install -r requirements.txt (install in the project folder )
3. python manage.py runserver
4.http://127.0.0.1:8000/

Test backend functionalities:

Go to pycharm to test api.  click   Tools on  menu in pycharm and click -> HTTP Client -> Test Restful Web Service
( Right now, in the database, there are testing data. not  real data in the database.)

See screenhosts in screenshots_see_here folder for a reference to do the test.

1. Get a list of all stored taco recipes

HTTP method :  select GET
Host/port http://127.0.0.1:8000/

Path: input:  /api/recipe/
click green triangle button (run button )  to run it. You will see a list of all stored taco recipes. 
see screenshots 1

2. Get a list of tacos that match an ingredient search term
HTTP method : GET
Host/port  http://127.0.0.1:8000/
in Request Parameters:
name= ingredient，value=beef
Path:  /api/recipe/

click green triangle button (run button )  to run it. You will see a list of all stored taco recipes when ingredient = beef
see screenshots 2

3. GET a list tacos that match an ingredient category
HTTP method :GET
Host/port  http://127.0.0.1:8000/
in Request Parameters: name=category，value=meat
Path:  /api/recipe/

click green triangle button (run button )  to run it. You will see a list of all stored taco recipes when category = meat
see screenshots 3

4. GET a single taco by id
HTTP method 选中GET
Host/port http://127.0.0.1:8000/
Path:  /api/recipe/ID/ for example:  /api/recipe/1/ 

click green triangle button (run button )  to run it. You will see a single taco when id = 1
see screenshots 4

5. GET a list all ingredient in the taqueria inventory
HTTP method : GET
Host/port http://127.0.0.1:8000/
Path:  /api/ingredient/
click green triangle button (run button )  to run it. You will see a list all ingredient
see screenshots5

6. GET a list ingredients filtered by a category
HTTP method :GET
Host/port http://127.0.0.1:8000/
in Request Parameters
name=category，value=meat
Path:  /api/ingredient/
http://127.0.0.1:8000/
click green triangle button (run button )  to run it. You will see a list ingredients filtered by a category when category = meat
see screenshots 6

7.1 create tacos using ingredients in the ingredient inventory
HTTP method :POST
Host/port http://127.0.0.1:8000/
in Headers
name=Content-Type，value=application/json
in Request body  Text={"name":"taco","ingredients":[1]}
Path:  /api/recipe/
click green triangle button (run button )  to run it. You will see a list ingredients filtered by a category when category = meat, because this ingredients are already exists , it will return the existing taco recipe. Wont create a new one.
see screenshots 7.1 and 7.1.1


7.2 update taco reicpes
HTTP method :PATCH
Host/port http://127.0.0.1:8000/
Headers
name=Content-Type，value=application/json
Request body:Text={"name":"taco","ingredients":[1]}
Path:   /api/recipe/ID/ for example /api/recipe/1/  will change id=1's recipe， to make this recipe as the content of text.
click green triangle button (run button )  to run it. You will see the taco recipes are updated. See creenshot 7.2 and 7.2.1

7.3 delete taco reicpes
HTTP method :DELETE
Host/port  http://127.0.0.1:8000/
in Headers
name = Content-Type，value=application/json
Path=  /api/recipe/ID/  for example : /api/recipe/1/ will delete  recipe
click green triangle button (run button )  to run it. You will see to delete recipe with id  = 1

Same testing precedure similiar as 7.2. no screenshots for this one.


8.1 create ingredient
HTTP method ：POST
Host/port http://127.0.0.1:8000/
In Headers
name=Content-Type，value=application/json
in Request body=Text, text ={"name":"g1","category":1}
Path:  /api/ingredient/
click green triangle button (run button )  to run it. You will see a new ingredient 
see screenshots 8.1 and 8.1.1

8.2 update ingredient
HTTP method =PATCH
Host/port http://127.0.0.1:8000/
Headers
name=Content-Type，value=application/json
in Request body Text={"name":"beef","category":1}
Path=  /api/ingredient/ID/ for example /api/ingredient/1/  to change the id=1 ingredient， to  the content in the text
click green triangle button (run button )  to run it. You will see

8.3 delete ingredient
HTTP method DELETE
Host/port http://127.0.0.1:8000/
Headers
name=Content-Type，value=application/json
Path /api/ingredient/ID/  for example : /api/ingredient/1/  will delete ingredient with id =1


9 login
HTTP method =POST
Host/port http://127.0.0.1:8000/
Headers
name=Content-Type，value=application/json
Request body Text={"username":"test","password":"123qweasd"}
Path  /api/auth/login
save the value of  access （ note: only the value of access), it will be used in the later testing.

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE3MzY1MzIzLCJqdGkiOiIwZTdlNzY5ZjFjZDY0MTNmOTBjNTE4NjY1NGFiNDI4MiIsInVzZXJfaWQiOjF9.-iLpebd5s6lZrM7uewDCFSOwELrCN9SsGpQicva-wgM
see screenshot 9.1 and 9.11

10.1 create menus
HTTP method POST
Host/port http://127.0.0.1:8000/
in Headers
name=Content-Type，value=application/json
name= Authorization， value = JWT+one space + value of access
for example:
value= JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4NTkxMzE2NiwianRpIjoiNzdiODBmYjQ4ZTkwNGRkNDg3YzAyZGQxZTk1NDliYjMiLCJ1c2VyX2lkIjoxfQ.YIPa5XI87BAzBUa3pyYlqab3WrNqgSWm4OEtBbCKrJA","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE3MzYyNzY2LCJqdGkiOiJlN2Q3M2ZiN2E3ZTE0ZjNiOGI5YjM4MDU0M2NmOGE4YSIsInVzZXJfaWQiOjF9.LU-22Tzigl8QXzvJ5yjRQMBBSpXm-j21tFy7r3IvM94

Request body Text,={"name":"menu1","recipes":[1]}
Path  /api/menus/
see screenshot 10.1 and 10.11

10.2 update menus
HTTP method PATCH
Host/port http://127.0.0.1:8000/
Headers
name=Content-Type，value=application/json
Headers
name  Authorization，value=JWT+one space + value of access
Request body Request body text={"name":"menu1","recipe":[1]}
Path  /api/menus/ID/  for example /api/menus/1/ change menu to the content in the text


10.3 delete menus
HTTP method DELETE
Host/port http://127.0.0.1:8000/
in Headers
name=Content-Type，value=application/json
Headers
name Authorization，value=JWT+one space + value of access
Path  /api/menus/ID/ for example /api/menus/1/ will delete the  menus

10.4 read menus
HTTP method GET
Host/port http://127.0.0.1:8000/
Headers
name=Content-Type，value=application/json
Headers
name Authorization，value=JWT+one space + value of access
Path  /api/menus/ID/  for example : /api/menus/1/  will get menus with id = 1



test pdf:
login to http://127.0.0.1:8000/admin and go back to 
http://127.0.0.1:8000/api/menus/pdf/     

will see and downlod pdf version.

notes:

*python manage.py createsuperuser  to create a new super user


*you can see the admin site:
http://127.0.0.1:8000/admin
username：  test
password:  123qweasd





