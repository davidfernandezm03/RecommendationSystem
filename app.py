from flask import Flask, render_template, request, url_for
from neo4jconn import Neo4jConnection
from querys import *
from pyvis.network import Network
import os
import json

app = Flask(__name__)

def create_network(animes_nodes, profiles_nodes, edges):
    folder = os.path.join('templates', 'network')
    name_html = 'result.html'
    file = os.path.join(folder, name_html)
    if os.path.exists(file):
        os.remove(file)

    net = Network(height='600px', width='100%', bgcolor='#ffffff', directed=True, font_color='white')

    for node in animes_nodes:
        net.add_node(node, label=node, shape='box', title=node, color='#97C2FC')

    for node in profiles_nodes:
        net.add_node(node, label=node, shape='ellipse', title=node, color='#030233')

    for e in edges:
        net.add_edge(e[0], e[1])

    net.write_html(file)

@app.route('/', methods=('GET', 'POST'))
def index():
    connectivity = True if conn.connectivity else False

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False

    return render_template('index.html', connectivity=connectivity)

@app.route('/query1', methods=('GET', 'POST'))
def query1():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            response = conn.run_query(query_1)

    return render_template('query1.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query2', methods=('GET', 'POST'))
def query2():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            response = conn.run_query(query_2)

    return render_template('query2.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query3', methods=('GET', 'POST'))
def query3():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            title = request.form['title']
            parameters = {'title': title}
            response = conn.run_query(query_3, parameters)

    return render_template('query3.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query4', methods=('GET', 'POST'))
def query4():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            genre = request.form['genre']
            min_episodes = float(request.form['min_episodes'])
            max_episodes = float(request.form['max_episodes'])
            max_results = int(request.form['max_results'])
            parameters = {'min_episodes': min_episodes,
                          'max_episodes': max_episodes,
                          'max_results': max_results
                          }
            response = conn.run_query(query_4.format(genre=genre),
                                      parameters)

    return render_template('query4.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query5', methods=('GET', 'POST'))
def query5():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            max_results = int(request.form['max_results'])
            parameters = {'max_results': max_results}
            response = conn.run_query(query_5, parameters)

    return render_template('query5.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query6', methods=('GET', 'POST'))
def query6():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            gender = request.form['gender']
            title = request.form['title']
            max_results = int(request.form['max_results'])
            parameters = {'gender': gender,
                          'title': title,
                          'max_results': max_results
                          }
            response = conn.run_query(query_6, parameters)

            a_nodes = [title]
            p_nodes = [x['user'] for x in response]
            edges = [(x, title) for x in p_nodes]
            create_network(a_nodes, p_nodes, edges)

    return render_template('query6.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query7', methods=('GET', 'POST'))
def query7():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            name = request.form['name']
            parameters = {'name': name}
            response = conn.run_query(query_7, parameters)

            a_nodes = [x['title'] for x in response]
            p_nodes = [name]
            edges = [(name, x) for x in a_nodes]
            create_network(a_nodes, p_nodes, edges)

    return render_template('query7.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query8', methods=('GET', 'POST'))
def query8():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            title = request.form['title']
            parameters = {'title': title}
            response = conn.run_query(query_8, parameters)

    return render_template('query8.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query9', methods=('GET', 'POST'))
def query9():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            genre = request.form['genre']
            gender = request.form['gender']
            min_score = float(request.form['min_score'])
            max_score = float(request.form['max_score'])
            max_results = int(request.form['max_results'])
            parameters = {'gender': gender,
                          'min_score': min_score,
                          'max_score': max_score,
                          'max_results': max_results
                          }
            response = conn.run_query(query_9.format(genre=genre), parameters)

    return render_template('query9.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query10', methods=('GET', 'POST'))
def query10():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            max_results = int(request.form['max_results'])
            parameters = {'max_results': max_results}
            response = conn.run_query(query_10, parameters)

    return render_template('query10.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query11', methods=('GET', 'POST'))
def query11():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            title_1 = request.form['title_1']
            title_2 = request.form['title_2']
            title_3 = request.form['title_3']
            parameters = {'title_1': title_1,
                          'title_2': title_2,
                          'title_3': title_3
                          }
            response = conn.run_query(query_11, parameters)

            a_nodes = [title_1, title_2, title_3]
            p_nodes = [x['user'] for x in response]
            edges = [(x, y) for x in p_nodes for y in a_nodes]
            create_network(a_nodes, p_nodes, edges)

    return render_template('query11.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query12', methods=('GET', 'POST'))
def query12():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            title = request.form['title']
            gender = request.form['gender']
            max_results = int(request.form['max_results'])
            parameters = {'title': title,
                          'gender': gender,
                          'max_results': max_results}
            response = conn.run_query(query_12, parameters)

    return render_template('query12.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query13', methods=('GET', 'POST'))
def query13():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            title = request.form['title']
            max_results = int(request.form['max_results'])
            parameters = {'title': title,
                          'max_results': max_results
                          }
            response = conn.run_query(query_13, parameters)

    return render_template('query13.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query14', methods=('GET', 'POST'))
def query14():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            title_1 = request.form['title_1']
            title_2 = request.form['title_2']
            gender = request.form['gender']
            max_results = int(request.form['max_results'])
            parameters = {'title_1': title_1,
                          'title_2': title_2,
                          'gender': gender,
                          'max_results': max_results}
            response = conn.run_query(query_14, parameters)

    return render_template('query14.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/query15', methods=('GET', 'POST'))
def query15():
    connectivity = True if conn.connectivity else False
    response = None

    if request.method == 'POST':
        if 'check_db' in request.form:
            conn.verify_connectivity()
            connectivity = True if conn.connectivity else False
        elif 'run_query' in request.form:
            genre = request.form['genre']
            gender = request.form['gender']
            min_score = float(request.form['min_score'])
            max_results = int(request.form['max_results'])
            parameters = {'gender': gender,
                          'min_score': min_score,
                          'max_results': max_results
                          }
            response = conn.run_query(query_15.format(genre=genre), parameters)

    return render_template('query15.html',
                           connectivity=connectivity,
                           response=response
                           )

@app.route('/network', methods=('GET', 'POST'))
def network():
    return render_template('network/result.html')

if __name__ == "__main__":
    credentials = os.path.join('config', 'credentials.json')
    with open(credentials) as file:
        conf = json.load(file)

    uri = conf['uri']
    user = conf['user']
    password = conf['password']
    db = conf['db']

    conn = Neo4jConnection(uri, user, password, db)
    app.run(debug=True, host='0.0.0.0', port=5000)
    conn.close()