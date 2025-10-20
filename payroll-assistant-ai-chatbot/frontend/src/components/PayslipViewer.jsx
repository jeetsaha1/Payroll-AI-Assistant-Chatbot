import React, { useEffect, useState } from 'react';

const PayslipViewer = ({ employeeId }) => {
    const [payslip, setPayslip] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchPayslip = async () => {
            try {
                const response = await fetch(`/api/payslip/${employeeId}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch payslip');
                }
                const data = await response.json();
                setPayslip(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchPayslip();
    }, [employeeId]);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            <h2>Payslip for {payslip.month} {payslip.year}</h2>
            <p>Net Salary: ₹{payslip.netSalary}</p>
            <p>Basic: ₹{payslip.basic}</p>
            <p>HRA: ₹{payslip.hra}</p>
            <p>Allowances: ₹{payslip.allowances}</p>
            <p>Deductions: ₹{payslip.deductions}</p>
            <button onClick={() => window.open(payslip.pdfUrl, '_blank')}>
                Download Payslip
            </button>
        </div>
    );
};

export default PayslipViewer;