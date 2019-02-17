#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request, jsonify
import logging
from logging import Formatter, FileHandler
import os
import requests
from flask_socketio import SocketIO, send


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
def user_download():
    url = request.args['url']  # user provides url in query string
    r = requests.get(url)

    # write to a file in the app's instance folder
    # come up with a better file name
    with app.open_instance_resource( app.root_path + "/static/media" + '/sample.mp4', 'wb') as f:
        f.write(r.content)
    
    return render_template('pages/placeholder.home.html')


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
