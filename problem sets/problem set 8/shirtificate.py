from fpdf import FPDF

class Shirtificate(FPDF):
  def header(self):
    self.set_font("helvetica", "B", 50)
    self.cell(0, 50, "CS50 Shirtificate", align="C")
    self.ln(20)

  def add_shirt(self, name):
    self.image("shirtificate.png", x=10, y=70, w=190)

    self.set_font("helvetica", "B", 30)
    self.set_text_color(255, 255, 255)
    self.set_y(140)
    self.cell(0, 50, f"{name} took CS50", align="C")

name = input("Name: ")

pdf = Shirtificate(orientation="P", format="A4")
pdf.add_page()
pdf.add_shirt(name)
pdf.output("shirtificate.pdf")