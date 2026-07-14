# Password Cracking & Credential Attack Suite

An Educational Cybersecurity Toolkit for Password Security Analysis, Dictionary Generation, Hash Detection, Password Strength Evaluation, and Safe Attack Simulations.

---

## Overview

The **Password Cracking & Credential Attack Suite** is an educational cybersecurity project developed to demonstrate how attackers attempt to compromise weak passwords and how defenders can evaluate password security.

The project simulates common password auditing techniques including:

- Dictionary Generation
- Password Mutation
- Password Strength Analysis
- Hash Type Detection
- Dictionary Attack Simulation
- Brute Force Simulation
- Password Audit Report Generation

This toolkit **does not perform real-world password attacks**. It is intended strictly for learning, demonstrations, and authorized security assessments.

---

## Objectives

- Learn password authentication concepts.
- Understand password hashing.
- Generate custom password dictionaries.
- Simulate dictionary attacks.
- Simulate brute-force attacks.
- Analyze password strength.
- Calculate password entropy.
- Generate password audit reports.

---

## Features

- ✅ User Input Module
- ✅ Dictionary Wordlist Generator
- ✅ Password Mutation Engine
- ✅ Hash Detection
- ✅ Sample Hash Parsing
- ✅ Dictionary Attack Simulation
- ✅ Brute Force Password Simulation
- ✅ Password Strength Analyzer
- ✅ Password Entropy Calculation
- ✅ Security Report Generator
- ✅ Command Line Interface

---

# Project Architecture

```
                    User Input
                         │
                         ▼
              Dictionary Generator
                         │
                         ▼
                 Password Mutation
                         │
                         ▼
                 Wordlist Generation
                         │
                         ▼
                 Hash Extraction
                         │
                         ▼
          Dictionary Attack Simulation
                         │
                         ▼
           Brute Force Simulation
                         │
                         ▼
           Password Strength Analysis
                         │
                         ▼
             Report Generation
```

---

# Project Structure

```
password-cracking-suite/
│
├── analyzer/
│   └── strength.py
│
├── bruteforce/
│   └── simulator.py
│
├── dictionary/
│   └── generator.py
│
├── hashes/
│   ├── extractor.py
│   └── sample_shadow.txt
│
├── reports/
│   └── report.txt
│
├── wordlists/
│   └── list.txt
│
├── screenshots/
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

---

# Technologies Used

| Technology | Purpose              |
| ---------- | -------------------- |
| Python 3   | Programming Language |
| VS Code    | IDE                  |
| Git        | Version Control      |
| Docker     | Testing Environment  |
| hashlib    | Hash Generation      |
| itertools  | Brute Force          |
| pandas     | Reports              |
| matplotlib | Charts               |
| pyfiglet   | Banner               |
| colorama   | Terminal Colors      |
| tqdm       | Progress Bar         |
| tabulate   | Tables               |

---

# Installation

## Install required 
'''
code —-version

python3 --version

pip3 --version

git —-version

brew —-version
'''
<img width="1674" height="516" alt="image" src="https://github.com/user-attachments/assets/0a5a63c1-6d07-4280-a802-248ef86afd9f" />

---

## Open project

```bash
cd password-cracking-suite
```
---

## Create Virtual Environment

Mac/Linux

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```
<img width="1678" height="504" alt="image" src="https://github.com/user-attachments/assets/92a6dd45-43f2-442f-a371-3f5a2f3cf979" />

---

## Install Dependencies

```bash
pip install -r requirements.txt
```
<img width="3024" height="1510" alt="image" src="https://github.com/user-attachments/assets/ffc94501-d55b-498e-9792-92dd98d8883a" />
<img width="841" height="244" alt="Screenshot 2026-06-28 at 1 34 42 PM" src="https://github.com/user-attachments/assets/61bd6fd8-e251-41f8-b814-0a0c49b3ce61" />

---

# Running the Project

Run the main menu

