import React from "react";

export default function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container-fluid">
        <a className="navbar-brand" href="/">💼 Payroll Assistant</a>
        <div className="collapse navbar-collapse">
          <ul className="navbar-nav ms-auto">
            <li className="nav-item"><a className="nav-link" href="/">Dashboard</a></li>
            <li className="nav-item"><a className="nav-link" href="/payslips">Payslips</a></li>
            <li className="nav-item"><a className="nav-link" href="/employees">Employees</a></li>
          </ul>
        </div>
      </div>
    </nav>
  );
}
