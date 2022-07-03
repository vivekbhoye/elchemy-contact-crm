# elchemy-contact-crm

# Assignment requirement :

1. User Login and Registration 
- it also includes user verification through email functionality.

2. Customer Information Screen 
- View/Add/Delete/Update Customer information(Name, email, phone, address, GST No., frequency of automated reminder)

3. CRM Screen 
- For each of the customer, a contact screen has to be made where the user can see the history of past communications. He can add the communications made with timestamp information, conversation information. Also there should be a functionality to directly send mail to the customer from the app itself(fetch the email of the user automatically from database)

# All Views details with functionality :
User View :
1. HomePage : All Customers are shown with functions are as follows:
    - To Add Customer
    - To Delete Customer
    - To Update Customer
    - Clicking on any info of customer will redirect to that customers all communications View.
2. All Communications View : \
Contains all communications of all Customers with functions to :
    - To Add Communications
    - To Delete Communications
    - To Update Communications
    - to send email to that customer and email info will be added to that customers Communications list.
3. Communications View of particular customer : \
Contains all communications of That Customers with functions to :
    - To Add Communications
    - To Delete Communications
    - To Update Communications
    - to send email to that customer and email info will be added to that customers Communications list.

4. User Signup View : \
User can be register in Signup View and email will be sent to their email address after confirming that account will be activated and user can login.

5. User Login View :  
User can login by using username login method.

Anonymous View : 
- All views Without ability to add, delete, update functions.

## Authors

- [@vivekbhoye](https://github.com/vivekbhoye)

## Prerequisites
1. Python 3
2. python3-venv (if-needed)
 ```sudo apt-get install python3-venv```
## Installation

1. Clone git repository

```bash
  git clone https://github.com/vivekbhoye/elchemy-contact-crm
  cd elchemy-contact-crm
```

2. Create new virtual environment and activate it.
  replace path/to/directory with your path 
```bash
  python3 -m venv .venv
  source "path/to/directory/elchemy-contact-crm/.venv/bin/activate"
```
3. install all dependency using below command.

```bash
  pip install -r requirements.txt
```
4. now in project folder config/settings.py replace your Postgresql database settings.
```bash
DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.postgresql_psycopg2', 
        'NAME'    : 'contact_crm',                 # database name 
        'USER'    : 'test',                     # user name
        'PASSWORD': 'Secret_1234',              # password
        'HOST'    : 'localhost',                # host name
        'PORT'    : '3306',                     # Port no 
    }
}
```
5. now create table using following command.
```bash
  python manage.py makemigrations
  python manage.py migrate
```
6. after migrations. Run server using below command.

```bash
  python manage.py runserver
```

7. now navigate to http://127.0.0.1:8000/ 

## Third Party Packages
Django Crispy forms : for forms visual appearance and Validation.
## Screenshots

User Signup/Register ( confirmation Email will be sent to email address.  )
<kbd> 
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/Signup_View.png?raw=True)
</kbd>

User Email sent \
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/mail_sent.png?raw=True)
</kbd>

Mail Confirmation \
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/confirm_link.png?raw=True)
</kbd>

User Login Page
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/Login_View.png?raw=True)
</kbd>

Logged in User View 
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/Login_User_Home_View.png?raw=True)
</kbd>

Add Customer 
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/Create_Customer.png?raw=True)
</kbd>

Update Customer 
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/Update_Customer.png?raw=True)
</kbd>

Delete Customer 
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/Delete_Customer.png?raw=True)
</kbd>

Particular Customer Communication View ( all communication with that customer are listed )
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/Particular_Customer_Communications.png?raw=True)
</kbd>

Particular Customer's create new Communication ( here Customer Nana patekar's new communication)
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/Create_Communication_For_Particular_Customer.png?raw=True)
</kbd>

Communication Update View
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/Update_Communication_For_Particular_Customer.png?raw=True)
</kbd>

Communication Delete View
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/Delete_Communication_For_Particular_Customer.png?raw=True)
</kbd>

Communication Send email to that customer View
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/Sendmail_Communication_For_Particular_Customer.png?raw=True)
</kbd>

All communications View 
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/All_Communications.png?raw=True)
</kbd>

new Communication for any Customer choose View
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/any_new_communication.png?raw=True)
</kbd>

Anonymous User View 
<kbd>
![App Screenshot](https://github.com/vivekbhoye/elchemy-contact-crm/blob/master/Screenshots/Anonymous_User_View.png?raw=True)
</kbd>

