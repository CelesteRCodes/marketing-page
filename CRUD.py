from model import User, db, connect_to_db

def create_user(name, email):
    """ 
    For example:

    >>> create_user("celeste r", "celestercodes@gmail.com")

    [<User 6>]
    """
    user = User(name = name, email = email)
    

    db.session.add(user)
    db.session.commit()
    return user


if __name__ == '__main__':
    from server import app
    connect_to_db(app)