from flask import Flask
import socket

#define flask app
app=Flask(__name__)

from views import *

if __name__ == '__main__':
	app.config['DEBUG'] = True #helps you to see changes without re-running app
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('localhost', 0))
	port = sock.getsockname()[1]
	sock.close()
	app.run(port=port)
