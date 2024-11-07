#!/bin/sh

# func for saving output to file
save_report_to_file() {
    local report_path="/path/to/your/report_directory/report_$(date +%Y-%m-%d_%H:%M:%S).txt"
    echo "$1" > "$report_path"
    echo "Saved to file: $report_path"
}

brew update

brew upgrade

installed_updates=$(brew list --versions)

echo "Installed updates:"
echo "$installed_updates"

report_message="Next updates were installed:\n\n$(echo "$installed_updates")\n\nPlease, check your system."

save_report_to_file "$report_message"