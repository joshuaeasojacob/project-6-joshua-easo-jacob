# My Expense Tracker

## Project Description
A simple expense tracking web application built using Python and Flask.

## Features
- Homepage to record expenses
- Add expenses using a POST form
- Input validation
- Display recorded expenses
- Calculate total expenses
- About and health routes

## Technologies
- Python
- Flask
- HTML
- Jinja templates

## Installation
Install dependencies:
pip install -r requirements.txt

Run the application:
python app.py

Open http://127.0.0.1:5001 in your browser.

## Routes
- GET / : Homepage
- GET /about : About page
- GET /health : Health check
- POST /add : Add an expense

## Limitation
Expenses are stored temporarily in memory and are cleared when the server restarts.
