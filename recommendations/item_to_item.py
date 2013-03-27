def preprocess(byitems, byuser, items):
    d = {}
    for item in items:
        for usr in byitems[item]:
            for item_user in byuser[usr]:
                if item_user != item:
                    count = d.setdefault(item, {}).setdefault(item_user, 0)
                    d[item][item_user] = count + 1

        sorted_items = sorted(d[item].iteritems(), key = lambda item: item[1], reverse = True)
        d[item] = map(lambda item: item[0], sorted_items)
    return d
def item_to_item(item, data):
    return data[item]
print item_to_item('book',
                   preprocess({'tv': ['bob', 'lucy', 'jude'], 'book': ['bob', 'lucy'], 'video': ['bob']}, {'bob': ['tv', 'book', 'video'], 'lucy': ['tv', 'book'], 'jude':['tv']}, ['tv', 'book', 'video']))
                   
    
        
