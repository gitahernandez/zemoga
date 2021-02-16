# Zemoga Assestment

## Setup Manually

First of all you need to clone the repository:

```sh
$ git clone https://github.com/gitahernandez/zemoga.git
$ cd zemoga
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ mkvirtualenv -p python3.6.11 zemoga
$ workon zemoga
```

Then install the dependencies:

```sh
$ (zemoga)pip install -r requirements.txt
```

```sh
(zemoga)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Run using Docker

### Install

    git clone https://github.com/gitahernandez/zemoga.git
    cd dockerfile
    docker build -t zemoga .

### Run

Run the image and binding associated ports

    docker run -dp 8000:8000 zemoga
    
And navigate to `http://127.0.0.1:8000/`.
