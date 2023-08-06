from .event import Event


def check_stats(feature):
    
    if feature.prev_hash == "":
        event = Event.CREATED
    
    if feature.prev_hash != feature.hash and feature.prev_hash != "":
        event = Event.UPDATED
        
    if feature.prev_hash == feature.hash:
        event = Event.NO_CHANGE

    return event.value

