# Payroll Assistant with AI Chatbot

## Overview
The Payroll Assistant with AI Chatbot is a comprehensive solution designed to streamline payroll management and enhance employee engagement through an AI-powered chatbot. This project integrates core payroll functionalities with an intelligent assistant to provide real-time information and support to employees and HR personnel.

## Features
- **Core Payroll Management**
  - Employee database management
  - Salary calculation including deductions and allowances
  - Payslip generation in PDF format
  - Payroll accounting entries and compliance reporting

- **AI Chatbot Assistant**
  - Natural language processing for payroll-related queries
  - Employee self-service capabilities
  - HR/Admin reporting features

- **Security**
  - Role-based access control
  - Secure authentication mechanisms
  - Data encryption for sensitive information

- **Optional Advanced Features**
  - Voice assistant capabilities
  - Multilingual support
  - Integration with attendance systems
  - Predictive insights for payroll trends

## Tech Stack
- **Backend**: Python (Flask), SQLAlchemy, MySQL/PostgreSQL
- **Chatbot**: OpenAI GPT / Rasa / Dialogflow
- **Frontend**: React, HTML, CSS
- **Database**: MySQL/PostgreSQL

## Setup Instructions
1. **Clone the repository**
   ```
   git clone <repository-url>
   cd payroll-assistant-ai-chatbot
   ```

2. **Backend Setup**
   - Navigate to the `backend` directory.
   - Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the Flask application:
     ```
     python app.py
     ```

3. **Frontend Setup**
   - Navigate to the `frontend` directory.
   - Install the required npm packages:
     ```
     npm install
     ```
   - Start the React application:
     ```
     npm start
     ```

4. **Database Setup**
   - Execute the SQL schema in your database to create the necessary tables.

## Usage
- Employees can log in to access their payroll information and interact with the AI chatbot for queries.
- HR/Admin can utilize the chatbot for reporting and managing payroll-related tasks.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.