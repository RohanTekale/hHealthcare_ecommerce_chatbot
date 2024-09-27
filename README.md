# Healthcare E-commerce Chatbot

## Overview
This project is a healthcare-related e-commerce platform that includes a chatbot for assisting users with inquiries related to healthcare and e-commerce operations. The chatbot is built using Django for the backend and Gradio for the frontend interface.

## Project Structure
healthcare_ecommerce_chatbot/ │ ├── manage.py ├── chatbot/ │ ├── init.py │ ├── models.py │ ├── views.py │ ├── urls.py │ ├── serializers.py │ └── templates/ │ └── index.html ├── ecommerce/ │ ├── init.py │ ├── models.py # Product and Order models │ ├── views.py # Product and Order views │ ├── urls.py # E-commerce app URLs │ └── serializers.py # Serializers for Product and Order ├── healthcare_ecommerce_chatbot/ │ ├── init.py │ ├── settings.py │ ├── urls.py └── gradio_app/ ├── init.py ├── app.py └── utils.py


## Features
- **Product Management**: Manage products with attributes such as name, description, price, and stock quantity.
- **Order Management**: Handle user orders with statuses like pending, shipped, delivered, and canceled.
- **Chatbot Functionality**: Provide users with an interactive interface to get assistance on healthcare inquiries and e-commerce operations.

## Technologies Used
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Gradio**: A Python library for creating user-friendly interfaces for machine learning models.
- **SQLite/PostgreSQL**: Database for storing product and order data.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries, please reach out to:

Name: Rohan Tekale
Email: tekalerohan7@gmail.com
