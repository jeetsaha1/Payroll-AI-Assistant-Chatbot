import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import ChatbotWidget from './components/ChatbotWidget';
import PayslipViewer from './components/PayslipViewer';
import './styles/main.css';

const App = () => {
    return (
        <Router>
            <div className="App">
                <Switch>
                    <Route path="/" exact component={Dashboard} />
                    <Route path="/chat" component={ChatbotWidget} />
                    <Route path="/payslip" component={PayslipViewer} />
                </Switch>
            </div>
        </Router>
    );
};

export default App;