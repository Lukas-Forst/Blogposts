import random
import plotly.graph_objects as go
from docxtpl import DocxTemplate

# Generate fictional survey data
categories = ['Price', 'Quality', 'Customer Service', 'Delivery', 'Overall Experience']
satisfaction_levels = [random.randint(1, 10) for _ in range(len(categories))]

# Create a radar chart using plotly
fig = go.Figure(data=go.Scatterpolar(
    r=satisfaction_levels,
    theta=categories,
    fill='toself'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[1, 10]
        )
    ),
    showlegend=False
)

# Save the chart as an image
chart_filename = "radar_chart.png"
fig.write_image(chart_filename)

# Load the Word document template
doc = DocxTemplate("survey_template.docx")
context = {
    'Client': "Sarah Davis",
    "Name": "Robert Wilson",
"Position":"IT Director", 
"Company": "Acme Industries"
}

doc.render(context)

# Replace the picture placeholder in the template with the chart image
doc.replace_media("temp-plot.png", chart_filename)

# Save the updated document
doc.save("Survey_Report.docx")
