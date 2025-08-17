#!/usr/bin/env python3
import subprocess
import argparse

# Shows the dialog info
def show_info(message):
    subprocess.run(['zenity', '--info', '--text', message])

# Shows the dialog prompt
def show_entry(message):
    # Writes input to stdout
    result = subprocess.run(['zenity', '--entry', '--text', message], capture_output=True, text=True)
    return result.stdout.strip()

# Main function
def main():
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

    # Adds the actual command name flag
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
 
# Run the program
if __name__ == "__main__":
    main()