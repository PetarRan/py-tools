from flask import Flask, render_template, make_response, request
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/pdfmerge.html/upload', methods=['POST'])
def upload():
    pdf_files = request.files.getlist('pdf_file')

    writer = PdfWriter()

    for pdf_file in pdf_files:
        reader = PdfReader(pdf_file)
        # Loop through each page in the PDF file and add it to the writer object
        for i in range(len(reader.pages)):
            writer.add_page(reader.pages[i])

        # Save the merged PDF file to a byte stream
    output_stream = BytesIO()
    writer.write(output_stream)

    # Return the merged PDF file as a downloadable attachment
    response = make_response(output_stream.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=merged.pdf'
    response.headers['Content-Type'] = 'application/pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)