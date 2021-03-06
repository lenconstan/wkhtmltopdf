from app import app, render_template, url_for, request, os
# from app import os
import pdfkit
import io
import base64
import jinja2
import os, sys, subprocess, platform

os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable) 
WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')], 
stdout=subprocess.PIPE).communicate()[0].strip()
pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)




@app.route('/')
@app.route('/index')
def index():
    # print(os.environ.get('SECRET_KEY'))
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
    pdf = pdfkit.from_string(outputText, False, configuration=pdfkit_config, options=options)
    file = io.BytesIO(pdf)
    base64_pdf = base64.b64encode(file.getvalue())

    return base64_pdf
    

