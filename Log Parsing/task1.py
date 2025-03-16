
def check_logs(log_file):
    suspicious_patterns = ["failed login", "unauthorized access", "suspicious activity detected"]
    
    with open(log_file, "r") as file:
        for line in file:
            if any(pattern.lower() in line.lower() for pattern in suspicious_patterns):
                print(f"ALERT: Suspicious activity detected - {line.strip()}")

if __name__ == "__main__":
    log_file = "log.txt"  
    check_logs(log_file)
