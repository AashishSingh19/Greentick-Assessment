This project contains the technical asssessments for Green Tick.

1. Log Parsing and Basic Alert System
   
This is a basic program created using Python as the programming language. This system scans the log file for any suspicious activities or patterns such as 'unauthorized access', 'failed login attempts' and
'suspicious activities'. If such patterns are found then the system generates an alert by printing a message to the console.

# STEPS TO RUN THE CODE:

1. Ensure that Python is installed on your device.
2. Clone or download the project to your local machine.
3. Unzip the project and run it using an IDE(Visual Studio Code or Pycharm)
4. Run the program.

# Assumptions and limitations

1. Basic log file scanning
   It is a simple system that only reads the text based log file where each entry is on a new line.
   
2. Static log file scanning
   It does not take real time logins into accounts and only analyzes static logs.

2. Webscan crawler

A simple web crawler that can visit a website and scan for basic vulnerabilities like:-
-Presence of HTTP security headers (e.g., X-Content-Type-Options, Strict-TransportSecurity)
-Presence of outdated software versions (if visible on the webpage or headers).
-Presence of forms without security attributes (e.g., action attribute missing or method="GET" instead of POST).

# STEPS TO RUN THE CODE:

1. Ensure that Python is installed on your device.
2. Clone or download the project to your local machine.
3. Install dependencies (if not already installed) :-
   pip install requests beautifulsoup4
4. Run the code using an IDE(Visual Studio Code or Pycharm).
5. Enter the url of the website; https://example.com.
6. The results will be displayed as a message in the console.

# Assumptions and limitations

1. Basic Security functions
   Simple and basic web crawler that only checks for missing action attributes and insecure GET methods.
   
2. Scope of software version detection
   The system only checks Apache version from the server header that if hidden may not detect them.
   
3. Limited Javascript Execution
   The scanner does not execute JavaScript, so vulnerabilities in dynamically loaded content may be missed.
