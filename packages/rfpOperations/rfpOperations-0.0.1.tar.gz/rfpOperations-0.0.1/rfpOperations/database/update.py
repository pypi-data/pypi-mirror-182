from typing import List
from .instance import Session, engine, Property, Feature
from ..identifier.hash_p_feature import hash_feature


def update(given_data: List, prev_hashes: List):
    """update database based on given data"""
    local_sess = Session(bind=engine)

    for p in given_data:
        prop_to_update = (
            local_sess.query(Property).filter(Property.id == p["id"]).first()
        )

        prop_to_update.price = p["price"]
        prop_to_update.beds = p["num_beds"]
        prop_to_update.baths = p["num_baths"]
        prop_to_update.liv_rooms = p["num_liv_rooms"]
        prop_to_update.address = p["address"]
        updated_prop = prop_to_update

        updated_ftrs = (
            updated_prop.price,
            updated_prop.beds,
            updated_prop.baths,
            updated_prop.liv_rooms,
            updated_prop.address,
        )

        f_instance = local_sess.query(Feature).filter(Feature.id == p["id"]).first()
        f_instance.hash = hash_feature(updated_ftrs)
        try:
            prev_hash = [pair[1] for pair in prev_hashes if pair[0] == updated_prop.id][0]
        except IndexError:
            prev_hash = ""

        f_instance.prev_hash = prev_hash

    local_sess.commit()
