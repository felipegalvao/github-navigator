# Github Navigator

Github Navigator is built with Django. To use it, first you got to install the dependencies, which are:

* django
* requests
* selenium (only for tests)

You can install the dependencies through pip.

## Usage

Github Navigator uses the "requests" package to make a request to the Github API and return 
information from repositories using the search term provided.

After you start the server using Django, access localhost:8000/navigator and input the search term 
on the input box. You can also provide the search_term directly through the url 
(ex. localhost:8000/navigator/?search_term=arrow).

## Tests

Functional and unit tests are also provided. For the functional test, Selenium and Firefox with 
Geckodriver are required.