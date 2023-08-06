from typing import List
from .instance import Session, engine, Property, Feature
from .create import get_id_hist


def delete(given_data: List):
    """if some id not appears in the given data then remove it from db"""
    local_sess = Session(bind=engine)

    given_data_ids = [int(d["id"]) for d in given_data]

    for id in get_id_hist():
        if id not in given_data_ids:
            prop_to_del = local_sess.query(Property).filter(Property.id == id).first()
            local_sess.delete(prop_to_del)

            ftr_to_del = local_sess.query(Feature).filter(Feature.id == id).first()
            local_sess.delete(ftr_to_del)

            local_sess.commit()
