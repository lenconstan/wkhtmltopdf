from app import app, render_template, url_for, request
import pdfkit
import pydf
import io
import base64
import jinja2



@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/pdf')
def pdf():
    # Render template with jinja2
    f = open("app/templates/test.html", "r")
    templateLoader = jinja2.FileSystemLoader(searchpath="app/templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "testlabel.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(val='Stan')

    # Convert HTML to PDF
    options = {
        'page-size': 'A6',
        'orientation': 'Portrait'
    }
    pdf = pdfkit.from_string(outputText, False, options=options)
    file = io.BytesIO(pdf)
    base64_pdf = base64.b64encode(file.getvalue())

    return base64_pdf
    

