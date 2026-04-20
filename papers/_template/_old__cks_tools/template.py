"""
Make Readme lib for Control System
"""

from jinja2 import Template
import os

def render_template(output_path, template_content, data_dict):
    """
    Loads a text file as a Jinja2 template, renders it with 
    data_dict, and saves it to output_path.
    """
    try:
        # 2. Create a Jinja2 Template object
        template = Template(template_content)

        # 3. Render the template with the dictionary data
        rendered_text = template.render(data_dict)

        # 4. Save the result to the output file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(rendered_text)
        
        print(f"Successfully rendered to '{output_path}'")
        return True

    except Exception as e:
        print(f"An error occurred during template rendering: {e}")
        return False

def test():
    # Example dictionary (often loaded from JSON)
    my_data = {
        "project_name": "T3-Automation",
        "version": "1.0.4",
        "items": ["Auth", "Database", "Logging"],
        "is_active": True
    }

    render_template("template.txt", "output.txt", my_data)

