from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file from the request
    file = request.files['file']
    
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file)
    
    # Perform data aggregation operations using Pandas
    # ... (your data aggregation code here) ...
    
    # Return the aggregated data as a response
    return df.to_html()
