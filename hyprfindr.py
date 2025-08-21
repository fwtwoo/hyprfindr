#!/usr/bin/env python3
import subprocess
import argparse
from pathlib import Path
from enum import Enum

# Shows an info dialog
def show_notification(message):
    subprocess.run(['zenity', '--notification', '--text', message])

# Function for argument parsing
def parse_args():
    # ArgumentParser checks for CLI argument
    parser = argparse.ArgumentParser(
        prog="hyprfindr",
        description="Search and display Hyprland keybinds via CLI and your notification daemon.",
    )

    # Adds the --version flag
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1"
    )

    # Adds the actual app/command name flag
    parser.add_argument(
        "query",
        metavar="NAME",
        help="Search keybinds by application/command name, or by a key within a key combination."
    )

    # Reutrns argument
    args = parser.parse_args()
    return args.query

# Function for getting variables
def split_variables():
    # Config path
    path = Path("~/.config/hypr/hyprland.conf").expanduser()

    # Open file and read
    with open(path, "r") as file:
        # Create dictionary
        variable_dict = {}
        for line in file:
            # Split to remove comments
            line = line.split("#")[0]
            # Split into two parts
            if line.startswith("$"):
                lhs, rhs = line.split("=", 1)

                # Strip line of whitespaces
                var_name = lhs.strip()
                var_value = rhs.strip()

                variable_dict[var_name] = var_value
            else:
                continue

        return variable_dict

# Function for gettings binds
def split_binds():
    # Config path
    path = Path("~/.config/hypr/hyprland.conf").expanduser()
    # Variables to use later
    variables = split_variables()

    # Create empty list
    binds = []
    # Open file and read
    with open(path, "r") as file:
        for line in file:
            # Split to remove comments
            line = line.split("#")[0]
            # Split into two parts
            if '=' in line:
                lhs, rhs = line.split("=", 1)
            else:
                continue

            # Strip line of whitespaces
            stripped = rhs.strip()

            # Filter with "bind"
            if lhs.split()[0] == "bind":
                # Create list
                elements = []
                # Split at ","
                for p in stripped.split(","):
                    parts = p.strip() # Strip whitespaces
                    if parts != "":
                        # Add to list
                        elements.append(parts)

                # Create new list
                translated_elements = []
                # Loop through
                for element in elements:
                    for name, value in variables.items():
                        # Replace with real variable value
                        element = element.replace(name, value)
                    translated_elements.append(element) # Append translated
                 
                # Append to list
                binds.append(translated_elements)
    return binds

# Main function
def main():
    # Init variables
    binds = split_binds()
    variables = split_variables()

    # parse_args's return value
    user_input = parse_args()

    found = False

    # Loop through binds
    for bind in binds:
        has_exec = "exec" in bind
        # If users input matches bind
        if user_input in bind:
            # Check exec and splice
            if has_exec:
                keybind = bind[:2] # Get first 2 items
                command = bind[-1] # Get last item
            else:
                keybind = bind[:2] # Get first 2 items
                command = bind[2] # Get 3rd item

            # Join to format nicely
            keybind_str = " + ".join(keybind)
            
            # Show notification and print output
            msg = f"{keybind_str} → {command}"
            show_notification(msg)
            print(msg) # For piping or logging

            found = True

    # If user input doesn't exist in bind
    if not found:
        print("No match found.")

# Run the program
if __name__ == "__main__":
    main()
