#!/usr/bin/env python3
'''List based routines'''

def me_lists(args):
    print("me_lists...")
    
    if args:
        print(vars(args))
    me_lists_one(args)

def me_lists_one(args):
    print("me_lists_one")
