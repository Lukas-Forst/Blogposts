from docxtpl import DocxTemplate
from datetime import  datetime
template = DocxTemplate("dynamic_table.docx")


context = {
    'Company':'Tonys Logistics',
    'date' : datetime.now().strftime("%d.%m.%Y"),
    'col_labels': ['Product', 'Category', 'Price', 'Stock'],
'tbl_contents': [
    {'label': 'Item 1', 'cols': ['Laptop', 'Electronics', '$900', '50'], 'bg': 'cccccc'},
    {'label': 'Item 2', 'cols': ['T-shirt', 'Apparel', '$15', '200'], 'bg': 'bababa'},
    {'label': 'Item 3', 'cols': ['Coffee Mug', 'Kitchenware', '$8', '150'], 'bg': 'cccccc'},
    {'label': 'Item 4', 'cols': ['Smartphone', 'Electronics', '$700', '100'], 'bg': 'bababa'},
],
}

template.render(context)

template.save("dynamic_table_out.docx")
