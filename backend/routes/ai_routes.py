from flask import Blueprint, request, jsonify
from services.ai_service import generate_ai_response

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ask-ai', methods=['POST'])
def ask_ai():
    data = request.json

    question = data['question']
    income = data['income']
    transactions = data['transactions']

    response = generate_ai_response(question, income, transactions)

    return jsonify({"answer": response})