from flask import render_template
from lucky import app

@app.route('/')
def main():
    return(render_template('index.html'))
