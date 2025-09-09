# Blockchain-Based Blue Carbon MRV System

## Overview
This project is designed to create a **transparent, secure, and verifiable carbon credit system** using blockchain technology.  
It integrates multiple stakeholders such as NGOs, Auditors, and Customers into a single ecosystem for efficient **Monitoring, Reporting, and Verification (MRV)** of blue carbon projects.

### Key Features
- **NGO Portal**: Uploads and manages project data.
- **Auditor Portal**: Verifies project authenticity and compliance.
- **Customer Portal**: Enables customers to purchase carbon credits.
- **Blockchain Layer**: Ensures immutability, transparency, and traceability of data.
- **Carbon Credit Registry**: Stores verified carbon credits for trading.
- **Database**: Maintains project and transaction metadata.

---

## System Flow

```mermaid
flowchart TD
    NGO[NGO Portal] --> |Upload Project Data| Backend
    Auditor[Auditor Portal] --> |Verify Projects| Backend
    Customer[Customer Portal] --> |Buy Carbon Credits| Backend

    Backend --> Blockchain[Blockchain Layer]
    Backend --> Database[(Database)]
    Blockchain --> Registry[Carbon Credit Registry]

    style Blockchain fill:#f9f,stroke:#333,stroke-width:2px
    style Registry fill:#bbf,stroke:#333,stroke-width:2px
````

---

## Tech Stack

* **Frontend**: React.js (Portals for NGO, Auditor, Customer)
* **Backend**: Node.js / Express
* **Blockchain**: Ethereum / Hyperledger Fabric
* **Database**: PostgreSQL / MongoDB
* **Registry**: Smart contracts for carbon credit issuance and transfer

---

## Future Scope

* Integration with IoT devices for automated project monitoring.
* AI-driven fraud detection in project validation.
* Global marketplace for carbon credits.