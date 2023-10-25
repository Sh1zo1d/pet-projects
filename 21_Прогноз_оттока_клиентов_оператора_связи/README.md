# Project Description:

The goal of this project is to develop a model for predicting customer churn in a telecommunications operator. To achieve this, we will use customer's personal data, information about the selected tariffs, and services. The main objective of the project is to create a model capable of predicting whether a subscriber is going to terminate the contract with the operator. This will enable the operator to proactively retain such users by offering them promo codes and special retention offers.

# Description of Services:

## The operator provides two main types of services:

1. Fixed-line telephone services, allowing customers to connect multiple lines simultaneously.
2. Internet services, available in two types: Digital Subscriber Line (DSL) and Fiber Optic.

In addition, customers have access to a range of services, including:
- Internet security (Device Protection) with antivirus and blocking of dangerous websites (Online Security).
- Dedicated technical support line (Tech Support).
- Cloud file storage for data backup (Online Backup).
- Streaming TV services (Streaming TV) and a catalog of movies (Streaming Movies).

Customers have the option to pay for services on a monthly basis or every 1-2 years. Various payment methods are available, and customers can receive electronic invoices.

### Data Description:

The data is stored in a PostgreSQL database, which consists of several tables:
- contract: Information about customer contracts.
- personal: Personal customer data.
- internet: Information about internet services.
- phone: Information about phone services.

Here are some key columns in these tables:

### Table: telecom.contract
- customerID: Customer ID.
- BeginDate: Contract start date.
- EndDate: Contract end date.
- Type: Payment type (e.g., yearly or monthly).
- PaperlessBilling: Electronic billing option.
- PaymentMethod: Payment method.
- MonthlyCharges: Monthly expenses.
- TotalCharges: Total customer expenses.

### Table: personal
- customerID: Customer ID.
- gender: Gender.
- SeniorCitizen: Whether the customer is a senior citizen.
- Partner: Whether the customer has a spouse or partner.
- Dependents: Whether the customer has dependents (children).

### Table: telecom.internet
- customerID: Customer ID.
- InternetService: Type of internet connection.
- OnlineSecurity: Security features like blocking dangerous sites.
- OnlineBackup: Cloud file storage for data backup.
- DeviceProtection: Antivirus service.
- TechSupport: Dedicated technical support.
- StreamingTV: Streaming TV services.
- StreamingMovies: Catalog of movies.

### Table: telecom.phone
- customerID: Customer ID.
- MultipleLines: Option to connect the phone to multiple lines simultaneously.
