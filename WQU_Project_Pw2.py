bnf_names = {d['bnf_name'] for d in scripts}
bnf_names = [name for name in bnf_names]
assert(len(bnf_names) == 5619)

groups = {name: [] for name in bnf_names}
for script in scripts:
    name = script['bnf_name']
    if not len(groups[name]) == 0:
        groups[name].append(script['items'])
    else:
        groups[name] = [script['items']]

        def dict_sum(data):
    length = 0
    b = []
    for key in data:
        a = (key, sum(data[key]))
        b.append(a)
        length += 1
    return b

def tuple_max(data):
    maxi = 0
    key = ''
    for i in range(len(data)):
        if data[i][1] > maxi:
            maxi = data[i][1]
            key = data[i][0]
        else:
            maxi = maxi
            key = key
    return (key, maxi)

items = dict_sum(groups)
#max_item = [("", 0)]
max_item = [tuple_max(items)]

def group_by_field1(data, fields):
    groups = {name: [] for name in data}
    if len(fields) > 1:
        for i in range(len(fields)):
            groups.add(fields[i])
    groups.add(fields)
    final_group = dict()
    for script in data:
        name = data[fields]
        if not len(groups[name]) == 0:
            groups[name].append(script[fields])
        else:
            groups[name] = [script[fields]]        
    return groups

def group_by_field(data, fields):
    #print(fields)
    groups = {field: [] for field in fields }
   # print (groups)
    for g in groups: 

        for d in data:              

            for key in d:  
                #print(d)
                if g in d[g]:
                    groups[d[g]].append(g)
                else:
                    pass
    return groups
groups = group_by_field(scripts, ('bnf_name','postal_code'))
print(max_item)
print(groups)

groups = group_by_field(scripts, ('bnf_name',))
test_max_item = groups

assert test_max_item == max_item
