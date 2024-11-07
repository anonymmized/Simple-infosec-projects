#!/bin/sh

save_report_to_file() {
    local report_path="/path/to/your/report_directory/report_$(date +%Y-%m-%d_%H:%M:%S).txt"
    echo "$1" > "$report_path"
    echo "Saved to file: $report_path"
}

sudo apt update

updates=$(sudo apt list --upgradable)
if [ -z "$updates" ]; then
    send_notification "No available updates."
    exit 0
fi

sudo apt upgrade -y

installed_updates=$(grep "^ii" /var/log/dpkg.log | grep "$(date +%Y-%m-%d)" | awk '{print $4}')

notification_message="Next updates were installed:\n\n$(echo "$installed_updates")\n\nPlease check your system."