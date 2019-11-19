from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
import random
from send_email import send_email

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
    return redirect(url_for('show_lobby', lobby_name=room_name, ))

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

@app.route('/lobby/<lobby_name>', methods=['POST'])
def send_lobby(lobby_name):
    """makes draws and sends emails"""
    email_list = {}
    room = ss_room.find_one({'lobby_name': lobby_name})
    members = []
    # make dict for information dict
    info_dict = {}
    for member in room['members']:
        info_dict[member[0]] = [member[1], member[2]]
        members.append(member[0])
    # make dict for draws
    draws = {}
    draws[members[0]] = members[len(members) -1]
    for index in range(1, len(members)):
        draws[members[index]] = members[index-1]


    #pass everything to emailsender function
    send_email(draws, info_dict)

    return redirect(url_for('show_lobby', lobby_name=lobby_name))

@app.route('/lobby/<lobby_name>/save', methods=['POST'])
def save_data(lobby_name):
    """Saves the infromation stored"""
    form = request.form.to_dict()
    ctr = 1
    members_list = []
    while True:
        if f'person{ctr}-name' in form.keys():
            lis = [form[f'person{ctr}-name'], form[f'person{ctr}-email'], form[f'person{ctr}-address']]
            members_list.append(lis)
            ctr += 1
        else: 
            break
    updated_item = {
        'lobby_name': lobby_name,
        'members': members_list
    }
    ss_room.update_one(
        {"lobby_name": lobby_name},
        {'$set': updated_item}
    )
    return redirect(url_for('show_lobby', lobby_name=lobby_name))
