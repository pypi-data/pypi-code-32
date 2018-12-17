from cpbox.tool import redistool
from cpbox.tool import local_cache

FROM_LOCAL_CACHE = 1
FROM_REDIS = 2
FROM_SLOW_OP = 3

class CacheUnit(object):

    def __init__(self, key, get_fn, expire=3600):
        self.key = key
        self.get_fn = get_fn
        self.expire = expire

    def fetch(self):
        return fetch(self.key, self.get_fn, None, None, self.expire)

    def invalid(self):
        delete(self.key)

def set_redis_url(url):
    redistool.init_proxy(url)

def delete(key):
    local_cache.delete(key)
    redistool.delete(key)

def fetch(key, get_fn, on_to_local_fn=False, return_filter_fn=False, expire=3600):
    get_key_fn = lambda key:key
    get_list_fn = lambda _ids:{key: get_fn(key)}
    return fetch_list(key, get_key_fn, get_list_fn, on_to_local_fn, return_filter_fn, expire)

def _get_list_from_cache_and_local_cache(keys, use_local_cache=True, on_to_local_fn=None, return_from_tag=False):
    list = {}
    un_hit_keys = []
    if use_local_cache:
        for key in keys:
            if local_cache.has(key):
                list[key] = (local_cache.get(key), FROM_LOCAL_CACHE) if return_from_tag else local_cache.get(key)
            else:
                un_hit_keys.append(key)
    else:
        un_hit_keys = keys

    if un_hit_keys:
        list_from_cache = redistool.get_list(un_hit_keys)
        for key, item in list_from_cache.items():
            if callable(on_to_local_fn):
                item = on_to_local_fn(key, item)
            list[key] = (item, FROM_REDIS) if return_from_tag else item
            local_cache.set(key, item)
    return list

def _fetch_list_from_cache(id_to_key_map, on_to_local_fn=None, use_local_cache=True, return_from_tag=False):
    keys = id_to_key_map.values()
    if callable(on_to_local_fn):
        key_to_id_map = {v: k for k, v in id_to_key_map.items()}
        def on_to_local_fn_proxy(key, item):
            id = key_to_id_map[key]
            return on_to_local_fn(id, item)
        return _get_list_from_cache_and_local_cache(keys, use_local_cache, on_to_local_fn_proxy, return_from_tag)
    else:
        return _get_list_from_cache_and_local_cache(keys, use_local_cache, None, return_from_tag)

def set_to_cache_for_fetch(id, raw_item, key=None, get_key_fn=None, on_to_local_fn=None, expire=600):
    if key is None and get_key_fn is None:
        raise Error('key or get_key_fn must be defined')

    if not key:
        key = get_key_fn(id)

    item = raw_item
    if on_to_local_fn:
        item = on_to_local_fn(id, raw_item)
    if expire > 0:
        redistool.set(key, raw_item, expire)
        local_cache.set(key, item, expire)
    return item

def fetch_list(ids, get_key_fn, get_list_fn, on_to_local_fn=None, return_filter_fn=None, expire=600, return_from_tag=False):
    '''
    1. if expire >= 0, will try to use local cache and redis;
       the raw result generated by get_list_fn will be cached to both cache.

    2. if expire == 0, will not fetch from local cache
    '''
    if not ids:
        return []

    is_list = isinstance(ids, list)
    if not is_list:
        ids = [ids]

    id_to_key_map = {}
    for id in ids:
        id_to_key_map[id] = get_key_fn(id)

    cache_list = {}
    if expire >= 0:
        cache_list = _fetch_list_from_cache(id_to_key_map, on_to_local_fn, expire > 0, return_from_tag)

    un_hit_ids = []
    result_map = {}
    for id, key in id_to_key_map.items():
        if key in cache_list:
            result_map[id] = cache_list[key]
        else:
            un_hit_ids.append(id)

    if un_hit_ids:
        raw_result = get_list_fn(un_hit_ids)
        for id, item in raw_result.items():
            key = id_to_key_map[id]
            item = set_to_cache_for_fetch(id, item, key=key, on_to_local_fn=on_to_local_fn, expire=expire)
            result_map[id] = (item, FROM_SLOW_OP) if return_from_tag else item

    filtered_result = {}
    if callable(return_filter_fn):
        for id, item in result_map.items():
            item = return_filter_fn(id, item)
            if not item:
                filtered_result[id] = item
    else:
        filtered_result = result_map

    if is_list:
        return filtered_result
    else:
        values = filtered_result.values()
        if values:
            return next(iter(values))
        else:
            return False