```bash
python main.py
```
<img width="840" height="228" alt="Screenshot 2026-06-26 at 7 08 16 PM" src="https://github.com/user-attachments/assets/4c6c68ba-c9a7-44f3-a7f5-78613f80fce3" />
<img width="839" height="213" alt="Screenshot 2026-06-26 at 7 08 56 PM" src="https://github.com/user-attachments/assets/55c1096d-dbad-44b8-80f4-0595c7b85e9e" />
<img width="840" height="186" alt="Screenshot 2026-06-26 at 7 15 55 PM" src="https://github.com/user-attachments/assets/8776a66c-8819-49c4-9b78-35540e219d07" />
<img width="2196" height="1516" alt="image" src="https://github.com/user-attachments/assets/68e929b6-9765-419d-a65e-0fbc16a22af7" />

Run dictionary generator

```bash
python dictionary/generator.py
```
<img width="840" height="131" alt="Screenshot 2026-06-26 at 7 08 35 PM" src="https://github.com/user-attachments/assets/489d563c-5bcf-4aa0-8c86-708c38ffeb75" />
<img width="838" height="198" alt="Screenshot 2026-06-26 at 7 09 48 PM" src="https://github.com/user-attachments/assets/ae38b9fe-203c-41b4-8992-dc3ce12a549d" />
<img width="2194" height="1560" alt="image" src="https://github.com/user-attachments/assets/52d3945f-17ae-4dd4-b746-53fd0244ca68" />

Run password analyzer

```bash
python analyzer/strength.py
```
<img width="840" height="327" alt="Screenshot 2026-06-26 at 7 14 46 PM" src="https://github.com/user-attachments/assets/241b8661-ff14-433a-8495-42c5d709dde6" />
<img width="2198" height="1086" alt="image" src="https://github.com/user-attachments/assets/56249c65-3e6f-4087-8832-cc195e5d5c7a" />

Run dictionary attack simulator

```bash
python bruteforce/simulator.py
```
<img width="841" height="242" alt="Screenshot 2026-06-26 at 7 12 53 PM" src="https://github.com/user-attachments/assets/8a9d8b51-7c59-402e-9445-018e00959e78" />
<img width="2196" height="870" alt="image" src="https://github.com/user-attachments/assets/fb9fdb13-e9c2-46a8-a083-aafe49946d3f" />

---

# Module Description

## Dictionary Generator

Generates password candidates using:

- Name
- Date of Birth
- Numbers
- Common patterns
- Password mutations

Example Output

```
rahul
rahul123
Rahul
rahul05041996
rahul@123
```
<img width="839" height="213" alt="Screenshot 2026-06-26 at 7 08 56 PM" src="https://github.com/user-attachments/assets/a7015a98-91e1-4ed6-b945-ad41f39e7262" />

---

## Password Mutation Engine

Creates variations of passwords.

Examples

```
rahul

↓

Rahul

↓

RAHUL

↓

rahul123

↓

r@hul

↓

rahul2026
```
<img width="838" height="198" alt="Screenshot 2026-06-26 at 7 09 48 PM" src="https://github.com/user-attachments/assets/9b167f61-cd71-42d2-b82a-a1743144b55e" />
<img width="2192" height="1024" alt="image" src="https://github.com/user-attachments/assets/f4bf04c4-0c39-4483-b60f-8a7804096acd" />

---

## Hash Module

Reads sample hash files.

Example

```
rahul:$6$abc123$hashvalue
```

Detects hash types

- MD5
- SHA1
- SHA256
- SHA512
<img width="837" height="241" alt="Screenshot 2026-06-26 at 7 10 47 PM" src="https://github.com/user-attachments/assets/83d3de94-b20b-40bb-8e1f-9d8cf3e28d9b" />
<img width="837" height="241" alt="Screenshot 2026-06-26 at 7 10 47 PM" src="https://github.com/user-attachments/assets/5c58ca2e-55ba-437c-aae3-f0ca0863b443" />
<img width="839" height="367" alt="Screenshot 2026-06-26 at 7 11 28 PM" src="https://github.com/user-attachments/assets/134ed5f2-d85c-4ea9-a717-f6383063f809" />
<img width="2196" height="1208" alt="image" src="https://github.com/user-attachments/assets/1b8be0d9-1df5-47e5-836f-3efcb1467458" />

