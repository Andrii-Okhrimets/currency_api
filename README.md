Description

This program works with API. For example: if you want to know the username or all its repositories, 
then you need to use API. Example: https://api.currencyfreaks.com/latest?apikey=YOUR_APIKEY&symbols=EUR,USD,UAH.
This way you get a json file and can get the information you are interested in.

INSTALLATION

You still need to install libraries:

''' pip install flask

pip install flask_sqlalchemy

pip install marshmallow flask-apispec

pip install requests

pip install pytest'''

Getting Started

To get started, you must first install the libraries listed above, and then clone the code and you can work with it.

We enter in the terminal: python app.py.
And we see that the program has started and we can use.

We can enter http://127.0.0.1:5000/swagger-ui/ in the address bar and see our methods there we can test.
But this will only work when we install the library: pip install marshmallow flask-apispec
