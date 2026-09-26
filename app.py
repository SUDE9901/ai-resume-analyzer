from flask import Flask, render_template, request
from analyzer import analyze_resume
import pdfplumber

app = Flask(__name__)

# PDF text extract function
def extract_text(file):
    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    return text


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":

        file = request.files["resume_pdf"]

        if file:
            text = extract_text(file)   # ✅ FIXED HERE
            result = analyze_resume(text)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)