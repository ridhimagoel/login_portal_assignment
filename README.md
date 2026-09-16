# Log Portal API Client & Device Controller

A Python-based automation tool for interacting with a secure log monitoring portal. This project demonstrates API authentication, token-based authorization, log monitoring, device discovery, and remote device control using REST APIs.

## Features

- User authentication through Login API
- Bearer token-based authorization for protected endpoints
- Continuous log monitoring with periodic API polling
- Fetch available devices and user permissions
- Toggle authorized device states through API requests
- Modular Python architecture for clean and reusable code

## Project Structure
login_portal_assignment/
│
├── api_client.py # Handles API communication (login, logs, controls, toggle)
├── log_stream.py # Manages continuous log monitoring
├── main.py # Application entry point and user interaction
└── README.md

## Setup Instructions
Clone the repository:
git clone <repository-url>
cd login_portal_assignment

## Install dependencies:
pip install requests

## Run the application using:
python main.py
