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
flowchart LR
    subgraph Users[Stakeholders]
        NGO[NGO Portal]
        Auditor[Auditor Portal]
        Customer[Customer Portal]
    end

    NGO --> |Project Submission| APIGW[API Gateway + Load Balancer]
    Auditor --> |Verification| APIGW
    Customer --> |Purchase Request| APIGW

    subgraph BackendCluster[Backend Services]
        Service[Business Logic / Token Issuance]
    end

    APIGW --> Service

    Service --> DB[(Database)]
    Service --> Blockchain[Blockchain Layer]

    Blockchain --> Registry[Carbon Credit Registry]

    subgraph Optional[Optional Layer]
        CDN[CDN / Cache]
    end

    NGO --> |Upload Photos/Docs| CDN
    CDN --> Service

    style Blockchain fill:#f9f,stroke:#333,stroke-width:2px
    style Registry fill:#bbf,stroke:#333,stroke-width:2px
    style APIGW fill:#ffb,stroke:#333,stroke-width:2px
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