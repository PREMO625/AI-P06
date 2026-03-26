# AI P06 - Expert Systems Suite

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/UI-Gradio-FF4B4B?logo=gradio&logoColor=white)
![Paradigm](https://img.shields.io/badge/AI-Rule--Based%20Expert%20Systems-0EA5E9)
![Status](https://img.shields.io/badge/Status-Ready%20to%20Run-22C55E)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

This project contains six rule-based expert systems implemented in Python with Gradio interfaces.
Each system captures domain knowledge as explicit logic and transforms user inputs into explainable recommendations.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Setup and Installation](#setup-and-installation)
5. [How to Run](#how-to-run)
6. [Expert Systems Detailed Guide](#expert-systems-detailed-guide)
7. [How the Inference Works](#how-the-inference-works)
8. [Expected Outputs and Interpretation](#expected-outputs-and-interpretation)
9. [Troubleshooting](#troubleshooting)

## Project Overview

The suite demonstrates how expert systems can be used in practical decision-support scenarios:

- Information governance and data policy recommendations
- Hospital triage support
- IT help desk ticket prioritization
- Employee performance evaluation
- Educational stock trading signal generation
- Airline scheduling and cargo operations planning

Each module has:

- `backend.py`: the inference and rule engine
- `app.py`: the interactive Gradio UI

## Tech Stack

- Python
- Gradio
- Rule-based logic using deterministic scoring and condition rules

## Project Structure

```text
AI P06/
|-- requirements.txt
|-- info.md
|-- README.md
|-- I_Information_Management/
|   |-- app.py
|   `-- backend.py
|-- II_Hospitals_and_Medical_Facilities/
|   |-- app.py
|   `-- backend.py
|-- III_Help_Desks_Management/
|   |-- app.py
|   `-- backend.py
|-- IV_Employee_Performance_Evaluation/
|   |-- app.py
|   `-- backend.py
|-- V_Stock_Market_Trading/
|   |-- app.py
|   `-- backend.py
`-- VI_Airline_Scheduling_and_Cargo_Schedules/
    |-- app.py
    `-- backend.py
```

## Setup and Installation

Run from project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Installed dependency from `requirements.txt`:

- `gradio>=5.23.0`

## How to Run

Each system runs independently.
Open a PowerShell terminal in project root and use one of the following commands.

### Option A: Run from inside each folder

```powershell
cd .\I_Information_Management
python app.py
```

Repeat the same pattern for other folders.

### Option B: Run directly from root

```powershell
python .\I_Information_Management\app.py
python .\II_Hospitals_and_Medical_Facilities\app.py
python .\III_Help_Desks_Management\app.py
python .\IV_Employee_Performance_Evaluation\app.py
python .\V_Stock_Market_Trading\app.py
python .\VI_Airline_Scheduling_and_Cargo_Schedules\app.py
```

After launch, Gradio prints a local URL (typically `http://127.0.0.1:7860`) in terminal.
Open it in your browser and interact with the interface.

## Expert Systems Detailed Guide

### I. Information Management Expert System

#### What it is

A policy recommendation engine for classifying organizational data and prescribing security, retention, and backup actions.

#### Why it is used

- Enforces consistent data handling decisions
- Reduces policy ambiguity
- Supports governance and compliance workflows

#### Inputs

- Data Type: Operational, Financial, Legal, Employee Records, Knowledge Base
- Sensitivity: Low, Medium, High
- Access Frequency: Daily, Weekly, Monthly, Rarely
- Regulatory Requirement: Yes/No
- Business Criticality: Low, Medium, High

#### How it works

- Computes a weighted score from sensitivity, compliance need, criticality, access pattern, and data category
- Maps score to a classification bucket:
  - Public Knowledge
  - Operational Internal
  - Confidential Business
  - Restricted Critical
- Adds extra controls such as audit logs, encryption, and cold-tier movement based on conditions

#### Output

- Recommended Classification
- Policy Summary
- Action list (security, retention, backup, governance)
- Inference Reasoning (input trace)

---

### II. Hospitals and Medical Facilities Expert System

#### What it is

A triage-oriented medical support expert system that ranks likely conditions and proposes first-response routing.

#### Why it is used

- Helps structure early triage decisions
- Improves consistency in symptom-based initial assessment
- Highlights urgency and emergency pathways quickly

#### Inputs

- Symptoms (multi-select)
- Age
- Pain scale (0-10)
- Symptom duration

#### How it works

- Uses predefined condition rules with symptom weights for:
  - Acute Viral Fever
  - Asthma Exacerbation
  - Possible Cardiac Event
  - Migraine Episode
  - Gastroenteritis / Food Infection
- Calculates probability per condition
- Boosts risk scoring for age, severe pain, and longer duration
- Applies emergency flags (for example chest pain, shortness of breath, fainting)
- Produces top 3 probable conditions with department mapping

#### Output

- Triage Level (Critical, High, or Moderate pathway)
- Most Probable Conditions (Top 3 ranked)
- Recommended First Response
- Suggested Care Path
- Inference Reasoning with matched symptoms

#### Important note

Educational decision support only, not a replacement for medical diagnosis.

---

### III. Help Desks Management Expert System

#### What it is

A rule-based IT ticket classifier that prioritizes incidents, maps ownership team, and applies SLA guidance.

#### Why it is used

- Standardizes incident prioritization
- Speeds up correct team routing
- Improves response-time compliance

#### Inputs

- Issue Type: Software, Hardware, Network, Security, Access
- Business Impact: Low, Medium, High
- Urgency: Low, Medium, High
- VIP User: Yes/No
- Service Downtime: Yes/No

#### How it works

- Aggregates a priority score from impact, urgency, VIP status, downtime, and issue category
- Converts score to priority bands:
  - P1 Critical
  - P2 High
  - P3 Medium
  - P4 Low
- Routes ticket to the corresponding support team
- Adds escalation and containment tasks for critical and security scenarios

#### Output

- Priority
- Assigned Team
- SLA target
- Action Checklist
- Inference Reasoning

---

### IV. Employee Performance Evaluation Expert System

#### What it is

A weighted scoring expert system for employee performance assessment with action-oriented management guidance.

#### Why it is used

- Makes evaluation criteria transparent
- Produces consistent rating outcomes
- Generates personalized improvement actions

#### Inputs

- Productivity (1-10)
- Work Quality (1-10)
- Collaboration (1-10)
- Attendance (1-10)
- Learning Agility (1-10)

#### How it works

- Computes weighted score:
  - Productivity: 30%
  - Quality: 30%
  - Collaboration: 15%
  - Attendance: 15%
  - Learning: 10%
- Maps score to rating:
  - Outstanding
  - Exceeds Expectations
  - Meets Expectations
  - Needs Improvement
- Creates targeted recommendations for weak dimensions

#### Output

- Weighted Score
- Performance Rating
- Management Action
- Recommendations list
- Inference Reasoning

---

### V. Stock Market Trading Expert System

#### What it is

An educational market signal engine that combines trend, momentum, volume, sentiment, and risk preference.

#### Why it is used

- Demonstrates explainable trading logic
- Trains decision discipline around risk and confirmation
- Converts multi-indicator inputs into a structured action plan

#### Inputs

- Market Trend: Uptrend, Sideways, Downtrend
- RSI (1-100)
- Volume: Low, Normal, High
- News Sentiment: Positive, Neutral, Negative
- Risk Profile: Conservative, Balanced, Aggressive

#### How it works

- Builds bullish and bearish scores
- Chooses base signal (BUY, SELL, HOLD)
- Applies risk-profile adjustments (for example conservative profile softens aggressive signals)
- Computes confidence from score separation
- Adds practical risk management actions

#### Output

- Final Signal
- Confidence percentage
- Action Plan checklist
- Inference Reasoning
- Educational disclaimer

#### Important note

Educational output only, not financial advice.

---

### VI. Airline Scheduling and Cargo Schedules Expert System

#### What it is

An operations planning expert system for flight schedule decisions and cargo routing under disruption.

#### Why it is used

- Improves operational consistency during disruptions
- Balances schedule reliability and cargo criticality
- Supports proactive coordination with airport and handling teams

#### Inputs

- Weather: Clear, Moderate, Severe
- Aircraft Status: On Time, Minor Delay, Technical Issue
- Crew Availability: High, Medium, Low
- Cargo Priority: Standard, Priority, Critical
- Airport Congestion: Low, Medium, High

#### How it works

- Computes disruption score from all operational constraints
- Maps score to risk category (Low, Medium, High)
- Chooses schedule action:
  - Operate with monitoring
  - Delay with protected slots and partial reroute
  - Reschedule and immediate critical reroute
- Appends context-specific operational checklist items

#### Output

- Operational Risk level
- Schedule Decision
- Action Checklist
- Inference Reasoning

## How the Inference Works

Across all six systems, the core expert-system pattern is:

1. Capture user facts through form inputs.
2. Evaluate rules and weights in backend logic.
3. Compute score or match strength.
4. Select decision class or recommendation path.
5. Return both recommendation and reasoning.

This keeps outputs explainable and easy to audit.

## Expected Outputs and Interpretation

- Classification-oriented systems return category + policy/checklist.
- Triage-oriented systems return urgency + probable causes + immediate action.
- Evaluation systems return score + rating + improvement guidance.
- Planning systems return risk + operational decision + execution checklist.

Use the reasoning field in each module to verify why a recommendation was generated.

## Troubleshooting

- If `python` is not recognized, install Python and ensure it is in PATH.
- If dependencies fail to install, upgrade pip:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- If Gradio port is busy, stop prior app instances and rerun.
- If PowerShell blocks activation script, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Academic Context

This suite aligns with Assignment 6 objective: implementing expert systems for practical domains and understanding how knowledge rules can support decision-making in real workflows.