from flask import Flask
from database import db
from routes.payroll import payroll_bp
from routes.chatbot import chatbot_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payroll.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(payroll_bp, url_prefix='/payroll')
app.register_blueprint(chatbot_bp, url_prefix='/chatbot')

@app.route('/')
def index():
    return "Payroll Assistant API is running!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)