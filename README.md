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


## Run using docker

### Install

    git clone https://github.com/gitahernandez/zemoga.git
    cd dockerfile
    docker build -t zemoga .

### Run

Run the image, binding associated ports, and mounting the present working
directory:

    docker run -dp 8000:8000 zemoga
    
And navigate to `http://127.0.0.1:8000/`.