---

## Dictionary Attack Simulation

Simulates how a password hash is compared against generated dictionary entries.

Workflow

```
Wordlist

↓

Hash each password

↓

Compare hashes

↓

Password Found
```

---

## Brute Force Simulation

Generates every possible password combination using selected characters.

Example

```
aaa

aab

aac

...

999
```

This module demonstrates the exponential increase in password search space.

<img width="838" height="409" alt="Screenshot 2026-06-26 at 7 13 21 PM" src="https://github.com/user-attachments/assets/746de858-f473-4af9-8fd0-d93ffa860bef" />
<img width="837" height="368" alt="Screenshot 2026-06-26 at 7 13 47 PM" src="https://github.com/user-attachments/assets/a94dced3-777c-4630-ae53-1e29ba4aad52" />
<img width="2204" height="902" alt="image" src="https://github.com/user-attachments/assets/76504f5c-fa68-45c1-87d4-7def96e157bd" />

---

## Password Strength Analyzer

Evaluates passwords based on:

- Length
- Uppercase letters
- Lowercase letters
- Numbers
- Special symbols

Example

```
Password

Rahul123@

Score

4

Strength

Strong
```
<img width="840" height="327" alt="Screenshot 2026-06-26 at 7 14 46 PM" src="https://github.com/user-attachments/assets/5ec06a88-a61e-4bd7-891b-58eada2d5247" />

---

## Password Entropy

Entropy estimates password complexity.

Formula

```
Entropy = log₂(character_set^length)
```

Higher entropy indicates stronger passwords.
<img width="1674" height="144" alt="image" src="https://github.com/user-attachments/assets/7540d644-f62a-4e8e-b454-e04952cc0c4d" />
<img width="2188" height="766" alt="image" src="https://github.com/user-attachments/assets/8094d4f3-e019-4f80-8786-ff98077efbe6" />

---

## Report Generator

Creates audit reports containing:

- Password strength
- Weak passwords
- Security recommendations
- Entropy score
- Dictionary attack results

Example

```
Password Audit Report

Password:
Rahul123@

Strength:
Strong

Entropy:
52 bits

Recommendation:
Increase password length to 12+ characters.
```
<img width="837" height="424" alt="Screenshot 2026-06-26 at 7 15 19 PM" src="https://github.com/user-attachments/assets/a01c82a5-2266-45fc-bd90-4dff45c994d5" />
<img width="839" height="131" alt="Screenshot 2026-06-26 at 7 15 41 PM" src="https://github.com/user-attachments/assets/2f41322f-5cca-45a2-8457-a9c08f7004dc" />
<img width="2194" height="1212" alt="image" src="https://github.com/user-attachments/assets/75f8eb3a-1d28-4e8c-ade4-6dd566a35b69" />

---

# Screenshots

