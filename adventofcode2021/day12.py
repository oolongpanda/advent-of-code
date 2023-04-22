with open('input/day12.txt') as f:
    input = [l.strip() for l in f.readlines()]
    dict = {}
    for i in input:
        individualread = i.split('-')
        if individualread[0] not in dict:
            dict.update({individualread[0]:{individualread[1]}})
        if individualread[0] in dict:
            newset = dict[individualread[0]]
            newset.update({individualread[1]})
            dict.update({individualread[0]:newset})
        if individualread[1] not in dict:
            dict.update({individualread[1]:{individualread[0]}})
        if individualread[1] in dict:
            newset = dict[individualread[1]]
            newset.update({individualread[0]})
            dict.update({individualread[1]:newset})
    
    paths = []
    completepaths = []
    for i in dict['start']:
        if i != 'end':
            paths += [['start', i]]
        else:
            completepaths += [['start', i]]

    while len(paths) != 0:
        newpaths = []
        for path in paths:
            working = []
            for i in dict[path[-1]]:
                if i not in path or i.isupper():
                    if i == 'end':
                        completepaths += [path + [i]]
                    else:
                        working += [path + [i]]
            newpaths += working
        paths = newpaths

    print ('Task 1:', len(completepaths))

    paths = []
    completepaths = []
    for i in dict['start']:
        if i != 'end':
            paths += [['start', i]]
        else:
            completepaths += [['start', i]]

    while len(paths) != 0:
        newpaths = []
        for path in paths:
            double = False
            for cave in path:
                if cave.islower() and path.count(cave) == 2:
                    double = True
                elif cave.islower() and path.count(cave) > 2:
                    print ('reeeeee')
            working = []
            for i in dict[path[-1]]:
                if double:
                    if i not in path or i.isupper():
                        if i == 'end':
                            completepaths += [path + [i]]
                        else:
                            working += [path + [i]]
                else:
                    if i != 'start':
                        if i == 'end':
                            completepaths += [path + [i]]
                        else:
                            working += [path + [i]]
            newpaths += working
        paths = newpaths

    print ('Task 2:', len(completepaths))
    
    # Task 1: 3679
    # Task 2: 10739