import re

def count(bag):
    count, description = re.compile("^(\d+) ([a-z ]+) bags?\.?$").match(bag).groups()
    return (int(count), description)

def parse(rule):
   main_bag, contents = rule.split(" bags contain ")
   if contents == "no other bags.":
        return main_bag, []
   return main_bag, [count(bag) for bag in contents.split(', ')]

def gold_in(name, rules):
    if name == "shiny gold":
        return True
    return any(gold_in(name, names) for _, name in names[name])

with open('input.txt') as f:
    data = f.read().splitlines()
    names = dict([parse(line) for line in data])

print(sum((gold_in(name, names) and 1 or 0) for name in names if name != "shiny gold"))
