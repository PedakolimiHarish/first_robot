#!/usr/bin/env python
s = input("enter")
key_mapping = {'w': [0, 1], 'x': [0, -1],
               'a': [-1, 0], 'd': [1, 0],
               's': [0, 0]}

def keys_cb(msg):

    vels = key_mapping[msg[0]]
    
    print(vels[0])
    print(vels[1])
    

if __name__ == '__main__':
    keys_cb(s)
