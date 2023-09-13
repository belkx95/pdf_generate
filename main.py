import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")
    pdf.line(10, 20, 200, 20)

    # add footer
    pdf.ln(267)
    pdf.set_font(family="Times", size=8, style="I")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=8, txt=row["Topic"], ln=1, align="R")

    # add lines
    for i in range(20, 300, 10):
        pdf.line(10, i, 200, i)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # add footer
        pdf.ln(279)
        pdf.set_font(family="Times", size=8, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=8, txt=row["Topic"], ln=1, align="R")

        # add lines
        for i in range(10, 300, 10):
            pdf.line(10, i, 200, i)

pdf.output("output.pdf")