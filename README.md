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
    %% Frontend Layer
    NGO([🟢 NGO Portal<br/>Web App]) --> |Upload Project Data| API[⚡ API Gateway]
    Auditor([🟠 Auditor Portal<br/>Web App]) --> |Verify Projects| API
    Customer([🔵 Customer Portal<br/>Web App]) --> |Buy Carbon Credits| API

    %% Backend Layer
    API --> BE[🖥️ Backend Services<br/>Node.js]
    BE --> DB[(🗄️ Database<br/>MongoDB)]
    BE --> AUTH[🔐 Auth Service<br/>OAuth2]

    %% Blockchain Layer
    BE --> SC[⛓️ Smart Contracts<br/>Ethereum]
    SC --> BC[🟣 Blockchain Ledger]
    BC --> REG[📑 Carbon Credit Registry<br/>Immutable Records]

    %% Styling
    style API fill:#ffe6cc,stroke:#333,stroke-width:2px
    style BE fill:#e6f2ff,stroke:#333,stroke-width:2px
    style DB fill:#ffffcc,stroke:#333,stroke-width:2px
    style AUTH fill:#ccffcc,stroke:#333,stroke-width:2px
    style SC fill:#f9ccff,stroke:#333,stroke-width:2px
    style BC fill:#f2ccff,stroke:#333,stroke-width:2px
    style REG fill:#bbf,stroke:#333,stroke-width:2px

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