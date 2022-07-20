map_={
    'key':'value',
    'key2':'value',
}
# map_.update({'company':'regex'})
print(map_)
print(map_.get('company','Not Found'))
# map_.fromkeys
map_['name']='agarwal'
print(map_.pop('key'))
print(map_)
print(map_.popitem())
print(map_)
print(map_.items())
map_['name']='agarwal'
x=map_.values()
print(x)
map_["color"] = "red"
print(x)
del map_['color']
print(map_)