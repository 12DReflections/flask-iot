#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request, jsonify
import logging
from logging import Formatter, FileHandler
import os
import requests
from flask_socketio import SocketIO, send, emit


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@socketio.on('message')
def handMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/download_advertisment')
@socketio.on('new_content')
def user_download():
    print('=======================')
    url = request.args['url']  # user provides url in query string
    r = requests.get(url)

    # # write to a file in the app's instance folder
    # # come up with a better file name
    f_name = '/sample3.mp4'
    with app.open_instance_resource( app.root_path + "/static/media" + f_name, 'wb') as f:
        f.write(r.content)
    socketio.emit('new_content', "refresh")

    return jsonify({'result' : "success"})



#----------------------------------------------------------------------------#
# Functions.
#----------------------------------------------------------------------------#
# Donwload a Large File with requests
def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    # app.run()
    socketio.run(app)
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
