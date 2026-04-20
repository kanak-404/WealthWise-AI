from flask import Flask
from routes.finance_routes import finance_bp
from routes.simulation_routes import simulation_bp
from routes.ai_routes import ai_bp

app = Flask(__name__)

app.register_blueprint(finance_bp)
app.register_blueprint(simulation_bp)
app.register_blueprint(ai_bp)

@app.route('/')
def home():
    return "Server is running!"

if __name__ == "__main__":
    app.run(debug=True)