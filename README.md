# Furniture Inventory Management System

## Description
A furniture inventory management system for a furniture store. The system allows users to add, update, and delete furniture items, as well as track their availability and location within the store.

## Setup Instructions

### Local Development

1. *Clone the repository:*

   
   git clone https://github.com/ambikasriv/furniture_inventory.git
   cd furniture_inventory
Create a virtual environment and install dependencies:


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
Run the application: python run.py


Testing
To run the tests, use the following command:


python -m unittest discover -s tests
Docker
To build and run the Docker container, use the following commands:

docker-compose up --build
CI/CD
This project uses GitHub Actions for CI/CD. The workflow configuration can be found in .github/workflows/ci.yml.