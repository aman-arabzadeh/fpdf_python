from fpdf import FPDF


pdf = FPDF()

pdf.add_page()


pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Ernest Hemingway", ln=True, align='C')


pdf.multi_cell(0, 10, txt='"All you have to do is write one true sentence. Write the truest sentence that you know."')

pdf.output("ErnestHemingway.pdf")

