# Suit Shop API

## Identification of the problem you are trying to solve by building this particular app

This API serves as an online store web app, providing formal dress essentials from numerous brands. It can be intimidating to find the right suit for different occasions, such as weddings or finding a new job. However some of the features of this API aleviate the difficulty of this task.  This API controls the communication between consumer and the merchandiser. It can help users with their difficulties by allowing them to filter stock by avalaible quantity, total price and size, as well as comparing the different brands. The managers and admins are able to create, delete and alter any of the products and their information.

## Why is it a problem that needs solving?

Currently the fashion industry contributes to 10% of global carbon emissions. This API aims to provide the customer a service which can help them find exactly what they are looking for, and hopefully in turn reducde the amount of waste produced. If the API can successfully help them find exactly what they need in terms of correct size, approrporiate price and something for the right occasiom, hopefully this can reduce the potential of waste.

## Why have you chosen this database system. What are the drawbacks compared to others?

PostgresSQL is open source, making it possible for developers like myself to utilise it for free regardless of whether we use it for personal or business purposes. PostgresSQL is relatively simple to use and highly adaptable to the various OS systems used by people throughout the world. 
Even though PostgresSQL has numerous benefits, other RDMBS like MySQL load enormous volumes of data significantly more quickly. This is a potential disadvantage of using PostgresSQL.

## Detail any third party services that your app will use

The application does not yet use any third-party services to function. Orders entered on the client side may be filled by third-party services in later development versions.

## Describe your projects models in terms of the relationships they have with each other

### Users

The primary information used by the database is contained in the user model;

- An artificial ID (PK)
- email and password for authorisation and authentication - is admin to verify this user's permissions (CRUD Authority) - any other information that the user considers sensitive (shown in the ERD)
- The User model and the rest of the database are connected:
Products - Address

### Products

- The data referring to the available products is contained in the products model.
- The products can be filtered by brand, style, size, etc. by users with CRUD Authoritiy.

## Discuss the database relations to be implemented in your application

A "one-to-one relationship" is described between the Address Model and the User Model. This is due to the user id(FK), which connects the address to a particular user. For instance, if the user has a user id of "1," then the contents of the address that also have that user id will be directly linked to that user.
This indicates that just that user will be linked to by the URL with the supplied user id. As there is a one-to-one relationship between the User Model and the Address Model created by this API, the user cannot currently have numerous addresses and must update their address if they move.

### Insturctions for Database Step up

psql -U Postgres

CREATE DATABASE suitdevapi;

CREATE USER suitdev WITH PASSWORD '123';

GRANT ALL PRIVILEGES ON DATABASE suitshopapi TO suitdev;

\q

### Creating the Venv & Activation

python3 -m venv .venv

source .venv/bin/activate

### Install the Requirements

#### Download the requirements.txt found in the Repository

pip install -r requirements.txt

### Flask CLI Commands Shortcut

flask db drop && flask db create && flask db seed

flask db drop

flask db create && flask db seed
