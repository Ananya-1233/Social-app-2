import streamlit as st
import random
import pandas as pd
from datetime import datetime
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors
import io

# ---- Setup Names ----
adults = ["Vikas Basava", "Chanbasu Goudru", "Manjunath Sanganal", "Mahabaleshwar Haligeri", "Deepak Kosandar"]
kids = ["Ananya Yakkundi", "Gangadhar Yadavannavar", "Vinayak Agali"]
gardens = ['Narendra Tarun Udyogi', 'Chanakya Tarun Udyogi','Azad Tarun Udyogi', 'Abhimanyu Tarun Udyogi']
parks = ['Vitthal Samanya Vidyarthi', 'Madhav Samanya Vidyarthi','Azad Samanya Vidyarthi','Abhimanyu Samanya Vidyarthi',
         'Narendra Samanya Vidyarthi','Mayur Verma Samanya Vidyarthi', 'Krishna Colony Samanya Vidyarthi',
         'Khudiram Bose Samanya Vidyarthi', 'Ramajaneya Samanya Vidyarthi']

st.title("ಪ್ರವಾಸಿ ಕಾರ್ಯಕರ್ತ ")

# ---- Date Selection ----
selected_date = st.date_input("Select a date for assignment", datetime.today())
seed_value = int(selected_date.strftime("%Y%m%d"))  # convert date to YYYYMMDD integer
random.seed(seed_value)

# ---- Random Assignment ----
assignments = []

# Adults can go to both gardens and parks
for adult in adults:
    place = random.choice(gardens + parks)
    assignments.append({"Name": adult, "Assigned Place": place})

# Kids can only go to gardens
for kid in kids:
    place = random.choice(parks)
    assignments.append({"Name": kid, "Assigned Place": place})

# Convert to DataFrame
df = pd.DataFrame(assignments)

# Show in Streamlit
st.subheader("Assignment Table")
st.dataframe(df)

# ---- PDF Generation Function ----
# def generate_pdf(dataframe, date_str):
#     buffer = io.BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=A4)
#     styles = getSampleStyleSheet()
#     story = []

#     # Title
#     story.append(Paragraph("Assignment Report", styles['Title']))
#     story.append(Spacer(1, 12))

#     # Description
#     description = f"""
#     ಪ್ರವಾಸಿ ಕಾರ್ಯಕರ್ತ  {date_str}.
#     """
#     story.append(Paragraph(description, styles['Normal']))
#     story.append(Spacer(1, 12))

#     # Table Data
#     table_data = [list(dataframe.columns)] + dataframe.values.tolist()
#     table = Table(table_data, hAlign="LEFT")
#     table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black)
#     ]))
#     story.append(table)

#     # Build PDF
#     doc.build(story)
#     buffer.seek(0)
#     return buffer

# # ---- Download Button ----
# pdf_buffer = generate_pdf(df, selected_date.strftime("%d-%m-%Y"))
# st.download_button(
#     label="Download Assignment Report as PDF",
#     data=pdf_buffer,
#     file_name=f"assignment_report_{selected_date.strftime('%Y%m%d')}.pdf",
#     mime="application/pdf"
# )
