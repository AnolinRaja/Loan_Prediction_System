import React, { useState } from 'react';
import '../styles/Form.css';

const Form = ({ onSubmit, loading }) => {
    const [formData, setFormData] = useState({
        income: '',
        loan_amount: '',
        credit_score: '',
        months_employed: '',
        age: '',
        dti_ratio: '',
        education: '1',
        employment_type: '1',
        marital_status: '1',
        has_mortgage: '0',
        has_cosigner: '0',
    });

    const [errors, setErrors] = useState({});

    /**
     * Validate form inputs
     * @returns {boolean} - true if valid, false otherwise
     */
    const validateForm = () => {
        const newErrors = {};

        if (!formData.income || formData.income <= 0) {
            newErrors.income = 'Income must be greater than 0';
        }
        if (!formData.loan_amount || formData.loan_amount <= 0) {
            newErrors.loan_amount = 'Loan amount must be greater than 0';
        }
        if (!formData.credit_score || formData.credit_score < 300 || formData.credit_score > 850) {
            newErrors.credit_score = 'Credit score must be between 300 and 850';
        }
        if (!formData.months_employed || formData.months_employed < 0) {
            newErrors.months_employed = 'Months employed must be 0 or greater';
        }
        if (!formData.age || formData.age < 18 || formData.age > 100) {
            newErrors.age = 'Age must be between 18 and 100';
        }
        if (!formData.dti_ratio || formData.dti_ratio < 0 || formData.dti_ratio > 100) {
            newErrors.dti_ratio = 'DTI Ratio must be between 0 and 100';
        }

        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    /**
     * Handle input change
     */
    const handleChange = (e) => {
        const { name, value, type } = e.target;
        setFormData({
            ...formData,
            [name]: type === 'select-one' ? value : (value === '' ? '' : parseFloat(value)),
        });
        // Clear error for this field when user starts typing
        if (errors[name]) {
            setErrors({
                ...errors,
                [name]: '',
            });
        }
    };

    /**
     * Handle form submission
     */
    const handleSubmit = (e) => {
        e.preventDefault();

        if (validateForm()) {
            onSubmit({
                income: parseFloat(formData.income),
                loan_amount: parseFloat(formData.loan_amount),
                credit_score: parseFloat(formData.credit_score),
                months_employed: parseFloat(formData.months_employed),
                age: parseFloat(formData.age),
                dti_ratio: parseFloat(formData.dti_ratio),
                education: parseInt(formData.education),
                employment_type: parseInt(formData.employment_type),
                marital_status: parseInt(formData.marital_status),
                has_mortgage: parseInt(formData.has_mortgage),
                has_cosigner: parseInt(formData.has_cosigner),
            });
        }
    };

    /**
     * Reset form
     */
    const handleReset = () => {
        setFormData({
            income: '',
            loan_amount: '',
            credit_score: '',
            months_employed: '',
            age: '',
            dti_ratio: '',
            education: '1',
            employment_type: '1',
            marital_status: '1',
            has_mortgage: '0',
            has_cosigner: '0',
        });
        setErrors({});
    };

    return (
        <div className="form-container">
            <h2>Loan Application Form</h2>
            <form onSubmit={handleSubmit}>
                {/* Primary Information */}
                <fieldset>
                    <legend>Personal Information</legend>
                    
                    <div className="form-group">
                        <label htmlFor="income">Annual Income ($)</label>
                        <input
                            type="number"
                            id="income"
                            name="income"
                            value={formData.income}
                            onChange={handleChange}
                            placeholder="Enter annual income"
                            disabled={loading}
                            required
                        />
                        {errors.income && <span className="error-message">{errors.income}</span>}
                    </div>

                    <div className="form-group">
                        <label htmlFor="age">Age</label>
                        <input
                            type="number"
                            id="age"
                            name="age"
                            value={formData.age}
                            onChange={handleChange}
                            placeholder="Enter your age"
                            disabled={loading}
                            required
                        />
                        {errors.age && <span className="error-message">{errors.age}</span>}
                    </div>

                    <div className="form-group">
                        <label htmlFor="education">Education Level</label>
                        <select
                            id="education"
                            name="education"
                            value={formData.education}
                            onChange={handleChange}
                            disabled={loading}
                        >
                            <option value="0">High School</option>
                            <option value="1">Bachelor's Degree</option>
                            <option value="2">Master's Degree</option>
                            <option value="3">PhD</option>
                        </select>
                    </div>

                    <div className="form-group">
                        <label htmlFor="marital_status">Marital Status</label>
                        <select
                            id="marital_status"
                            name="marital_status"
                            value={formData.marital_status}
                            onChange={handleChange}
                            disabled={loading}
                        >
                            <option value="0">Single</option>
                            <option value="1">Married</option>
                            <option value="2">Divorced</option>
                            <option value="3">Widowed</option>
                        </select>
                    </div>
                </fieldset>

                {/* Employment Information */}
                <fieldset>
                    <legend>Employment Information</legend>
                    
                    <div className="form-group">
                        <label htmlFor="employment_type">Employment Type</label>
                        <select
                            id="employment_type"
                            name="employment_type"
                            value={formData.employment_type}
                            onChange={handleChange}
                            disabled={loading}
                        >
                            <option value="0">Self-Employed</option>
                            <option value="1">Employed Full-Time</option>
                            <option value="2">Employed Part-Time</option>
                            <option value="3">Retired</option>
                        </select>
                    </div>

                    <div className="form-group">
                        <label htmlFor="months_employed">Months Employed</label>
                        <input
                            type="number"
                            id="months_employed"
                            name="months_employed"
                            value={formData.months_employed}
                            onChange={handleChange}
                            placeholder="Enter months employed"
                            disabled={loading}
                            required
                        />
                        {errors.months_employed && <span className="error-message">{errors.months_employed}</span>}
                    </div>
                </fieldset>

                {/* Loan Information */}
                <fieldset>
                    <legend>Loan Information</legend>
                    
                    <div className="form-group">
                        <label htmlFor="loan_amount">Loan Amount ($)</label>
                        <input
                            type="number"
                            id="loan_amount"
                            name="loan_amount"
                            value={formData.loan_amount}
                            onChange={handleChange}
                            placeholder="Enter loan amount"
                            disabled={loading}
                            required
                        />
                        {errors.loan_amount && <span className="error-message">{errors.loan_amount}</span>}
                    </div>

                    <div className="form-group">
                        <label htmlFor="credit_score">Credit Score</label>
                        <input
                            type="number"
                            id="credit_score"
                            name="credit_score"
                            value={formData.credit_score}
                            onChange={handleChange}
                            placeholder="Enter credit score (300-850)"
                            disabled={loading}
                            required
                        />
                        {errors.credit_score && <span className="error-message">{errors.credit_score}</span>}
                    </div>

                    <div className="form-group">
                        <label htmlFor="dti_ratio">Debt-to-Income Ratio (%)</label>
                        <input
                            type="number"
                            id="dti_ratio"
                            name="dti_ratio"
                            value={formData.dti_ratio}
                            onChange={handleChange}
                            placeholder="Enter DTI Ratio (0-100)"
                            step="0.01"
                            disabled={loading}
                            required
                        />
                        {errors.dti_ratio && <span className="error-message">{errors.dti_ratio}</span>}
                    </div>
                </fieldset>

                {/* Financial Details */}
                <fieldset>
                    <legend>Financial Details</legend>
                    
                    <div className="form-group checkbox">
                        <input
                            type="checkbox"
                            id="has_mortgage"
                            name="has_mortgage"
                            checked={formData.has_mortgage === '1'}
                            onChange={(e) => {
                                setFormData({
                                    ...formData,
                                    has_mortgage: e.target.checked ? '1' : '0',
                                });
                            }}
                            disabled={loading}
                        />
                        <label htmlFor="has_mortgage">Has Mortgage</label>
                    </div>

                    <div className="form-group checkbox">
                        <input
                            type="checkbox"
                            id="has_cosigner"
                            name="has_cosigner"
                            checked={formData.has_cosigner === '1'}
                            onChange={(e) => {
                                setFormData({
                                    ...formData,
                                    has_cosigner: e.target.checked ? '1' : '0',
                                });
                            }}
                            disabled={loading}
                        />
                        <label htmlFor="has_cosigner">Has Co-Signer</label>
                    </div>
                </fieldset>

                <div className="form-actions">
                    <button
                        type="submit"
                        className="btn btn-primary"
                        disabled={loading}
                    >
                        {loading ? 'Analyzing...' : 'Get Risk Assessment'}
                    </button>
                    <button
                        type="button"
                        className="btn btn-secondary"
                        onClick={handleReset}
                        disabled={loading}
                    >
                        Reset
                    </button>
                </div>
            </form>
        </div>
    );
};

export default Form;
