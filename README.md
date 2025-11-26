# 💉 SQLi Hunter: Injection Playground & Detection Engine

---

## 🌟 Project Overview
SQLi Hunter is a dual-component cybersecurity education platform designed to demonstrate the mechanics of SQL Injection (SQLi) attacks and the effectiveness of modern remediation techniques. It combines a visually immersive Vulnerable Web Application with an automated Detection Engine.The goal is to provide a safe, isolated environment where developers and security enthusiasts can visualize how injection attacks work in real-time and verify how Parameterized Queries neutralize them.

---

## ✨ Features and Technology Stack
| Component | Technology | Description | 
| --- | --- | --- |
| Core Logic | Python 3.x | The primary language for both the backend and the attack script. | 
| Web Framework | Flask | Lightweight server handling both vulnerable and secure API endpoints. | 
| Database | SQLite | A lightweight SQL engine used to demonstrate authentication bypass. | 
| User Interface | HTML5 / CSS3 | A dynamic "Cyberpunk/Glassmorphism" UI with real-time log visualization. | 
| Attack Engine | Requests / JSON | Custom Python script for fuzzing and response analysis. | 

---

## 🛡️ The Attack & Defense Architecture
The system operates on a unique interaction between a Target and a Hunter:

**Component 1: The Playground (Target)**
A Flask-based web application with a "Cyberpunk Terminal" interface that exposes two distinct authentication routes:

* 🔴 The Vulnerable Route (/vulnerable): Deliberately uses String Concatenation to build SQL queries.
  * Flaw: Inputs are treated as executable code.
  * Result: Allows authentication bypass via standard payloads (e.g., ' OR '1'='1).
* 🟢 The Secure Route (/secure): Implements Parameterized Queries (Prepared Statements).
  * Defense: Inputs are strictly treated as data.
  * Result: Injection attempts are neutralized, rendering payloads harmless.

**Component 2: The Hunter (Scanner)**
An external Python automation engine that acts as the "Red Team."

1. Payload Injection: Iterates through a dictionary of common SQL injection vectors (payloads.txt).
2. Response Analysis: Parses the JSON response from the web app to detect:
   * Successful Bypasses: Identifying when a login succeeds without valid credentials.
   * Syntax Errors: Detecting database crashes (indicative of potential Blind SQLi).

---

## 📁 Project Structure
```
SQLi-Hunter/
├── app/
│   ├── static/
│   │   ├── style.css       # Cyberpunk UI styling and animations.
│   │   └── script.js       # AJAX logic for non-blocking UI updates.
│   ├── templates/
│   │   └── index.html      # Main Dashboard with Live Terminal Log.
│   ├── app.py              # Flask Backend (Vulnerable & Secure logic).
│   └── database.db         # SQLite DB (Auto-generated on launch).
├── detector/
│   ├── engine.py           # The Python Attack Script (The Hunter).
│   └── payloads.txt        # List of attack vectors/fuzzing list.
├── requirements.txt        # List of necessary Python dependencies.
├── README.md               # Project documentation.
└── LICENSE                 # MIT License.
```

---

## 🚀 Getting Started
These instructions will get a copy of the project up and running on your local machine for testing and educational purposes.

### Prerequisites
* Python 3.8+
* pip (Python package installer)

### Installation

1. Clone the repository:
```Bash

git clone https://github.com/your-username/SQLi-Hunter.git
cd SQLi-Hunter
```

2. Install dependencies:
```Bash

pip install -r requirements.txt
```

### Running the Application
1. Start the Web Application (The Target): Navigate to the app directory and run the server.
```Bash
cd app
python app.py
```
Access the interface at: `http://127.0.0.1:5000`

2. Start the Detection Engine (The Hunter): Open a new terminal window, navigate to the detector directory, and run the script.

```Bash
cd detector
python engine.py
```

_Watch the terminal as the script attempts to breach the web application automatically._

---

## 🤝 Contributing
We highly value contributions! By tackling one of the points below, you can help make this tool more robust. Please fork the repository and submit a Pull Request.

Contribution Points
1. Blind SQLi Support: Enhance detector/engine.py to measure response times. If the server takes >5 seconds to respond to a SLEEP() payload, flag it as vulnerable.
2. WAF Evasion: Add a feature to the detector that attempts to bypass basic filters using encoding (e.g., URL Encoding, Hex Encoding).
3. Reporting: Update the engine to generate a PDF or HTML report of all found vulnerabilities after the scan completes.
4. UI Customization: Add a "Matrix Mode" theme to app/static/style.css.

---

## ⚠️ Legal Disclaimer
This project is for _**EDUCATIONAL PURPOSES ONLY**_._** Do not use**_ the _**detection engine**_ against targets you _**don't have explicit permission to test**_. The _**author**_ is _**not responsible**_ for any _**misuse of this tool.**_

---

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
