from .app import db, login_manager
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired
from flask_login import UserMixin

# Table intermédiaire pour la relation many-to-many (User et Book)
favorites = db.Table('favorites',
    db.Column('user_id', db.String(80), db.ForeignKey('user.username'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):  # C'est un toString
        return "<Author (%d) %s>" % (self.id, self.name)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    img = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author', backref=db.backref('books', lazy='dynamic'))

    def __repr__(self):
        return "<Book (%d) %s>" % (self.id, self.title)


class AuthorForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nom', validators=[DataRequired()])


def get_sample():
    return Book.query.all()  # Récupère tous les livres (limite optionnelle)

def get_book(book_id):
    return Book.query.get(book_id)


def get_author(id):
    return Author.query.get(id)


class User(db.Model, UserMixin):  # Utilisation de UserMixin pour simplifier
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))

    # Relation Many-to-Many avec la table 'favorites'
    favorite_books = db.relationship('Book', secondary=favorites, backref=db.backref('favorited_by', lazy='dynamic'))

    def get_id(self):
        return self.username


@login_manager.user_loader
def load_user(username):
    return User.query.get(username)


class BookForm(FlaskForm):    
    id = HiddenField('id')
    price = StringField('Prix', validators=[DataRequired()])
    title = StringField('Titre', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
    img = StringField('Image', validators=[DataRequired()])
    author = SelectField('Auteur', coerce=int)  # SelectField avec coerce=int pour gérer les IDs d'auteurs


    def __repr__(self):
        return "<Book (%d) %s>" % (self.id, self.title)