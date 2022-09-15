#!/usr/bin/python3
"""
    Web Flask 0.0.0.0 port 5000
"""
from flask import Flask, render_template
from models import storage
app =Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """
    List all the states
    """
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close_db(db):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
