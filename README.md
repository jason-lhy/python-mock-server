# Mock Server

A simple mock server application written in python.

## Required Tools & Versions
- MySQL 8.0.20
- Python 3.8.0
- Pyenv
- Pyenv virtualenv

## Setup
1. Run `migrations/1.sql` in your database
2. Export the following enviornment variable
`DB_USER` Database user username
`DB_PW` Database user password
(Optional) `DB_HOST` Database host, default `127.0.0.1`
(Optional) `DB_PORT` Database port, default `3306`
3. Run `pyenv virtualenv 3.8.0 mock-server`
4. Navigate to project root directory
5. Run `pip install -r requirements.txt`
6. Run `flask run`
Your mock server will start at port 5000
