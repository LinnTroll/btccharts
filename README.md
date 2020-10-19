## README

#### How to run local dev server:
`make migrate` to create database

`make start` to run all services

After running this command, the application should be available at http://127.0.0.1:8000/

#### How to load data from API:
Run `make load_data` to manually load data from the API.

Also, the data should be loaded every hour automatically.

#### How to run test:
`make test` runs backend unit tests.

`make lint` runs python code linter.
