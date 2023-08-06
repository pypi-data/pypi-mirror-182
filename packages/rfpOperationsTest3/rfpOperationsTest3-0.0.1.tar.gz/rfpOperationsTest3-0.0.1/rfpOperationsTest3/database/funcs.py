from .property import Feature, Property, Session, engine

def get_id_hist(id_hist=set()):
    local_sess = Session(bind=engine)

    props = local_sess.query(Property).all()

    for prop in props:
        id_hist.add(prop.id)

    """
    for value in local_sess.query(Property.id).distinct():
        id_hist.add(value[0])
    """

    return id_hist


def get_hashes(data):
    """get all hash values from given data"""
    local_sess = Session(bind=engine)
    hashes = []

    for p in data:
        try:
            ftr = (
                    local_sess.query(Feature).filter(Feature.id == p["id"]).first()
                )  # get the one with given id
            hash = ftr.hash
            id = ftr.id
            hashes.append((id, hash))

        except AttributeError:
            print(f"Newly created property is not in the database yet...")

    return hashes


def get_props():    
    local_sess = Session(bind=engine)

    return local_sess.query(Property).all()


def get_ftrs():
    local_sess = Session(bind=engine)

    return local_sess.query(Feature).all()
