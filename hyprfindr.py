#!/usr/bin/env python3
import subprocess
import argparse
from pathlib import Path

# Shows an info dialog
def show_info(message):
    subprocess.run(['zenity', '--info', '--text', message])

# Shows a prompt dialog
def show_entry(message):
    # Writes input to stdout
    result = subprocess.run(['zenity', '--entry', '--text', message], capture_output=True, text=True)
    return result.stdout.strip()

# Function for argument parsing
def parse_args():
    # ArgumentParser checks for CLI argument
    parser = argparse.ArgumentParser(
        prog="hyprfindr",
        description="Search and display Hyprland keybinds via Zenity dialogs.",
        epilog="If no argument is given, you’ll be prompted with a Zenity entry dialog."
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
        nargs="?", # "nargs" makes argument optional 
        metavar="NAME",
        help="Application/command name to search for in keybinds"
    )

    args = parser.parse_args()

    # Checking if user passed arguments or not
    if args.query is None:
        # Function for no argument (zenity prompt)
        user_input = show_entry("Enter app/command name")
        show_info(f"You passed '{user_input}'!")
    else:
        # Function for an argument (zenity info)
        show_info(f"You passed '{args.query}'!")

def split_binds(path):
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

                # Append to list
                binds.append(elements)
    return binds

def split_variables(path):
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

# Main function
def main():
    # Hyprland config path
    path = Path("~/.config/hypr/hyprland.conf").expanduser()

    binds = split_binds(path)
    variables = split_variables(path)

    print("Collected binds:")
    for b in binds:
        print(b)

    print("Collected variables:")
    for name, value in variables.items():
        print(f"{name} = {value}")

# Run the program
if __name__ == "__main__":
    main()
