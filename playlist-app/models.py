"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'playlist'
    id = db.Column(db.Integer,autoincrement=True,priamry_key=True)
    name = db.Column(db.Text, nullable=False,unique=True)
    description = db.Column(db.Text, nullable=False)
    playlistsong= db.relationship('PlaylistSong', backref = 'playlist', cascade = 'all,delete')

class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'song'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    title = db.Column(db.Text,nullable=False,unique=True)
    playlistsong= db.relationship('PlaylistSong', backref = 'song', cascade = 'all,delete')

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'playlistsong'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    playlist_id = db.Column(db.Integer,db.Foriegnkey('playlist.id'))
    song_id = db.Column(db.Integer,db.Foriegnkey('song.id'))


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
