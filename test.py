# from reportlab.lib.colors import blue
# from reportlab.lib.pagesizes import LETTER
# from reportlab.lib.units import inch
# from reportlab.pdfgen.canvas import Canvas
#
# canvas = Canvas("font-colors.pdf", pagesize=LETTER)
#
# # Set font to Times New Roman with 12-point size
# canvas.setFont("Nunito", 12)
#
# # Draw blue text one inch from the left and ten
# # inches from the bottom
# canvas.setFillColor(blue)
# canvas.drawString(1 * inch, 10 * inch, "Blue text Done")
# canvas.drawString(1 * inch, 20 * inch, "red text Done")
# canvas.drawString(1 * inch, 30 * inch, "black text Done")
#
#
# # Save the PDF file
# canvas.save()
from fpdf import FPDF, HTMLMixin
class HTML2PDF(FPDF, HTMLMixin):
    pass

def html2pdf():
    html = f'''
    <div style="width: 50%; margin: auto;">
        <h1 style="font-size: 30px; font-family: Nunito;text-align: center;">Bank Transaction</h1>
        <div style="padding: 50px 0 0 0;display: flex;width: 100%;justify-content: space-around;">
            <p style="font-family: Nunito; font-weight: 600;">Transaction Id: 1875675765</p>
            <p style="font-family: Nunito; font-weight: 600;">Date: 1875675765</p>
        </div>
        <div style="display: flex;justify-content: space-around;flex-wrap: wrap;">
            <p style="font-family: Nunito; font-weight: 600;">Sender Name: Gaurav Jha</p>
            <p style="font-family: Nunito; font-weight: 600;">Account Id: 8787868767</p>
            <p style="font-family: Nunito; font-weight: 600;">Amount Sent: 5000</p>
        </div>
        <div style="display: flex;justify-content: space-around;flex-wrap: wrap;">
            <p style="font-family: Nunito; font-weight: 600;">Receiver Name: Gaurav Jha</p>
            <p style="font-family: Nunito; font-weight: 600;">Account Id: 8787868767</p>
        </div>
        <div style="display: flex;justify-content: flex-end;flex-wrap: wrap;">
            <p style="font-family: Nunito; font-weight: 600;">Checked By: Admin</p>
        </div>
    </div>
    '''


    pdf = HTML2PDF()
    pdf.add_page()
    pdf.write_html(html)
    a = pdf.output('/home/pyderator/Documents/tkinterproject/myself/Collage-Tkinter-Project/ProgramFiles/testing/html2pdf.pdf')


html2pdf()
