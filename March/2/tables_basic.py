from docxtpl import DocxTemplate
import pandas as pd

# Load the template file
template = DocxTemplate("employee_report_template.docx")

# Read the Excel file using pandas
df = pd.read_excel("employees_data.xlsx")

# Convert the DataFrame to a list of dictionaries
employee_data = df.to_dict(orient="records")

# Create a context dictionary with data to be inserted into the template
context = {
    "employees": employee_data,
}

# Render the template with the context data
template.render(context)

# Save the generated document to a new file
template.save("Employee_Report.docx")