import matplotlib
matplotlib.use('Agg') 

import matplotlib.pyplot as plt
from matplotlib import rc
from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)


plt.rcParams['font.family'] = 'Apple SD Gothic Neo'


DATA_PATH = 'data/traffic_accidents.csv'
GRAPH_PATH = 'static/graph.png'


data = pd.read_csv(DATA_PATH)


def create_graph():
    plt.figure(figsize=(10, 6))
    plt.bar(data['지역'], data['교통사고수'], color='skyblue') 
    plt.title('지역별 교통사고 통계', fontsize=16)
    plt.xlabel('지역', fontsize=12)
    plt.ylabel('교통사고 수', fontsize=12)
    plt.savefig(GRAPH_PATH)
    plt.close()

@app.route('/')
def index():
    
    if not os.path.exists(GRAPH_PATH):
        create_graph()
    return render_template('index.html', graph_path=GRAPH_PATH)

@app.route('/filter', methods=['POST'])
def filter_data():
    cause = request.form.get('cause')
    filtered_data = data[data['사고원인'] == cause]
    table_html = filtered_data.to_html(classes='table table-bordered').strip()
    return render_template('filter.html', tables=table_html, cause=cause)

if __name__ == '__main__':
    app.run(debug=True)