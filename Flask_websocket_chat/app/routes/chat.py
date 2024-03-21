from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from flask_socketio import join_room, leave_room
from extensions import socketio, db
from app.models.room import Room

chat = Blueprint('chat', __name__)

@chat.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        room_name = request.form.get('room')
        if Room.query.filter_by(name=room_name).first():
            flash('Room already exists.')
            return redirect(url_for('chat.create'))
        new_room = Room(name=room_name)
        db.session.add(new_room)
        db.session.commit()
        return redirect(url_for('chat.room', room_id=new_room.id))
    return render_template('create_room.html')

@chat.route('/rooms/<room_id>', methods=['GET', 'POST'])
@login_required
def room(room_id):
    room = Room.query.filter_by(id=room_id).first()
    if room:
        join_room(room.name)
        return render_template('room.html', room=room)
    else:
        flash('Room does not exist.')
        return redirect(url_for('chat.create'))