import pandas as pd
import os
import json

def parse_excel_to_dict(file_path):
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

    tree = {}
    for _, row in df.iterrows():
        current_level = tree
        for col in df.columns[:-2]:  # Exclude 'Key' and 'Value'
            level = row[col]
            if pd.notna(level):  # Ensure level is not NaN
                if level not in current_level:
                    current_level[level] = {}
                current_level = current_level[level]

        key = row.get('Key')
        value = row.get('Value')

        if pd.notna(key) and pd.notna(value):  # Ensure key and value are not NaN
            current_level[key] = value
        else:
            print(f"Skipping row with NaN Key or Value: {row}")

    return tree

def format_dict_as_code(data, indent=4):
    """
    Format the dictionary as a properly indented Python code-like string.
    """
    def recursive_format(d, level=0):
        spaces = ' ' * (indent * level)
        if isinstance(d, dict):
            formatted = "{\n"
            for key, value in d.items():
                formatted += f"{spaces}{indent * ' '}{repr(key)}: {recursive_format(value, level + 1)},\n"
            formatted += f"{spaces}}}"
            return formatted
        else:
            return repr(d)

    return f"data = {recursive_format(data)}"


def sanitize_text(text):
    if not isinstance(text, str):
        return ""  # Return empty string if text is not valid
    return text.replace("\n", " ").replace("\\", " ").replace("𝑆", "S").replace("𝐻", "H")



if __name__ == "__main__":
    # Define the path to your Excel file
    file_path = r"D:\my code\autocad\new mind map\project3\data\prepare_tree.xlsx"
    output_file = r"D:\my code\autocad\new mind map\project3\data\output.py"

    # Parse the Excel file into a dictionary
    output = parse_excel_to_dict(file_path)
    if output:
        # Format the dictionary as Python code
        formatted_output = format_dict_as_code(output)

        # Print the output
        print(formatted_output)

        # Save the formatted output to a .py file using UTF-8 encoding
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(formatted_output)
        print(f"Formatted dictionary saved to {output_file}")
