import React from "react";

export default function Dashboard() {
  return (
    <div className="container mt-4">
      <h2>📊 Payroll Dashboard</h2>
      <div className="row mt-3">
        <div className="col-md-4">
          <div className="card p-3 shadow">
            <h4>Total Employees</h4>
            <p>120</p>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card p-3 shadow">
            <h4>Monthly Payroll</h4>
            <p>₹12,00,000</p>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card p-3 shadow">
            <h4>Pending Requests</h4>
            <p>8</p>
          </div>
        </div>
      </div>
    </div>
  );
}
