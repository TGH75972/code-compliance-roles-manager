# Role & Permissions Manager for Code Compliance Research

A modular, lightweight role and permissions management system built for open-source code compliance workflows and security research environments (e.g., FOSSology-style compliance tools and repositories handling reverse-engineering research like `reverse-engineer-anything`).

This tool enforces the **Principle of Least Privilege**, provides dynamic web-based role assignment, and maintains a **tamper-evident, append-only audit log** for every permission modification to ensure strict legal and technical accountability.

---

## Project Overview & Theme

In code compliance research, handling third-party binaries, decompiled software, and legal licensing disclosures requires fine-grained access governance. Standard single-tier admin/user permission models create severe security and compliance vulnerabilities:
- **Reviewers** examining license findings should not have self-approval privileges.
- **Approvers** must sign off on legal clearances without modifying underlying static analysis tools.
- **Auditors** require read-only verification access without the ability to alter compliance historical records.

This project bridges that gap by providing a structured permission model, an intuitive web management interface, and immutable audit logs.

---

## Features

- **Granular Role Definitions**: Built-in support for **Reviewer**, **Approver**, **Auditor**, **Core Researcher**, and **Repository Administrator** roles mapped explicitly to granular permission flags (`read_findings`, `edit_clearing`, `sign_off_approval`, `export_audit`).
- **Web-Based Role Assignment UI**: Clean, responsive frontend built with standard HTML5, CSS3, and modern Vanilla JavaScript to manage user roles dynamically.
- **Append-Only Audit Logging**: Every privilege change records actor ID, target user ID, previous role, updated role, reason, and an ISO-8601 timestamp.
- **Filterable Audit View**: Search, sort, and query permission modification records by user, date range, or action type.
- **Snapshot Exports**: Single-click downloadable reports of role assignments and active permission matrices in CSV and JSON formats.
- **High Test Coverage**: Unit tests designed to achieve >85% code coverage using Python's `unittest` framework and automated via GitHub Actions CI.

---

## System Architecture & Data Flow

```
[ Admin / User ] ──► [ Web UI (HTML/CSS/JS) ]
                             │
                             ▼ (REST API / Schema Validation)
                 [ Python Backend Governance Engine ]
                 ├── Validates Role Mapping & Schemas
                 ├── Enforces Access Rules & Protections
                 └── Appends to Audit Log
                             │
            ┌────────────────┴────────────────┐
            ▼                                 ▼
[ Immutable Audit Trail ]         [ CSV / JSON State Snapshots ]
```

---

## Tech Stack

- **Backend**: Python 3 (`json`, `csv`, `unittest`, `datetime`)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript (ES6+)
- **Version Control & CI/CD**: Git, GitHub, GitHub Actions
- **Data Schemas**: JSON / CSV structured mappings

---

##  Quick Start Guide

### Prerequisites
- Python 3.8 or higher installed on your system.
- Modern web browser (Chrome, Firefox, Edge, Safari).

### Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/role-permissions-manager.git
   cd role-permissions-manager
   ```

2. **Verify Environment**:
   ```bash
   python3 --version
   ```

3. **Run Unit Tests**:
   Ensure all role mappings and logging mechanisms pass local validation checks:
   ```bash
   python3 -m unittest discover tests/
   ```

4. **Launch Application**:
   Start the local backend service/server:
   ```bash
   python3 main.py
   ```
   Open your browser and navigate to `http://localhost:8000` to interact with the role assignment UI.

---

## Security & Governance Model

| Role | Read Findings | Edit Clearing | Sign-off Approval | Export Audit | Manage Settings |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Auditor** | ✅ | ❌ | ❌ | ✅ | ❌ |
| **Reviewer / Researcher** | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Approver / Lead** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Administrator** | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## Testing & CI

Continuous Integration is pre-configured using GitHub Actions. Every `push` or `pull_request` against the `main` branch triggers:
1. Automated execution of unit test suites.
2. Code coverage calculation ensuring the project meets the **>85% code coverage** standard.
3. Verification of JSON/CSV schema validations.

---

## License & Attribution

Developed as part of the **On-the-Job Training (OJT) Open Source Track** by **Harshit Yadav**, conforming to FOSSology design patterns and compliance research standards.