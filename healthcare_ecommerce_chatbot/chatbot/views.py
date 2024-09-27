from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatHistory
from .serializers import ChatHistorySerializer
from gradio_app.app import demo  # Import Gradio app

class ChatView(APIView):
    def post(self, request):
        user_message = request.data.get("message")
        # Process message with Gradio
        response = demo(user_message)
        
        # Save chat history
        chat_entry = ChatHistory(user_message=user_message, bot_response=response)
        chat_entry.save()
        
        return Response({"response": response})