<img width="840" height="160" alt="Screenshot 2026-06-26 at 7 04 08 PM" src="https://github.com/user-attachments/assets/0e992776-c976-422b-ab40-e12b8a785f07" />
<img width="2198" height="596" alt="image" src="https://github.com/user-attachments/assets/8b384957-7aa5-43b5-a955-87b4ab9be3f2" />
<img width="2198" height="854" alt="image" src="https://github.com/user-attachments/assets/c5046b74-1cc6-4675-a72e-00d04165e288" />
<img width="1098" height="604" alt="Screenshot 2026-07-14 at 5 00 41 PM" src="https://github.com/user-attachments/assets/4b6c3b2d-b8b8-4cd1-af5f-f57345748254" />
<img width="2194" height="774" alt="image" src="https://github.com/user-attachments/assets/4cfa03d5-2df2-4de1-b449-e1532f6c2b5a" />
<img width="2194" height="1492" alt="image" src="https://github.com/user-attachments/assets/0545b427-daea-4fee-81a7-2c6cfe4062ee" />
<img width="2200" height="1034" alt="image" src="https://github.com/user-attachments/assets/87ec90fa-6b46-4fca-86af-062a3559f81a" />
<img width="836" height="241" alt="Screenshot 2026-06-26 at 7 04 24 PM" src="https://github.com/user-attachments/assets/c43eff08-35ad-41b3-b44b-afe5807c98ba" />
<img width="839" height="296" alt="Screenshot 2026-06-26 at 7 03 40 PM" src="https://github.com/user-attachments/assets/ee06490e-16d6-4c04-b2e4-2615c1d58d5b" />
<img width="838" height="326" alt="Screenshot 2026-06-28 at 1 34 27 PM" src="https://github.com/user-attachments/assets/a4f864c6-bbb1-43d8-885c-cbadc6f445b5" />
<img width="837" height="672" alt="Screenshot 2026-06-26 at 7 36 50 PM" src="https://github.com/user-attachments/assets/21e02076-d5d6-4fbc-adb4-bd7cd94b1db7" />
<img width="838" height="437" alt="Screenshot 2026-06-26 at 7 34 49 PM" src="https://github.com/user-attachments/assets/ae7458b7-6338-4fac-be8c-a8af9cde0bf7" />
<img width="1094" height="819" alt="Screenshot 2026-06-26 at 7 34 27 PM" src="https://github.com/user-attachments/assets/7e0d7f91-0293-41d1-b793-ff6a5dae7c06" />
<img width="829" height="127" alt="Screenshot 2026-06-26 at 7 38 02 PM" src="https://github.com/user-attachments/assets/e545d36e-8283-4868-ae5a-ddb125bb31d9" />
<img width="1091" height="811" alt="Screenshot 2026-06-26 at 7 37 43 PM" src="https://github.com/user-attachments/assets/f39334ee-2d19-498f-9ba5-5823d2454e51" />
<img width="1095" height="774" alt="Screenshot 2026-06-28 at 1 49 04 PM" src="https://github.com/user-attachments/assets/97141641-f4ab-4504-9d32-8a8436e9d1dd" />
<img width="750" height="454" alt="Screenshot 2026-06-28 at 1 49 16 PM" src="https://github.com/user-attachments/assets/d443400c-a3fb-4166-b4dc-ef04eeb4fec9" />
<img width="830" height="197" alt="Screenshot 2026-06-26 at 7 02 56 PM" src="https://github.com/user-attachments/assets/4e7b620b-adc9-4040-b83b-c779c2e81330" />
<img width="838" height="146" alt="Screenshot 2026-06-26 at 7 05 20 PM" src="https://github.com/user-attachments/assets/1d867994-6b77-4d71-80e3-99aa0126e7e6" />

# Sample Output

Main Menu

```
Password Cracking Toolkit

1 Generate Dictionary

2 Analyze Password

3 Dictionary Attack

4 Brute Force Simulation

5 Generate Report
```

---

# Security Notice

This project is developed **only for educational purposes**.

It must be used only:

- Security awareness training
- Cybersecurity education
- Authorized penetration testing
- Password auditing
- Laboratory demonstrations

Unauthorized password attacks against systems you do not own or have permission to test may violate laws and organizational policies.

---

# Future Improvements

- GUI using Tkinter or Streamlit
- GPU Password Simulation
- Rainbow Table Demonstration
- ZIP Password Recovery Simulation
- PDF Report Generation
- Hashcat Integration (Educational)
- John the Ripper Integration (Educational)
- Password Policy Checker

---

# Challenges
Examples:

Creating a modular project structure
Understanding password hashing
Designing safe simulations
Managing dependencies
Writing reusable Python modules

---

# Learning Outcomes
Python Programming
Cybersecurity Fundamentals
Password Security
Hashing Algorithms
Dictionary Attacks
Brute Force Concepts
Secure Coding Practices
Git & GitHub Workflow

---

# Author

RahulKumar Prajapati

M.Sc. Information Technology

Cybersecurity & AI Enthusiast

GitHub:
https://github.com/PR-4157

---

# Acknowledgements

- Python Documentation
- Passlib
- OWASP Password Security Guidelines
- NIST Digital Identity Guidelines
- Cybersecurity Educational Resources
