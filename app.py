from flask import Flask, request, render_template, jsonify
import pandas as pd
from cachetools import TTLCache
import matplotlib.pyplot as plt


app = Flask(__name__)
cache = TTLCache(maxsize=100, ttl=300)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files')
    for file in files:
        cache[file.filename] = file.read().decode('utf-8')
    return jsonify({'success': True})

@app.route('/aggregate', methods=['GET', 'POST'])
def aggregate():
    # if request.method == 'POST':
        df = pd.read_csv('./csv-data/Original-Data.csv')

        plt.bar(df['service_filter'], df['city_name'])
        # Add labels and title
        plt.xlabel('service_filter')
        plt.ylabel('city_name')
        plt.title('Aggregated Data by service_filter')

        # Show the plot
        plt.show()

        # aggregated_data = ''
        # for filename, data in cache.items():
        #     aggregated_data += f'Filename: {filename}\nData: {data}\n\n'
        # return aggregated_data
    # else:
    #     return render_template('aggregate.html')

if __name__ == '__main__':
    app.run(debug=True)
