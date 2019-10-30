
# Scribble

![](https://dl.dropboxusercontent.com/s/8frf8rblw6pnpds/hipsterlogogenerator_1438007087793.png?dl=0)

Scribble is a Django application where users can read, write and interact
with the best content all around the world. It is designed to be built, refined and deployed over the course of four nights.

## Submitting

Fork this repo, and submit homework as a pull request on this repo...

```
$ cd scribble
$ virtualenv .env -p python3
$ source .env/bin/activate
$ pip3 install Django
$ pip3 install psycopg2
$ pip3 freeze > requirements.txt
$ django-admin startproject scribble_project .
$ django-admin startapp scribble
```
> When asked if you want to overwrite the readme, enter "n" (for no).

The `.` creates a new Django app inside the *CURRENT* folder. Otherwise, it creates a new folder. 

<!-- For instance, if you did `rails new scribble` it would create a `scribble` folder and put the Rails app inside there. -->

> This is how a lot of people end up with a `scribble` folder inside another `scribble` folder.

## Specifications

### Models + Migrations

1. Create [models](https://git.generalassemb.ly/sf-wdi-48/django-models#models) for Post and Comment
2. Create [migrations](https://git.generalassemb.ly/sf-wdi-48/django-models#migrations) for Post and Comment

We will start off with two models: `Post` and `Comment`.

A `Post` should have an `author`, `title`, and `body` (these can all be `CharField`s). A `Comment` should have an `author`, `body`, and a `post`. The `author` and `body` model attributes can be `CharField`s but `post` should be a `ForeignKey`.

