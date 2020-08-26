from fpdf import FPDF, HTMLMixin
from datetime import date
import random
import string


class HTML2PDF(FPDF, HTMLMixin):
    pass

def html2pdf(sender_acc,receiver,amount,invoice):
    transaction_id = ''.join(random.choice(string.hexdigits) for i in range(20))
    html = f'''
    <div style="width: 50%; margin: auto;">
        <h1 style="font-size: 30px; font-family: Nunito;text-align: center;">Bank Transaction</h1>
        <div style="padding: 50px 0 0 0;display: flex;width: 100%;justify-content: space-around;">
            <p style="font-family: Nunito; font-weight: 600;">Transaction Id: {transaction_id}</p>
            <p style="font-family: Nunito; font-weight: 600;">Date: {str(date.today())}</p>
        </div>
        <div style="display: flex;justify-content: space-around;flex-wrap: wrap;">
            <p style="font-family: Nunito; font-weight: 600;">Account Id: {sender_acc}</p>
            <p style="font-family: Nunito; font-weight: 600;">Amount Sent: {amount}</p>
            <p style="font-family: Nunito; font-weight: 400;">Invoice: {invoice}</p>
        </div>
        <div style="display: flex;justify-content: space-around;flex-wrap: wrap;">
            <p style="font-family: Nunito; font-weight: 600;">Receiver Account Id: {receiver}</p>
        </div>
        <div style="display: flex;justify-content: flex-end;flex-wrap: wrap;">
            <p style="font-family: Nunito; font-weight: 600;">Checked By: Online Transaction</p>
        </div>
    </div>
    '''
    
    pdf = HTML2PDF()
    pdf.add_page()
    pdf.write_html(html)
    pdf.output(f'/home/pyderator/Documents/tkinterproject/myself/Collage-Tkinter-Project/ProgramFiles/invoice/{str(sender_acc)+str(transaction_id)}.pdf')
