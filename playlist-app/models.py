"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    def __repr__(self):
        pl = self
        return f"<PlayList id = {pl.id} name = {pl.name} description: {pl.description}>"

    __tablename__ = "playlists"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    playlist_song = db.relationship('PlaylistSong', backref="playlist")


class Song(db.Model):
    """Song."""

    def __repr__(self):
        s = self
        return f"<Song id = {s.id} title = {s.title} artist: {s.artist}>"
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)
    playlist_song = db.relationship('PlaylistSong', backref="songs")


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    def __repr__(self):
        ps = self
        return f"<PlaylistSong id = {ps.id} playlist_id = {ps.playlist_id} song_id: {ps.song_id}>"

    __tablename__ = "playlists_songs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey(
        'playlists.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey(
        'songs.id'), primary_key=True)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
