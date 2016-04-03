# scrape_quora

A Python module to fetch and parse data from Quora user profiles. 

### Projects built using pyquora
* [`QUserAPI`](https://github.com/hansika/QUserAPI) – A REST API to get data from Quora user profiles.


## Installation
* You will need [Python 2](https://www.python.org/download/). 
* [pip](http://pip.readthedocs.org/en/latest/installing.html) is recommended for installing dependencies.

Install using pip:

    pip install scrape_quora

## Usage

```python

from scrape_quora import Scrape_Quora

name = Scrape_Quora.get_name('Hansika-Hewamalage')

```

## Features
### Currently implemented
Retrieve
* Profile Name
* URL
* Profile Picture Link
* No of Questions
* No of Answers
* No of Followers
* No of Following
* No of Edits


### Todo
Retrieve
* Facebook Profile Link
* Twitter Link
* Wordpress Link
* LinkedIn Link





