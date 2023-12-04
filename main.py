from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a cell
pdf.cell(200, 10, txt="Ernest Hemingway", ln=True, align='C')


# All you have to do is write one true sentence. Write the truest sentence that you know.
pdf.multi_cell(0, 10, txt='"All you have to do is write one true sentence. Write the truest sentence that you know."')

# Save the pdf with name .pdf
pdf.output("ErnestHemingway.pdf")

