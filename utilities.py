from collections import defaultdict
groups = defaultdict(list)

def group(req_data, group_by=None):

    res_data = [item.__dict__ for item in req_data]
    def del_key(d):
        del d['_sa_instance_state']
        return d
    res_data = map(del_key, res_data)
    if group_by is not None:
        for obj in res_data:
            groups[obj[group_by]].append(obj)
        res_data = groups.values()
    return res_data