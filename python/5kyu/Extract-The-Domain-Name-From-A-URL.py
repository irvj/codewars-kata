"""
https://www.codewars.com/kata/514a024011ea4fb54200004b

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"


"""


import re


def domain_name(url):
    domain_split = re.sub(r'^https?:\/\/', '', url).split('.')
    if domain_split[0] == 'www':
        domain_split.pop(0)
    return domain_split[0]


"""
Actual real world, non-exercise answer:

import tldextract

def domain_name(url):
    return tldextract.extract(url).domain

"""
