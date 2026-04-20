from flask import Blueprint, request, jsonify
from services.simulation_service import run_simulation

simulation_bp = Blueprint('simulation', __name__)

@simulation_bp.route('/simulate-improvement', methods=['POST'])
def simulate():
    data = request.json

    income = data['income']
    transactions = data['transactions']
    reduce_expense = data.get('reduce_expense_by', 0)
    increase_income = data.get('increase_income_by', 0)

    result = run_simulation(income, transactions, reduce_expense, increase_income)

    return jsonify(result)