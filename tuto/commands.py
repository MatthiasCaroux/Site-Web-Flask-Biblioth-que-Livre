import click
from .app import app, db


@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    
    # création de toutes les tables
    db.create_all()

    # chargement de notre jeu de données
    import yaml
    books = yaml.safe_load(open(filename))
    
    # import des modèles
    from .models import Author , Book

    # première passe: création de tous les auteurs
    authors = {}
    for b in books:
        a = b["author"]
        if a not in authors :
            o = Author(name=a)
            db.session.add(o)
            authors[a] = o
            db.session.commit()
    # deuxième passe: création de tous les livres
    for b in books:
        a = authors [b["author"]]
        o = Book(price = b["price"],
        title = b["title"],
        url = b["url"],
        img = b["img"],
        author_id = a.id)
        db.session.add(o)
        db.session.commit()

@app.cli.command()
def syncdb():
    '''Create all missing tables'''
    db.create_all()


@app.cli.command()
@click.argument('username')
@click.argument('password')
def newuser(username, password):
    '''Adds a new user.'''
    from .models import User
    from hashlib import sha256

    m = sha256()
    m.update(password.encode())
    u = User(username=username, password=m.hexdigest())
    db.session.add(u)
    db.session.commit()

@app.cli.command()
@click.argument('username')
@click.argument('password')
def passwd(username, password):
    '''Changes the password of a user.'''
    from .models import User
    from hashlib import sha256

    m = sha256()
    m.update(password.encode())
    u = User.query.get(username)
    u.password = m.hexdigest()
    db.session.commit()