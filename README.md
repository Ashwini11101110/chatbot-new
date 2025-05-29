# Chatbot Project

## Overview
This project is a simple chatbot application developed using Python and Flask. It provides a web-based interface where users can interact with the chatbot for various purposes such as answering queries or providing assistance.

## Features
- User-friendly web interface using Flask
- Basic conversational abilities powered by Python logic
- Organized project structure with templates and static files
- Easy to set up and run locally

## Project Structure
chatbot_project/
├── app.py # Main Flask application file
├── templates/ # HTML templates for the web interface
├── static/ # Static files like CSS, JavaScript, images
├── venv/ # Python virtual environment (excluded from git)
├── pycache/ # Python cache files
├── .gitignore # Git ignore rules
└── README.md # Project documentation



## Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/Ashwini11101110/chatbot-new.git
cd chatbot-new
Create a virtual environment


python -m venv venv
Activate the virtual environment

On Windows:


venv\Scripts\activate
On macOS/Linux:


source venv/bin/activate
Install dependencies


pip install -r requirements.txt
(If you don't have a requirements.txt yet, you can generate it with pip freeze > requirements.txt after installing necessary packages.)

Run the app


python app.py
Open your browser

Navigate to http://127.0.0.1:5000 to interact with the chatbot.

Usage
Type your messages into the chat interface.

The chatbot will respond based on predefined logic.

Extend or modify app.py to add more conversational capabilities.

