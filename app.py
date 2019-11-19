from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from lobby import Members
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/secretSanta')
# client = MongoClient(host=f'{host}?retryWrites=false')
# db = client.get_default_database()
client = MongoClient()
db = client.secretSanta
ss_room = db.ss_room

app = Flask(__name__)

@app.route('/')
def index(is_lobby=True):
    """index route"""
    return render_template('index.html', is_lobby=is_lobby)

@app.route('/', methods=['POST'])
def get_room():
    """processes room lookup and redirects to the room"""
    room_name = request.form.get('lobby_lookup')
    show_lobby(room_name)

@app.route('/new_lobby')
def show_lobby_form():
    """ Shows the form to make a new name"""
    return render_template('new_lobby.html', if_exist=False)

@app.route('/new_lobby', methods=['POST'])
def make_lobby():
    """check if lobby name exists, if not, create it"""
    temp_lobby_name = request.form.get('lobby_name')
    if ss_room.find_one({'lobby_name': temp_lobby_name}): # name already exists
        return render_template('new_lobby.html', if_exist=True)
    else:
        new_lobby = {
            'lobby_name': temp_lobby_name,
            'members': []
        }
        ss_room.insert_one(new_lobby)
        return redirect(url_for('show_lobby', lobby_name=temp_lobby_name))

@app.route('/lobby/<lobby_name>')
def show_lobby(lobby_name):
    """shows the lobby for the particular lobby name"""
    room = ss_room.find_one({'lobby_name': lobby_name})
    if room: 
        return render_template('show_lobby.html', lobby=room)
    else:
        return redirect(url_for('index', is_lobby=False))
        
