import math

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                       'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                       'The Night Listener': 3.0},
        'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                        'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                        'You, Me and Dupree': 3.5},
        'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                            'Superman Returns': 3.5, 'The Night Listener': 4.0},
        'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                        'The Night Listener': 4.5, 'Superman Returns': 4.0,
                        'You, Me and Dupree': 2.5},
        'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                        'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                        'You, Me and Dupree': 2.0},
        'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                        'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
        'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

def similarity(person1, person2):

    intersection = set(critics[person1].keys()) & set(critics[person2].keys())
    union = set(critics[person1].keys()) | set(critics[person2].keys())

    person1_items = 0
    person2_items = 0
    inner = 0
    for item in list(intersection):
        person1_items += critics[person1][item] ** 2
        person2_items += critics[person2][item] ** 2
        inner += critics[person1][item] * critics[person2][item]
    distance = inner / (math.sqrt(person1_items) * math.sqrt(person2_items))
    return person2, distance * len(intersection) / len(union)
            

def commendation(person):
    persons = [similarity(person, per) for per in critics.keys() if person != per]
    better_persons = filter(lambda person: person[1] > 0.5, persons)
    items_all = reduce(lambda item_set1, item_set2: set(item_set1) | set(item_set2), map(lambda person: person.keys(), critics.values()))
    back = []
    for item in items_all:
        count = 0
        if item not in critics[person]:
            for p in better_persons:
                if item in critics[p[0]]:
                    count += p[1] * critics[p[0]][item]
        else:
            continue
        back.append((item, count))

    return back
    
    
print commendation('Toby')
