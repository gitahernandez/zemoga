# Zemoga Assestment Test (Python Developer)

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
    cd zemoga
    docker build -t zemoga .

### Run

Run the image and binding associated ports

    docker run -dp 8000:8000 zemoga
    
And navigate to `http://127.0.0.1:8000/`.

## Usage

![Image of Usage](https://i.ibb.co/Brr4Bgr/Screenshot-from-2021-02-15-21-57-19.png)


By default there are 3 files loaded:

* DATABASE_dataset_namespace_reference-csv.csv
* SCHEMA_equity_research_industry_classification_data.csv
+ DATA_equity_research_industry_classification_data.csv

Click on Link Datasets button to link files and generate error file (both in a zip file)

