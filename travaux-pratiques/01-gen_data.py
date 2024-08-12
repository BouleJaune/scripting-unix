# Script utiliser pour générer des données factices

import pandas as pd
import random
from datetime import datetime, timedelta

# Définition des paramètres de génération
servers = ["Server1", "Server2", "Server3", "Server4", "Server5"]
severities = ["INFO", "WARNING", "ERROR", "CRITICAL"]
messages = {
    "INFO": ["System running smoothly.", "Routine check completed.", "Backup successful.", "Restart performed successfully", "Update was successful"],
    "WARNING": ["Disk space running low.", "High memory usage detected.", "Unusual login activity detected.", "Load average running high", "MySQL response time slow"],
    "ERROR": ["Application crashed.", "Service unavailable.", "Database connection lost.", "FileSystem saturated", "Server unresponsive"],
    "CRITICAL": ["System overload imminent.", "Critical security vulnerability detected.", "Data corruption detected.", "System bricked", "Server is on fire"]
}
infogerants = ["InfogérantA", "InfogérantB", "InfogérantC"]
applications = ["App1", "App2", "App3", "App4"]
environments = ["Production", "Staging", "Development"]
n = 10000


data = []
start_time = datetime.now()


def gen_line():

    timestamp = start_time - timedelta(minutes=random.randint(0, 10000))
    server = random.choice(servers)
    severity = random.choice(severities)
    message = random.choice(messages[severity])
    infogerant = random.choice(infogerants)
    application = random.choice(applications)
    environment = random.choice(environments)
    return [timestamp, server, severity, message, infogerant, application, environment]


data = []
for _ in range(n):
    data.append(gen_line())

df_large = pd.DataFrame(data, columns=["Timestamp", "Server", "Severity", "Message", "Infogérant", "Application", "Environment"])
csv_path = "./server_monitoring_logs.csv"
df_large.to_csv(csv_path, index=False)
