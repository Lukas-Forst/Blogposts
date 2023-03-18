from docxtpl import DocxTemplate
from datetime import date, datetime

# Load the template file
template = DocxTemplate("Evaluation_template.docx")

# Create a context dictionary with data to be inserted into the template
context = {
    'employee_name': 'John Doe',
    'start_date': date(2023, 1, 1).strftime("%d.%m.%Y"),
    'end_date': date(2023, 3, 31).strftime("%d.%m.%Y"),
    'tedate': datetime.now().strftime("%d.%m.%Y"),
    'score': 85,
    'manager_name': 'Jane Smith'
}

# Render the template with the context data
template.render(context)

# Save the generated document to a new file
template.save(f"Evaluation_{context['employee_name']}.docx")