from flask import Blueprint, request, jsonify
from services.chatbot_service import ChatbotService
from database import db

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    message = data.get('message')
    chatbot_service = ChatbotService(db.session)  # Pass db.session here
    response = chatbot_service.get_response(message)
    return jsonify({'response': response})