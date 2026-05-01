# GlobalTech Solutions Customer Management System

## 📌 Overview

The **GlobalTech Solutions Customer Management System** is a Python-based data management and analytics project that demonstrates the use of dictionaries and aggregation techniques.

This simulates a real-world business scenario where customers, services, and projects are managed and analyzed using Python core data structures.

---

## Features

### Customer Management

* Store customer records using nested dictionaries
* Retrieve and update customer data
* Validate customer information for completeness

### Service Catalog

* Maintain service categories with hourly rates
* Apply dynamic pricing adjustments
* Categorize services into pricing tiers (Basic, Standard, Premium)

### Project Tracking

* Assign multiple projects per customer
* Track project details:

  * Service type
  * Hours worked
  * Budget
  * Status tracking

### Data Analysis & Reporting

* Total hours across all projects
* Total and average budgets
* Maximum and minimum project budgets
* Customer-specific summaries
* Service usage frequency analysis

### Recommendation System

* Suggest services based on:

  * Customer history
  * Budget patterns
  * Previously unused services

---

## Data Structures Used

* Dictionaries (core structure)
* Nested dictionaries (customers, services)
* Lists of dictionaries (projects)
* Sets (service tracking)
* Dictionary comprehensions

---

## Key Functional Components

### Customer Validation

Ensures all required fields exist:

* company_name
* contact_person
* email
* phone

### Budget Analysis

Computes:

* Total budget per customer
* Average project budget
* Project counts

### Service Recommendation Engine

Recommends services based on:

* Unused services
* Budget compatibility
* Past project behavior

---

## ▶️ How to Run

1. Ensure Python 3 is installed

2. Navigate into the project directory:

```bash
cd globaltech-customer-system
```

3. Run the program:

```bash
python main.py
```

---

## Example Output

* Customer directory listing
* Project cost calculations
* Financial summaries
* Service usage breakdown
* Recommendation outputs

---

## Learning Outcomes

This project reinforces:

* Python dictionary operations
* Nested data handling
* Loops and conditionals
* Data aggregation techniques
* Real-world business logic simulation
* Comprehensions and functional decomposition

---
