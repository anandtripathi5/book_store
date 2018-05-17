# book_store
flask boiler plate(12 factor app) with JWT and email implementation. Having basic usage of libraries and best practices


##### Book store is a application where you can rent number of books and the charges will be deducted according to number of books and charges of a particular book

## Usage and refer postman collection link for it 
> https://www.getpostman.com/collections/9ac824e67b809e877ab0

1.  First signup to application by providing username and password to following url
> http://18.221.10.136:8080/api/v1/signup
2. login using following url
> http://18.221.10.136:8080/api/v1/login?user_name=anand&password=password
3. get books availability details: get method
> http://18.221.10.136:8080/api/v1/book_store
4. delete book: delete method
> http://18.221.10.136:8080/api/v1/book_store
5. rent book: post method
> http://18.221.10.136:8080/api/v1/book_store
6. Check user statement
> http://18.221.10.136:8080/api/v1/user_statement

## Installation
Please follow following steps
* git clone https://github.com/anandtripathi5/book_store.git
* create virtual environment
```sh 
virtualenv book_store
```
* Activate virtualenv
```
source book_store/bin/activate
```
* Install dependencies
```
pip install -r requirement.txt
```
* run supervisor using supervisor.conf file and pass mysql url in env_var.env file
