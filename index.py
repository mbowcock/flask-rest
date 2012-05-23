from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'App Root'

@app.route('/resources')
def api_resource():
    return 'List of '.format(url_for('api_resource'))

@app.route('/resource/<resourceid>')
def api_resource(resourceid):
    return 'Viewing {0}'.format(resourceid)

if __name__ == '__main__':
    app.run()
