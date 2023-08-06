from typing import List
from .funcs import get_id_hist
from ..identifier.hash_p_feature import hash_feature
from .instance import Property, Session, engine, Feature

def create(data: List):
    """create new instances from fresh data"""
    local_sess = Session(bind=engine)

    id_hist = get_id_hist()

    for property in data:
        new_property = Property(
            id=int(property["id"]),
            price=property["price"],
            beds=property["num_beds"],
            baths=property["num_baths"],
            liv_rooms=property["num_liv_rooms"],
            address=property["address"],
        )
        feautures = (
            new_property.price,
            new_property.beds,
            new_property.baths,
            new_property.liv_rooms,
            new_property.address,
        )
        hashed_features = hash_feature(feautures)
        new_features = Feature(id=int(property["id"]), hash=hashed_features, prev_hash="")

        if new_property.id not in id_hist:  # Avoid unique key error
            local_sess.add(new_property)
            local_sess.add(new_features)

    local_sess.commit()
