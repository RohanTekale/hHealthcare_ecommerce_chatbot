import os
import gradio as gr

# Set the settings module for Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "healthcare_ecommerce_chatbot.settings")

import django
django.setup()  # This sets up Django

from gradio_app.utils import process_response  # Now you can import your function

def demo(input_text):
    response = process_response(input_text)
    return response

if __name__ == "__main__":
    gr.Interface(fn=demo, inputs="text", outputs="text").launch()
