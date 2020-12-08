import re

def count(bag):
    count, description = re.compile("^(\d+) ([a-z ]+) bags?\.?$").match(bag).groups()
    return (int(count), description)

def parser(rule):
    main_bag, contents = rule.split(" bags contain ")
    if contents == "no other bags.":
        return main_bag, []
    return main_bag, [count(bag) for bag in contents.split(', ')]

def solution(name, names):
    return 1 + sum(count * solution(name, names) for count, name in names[name])

with open('input.txt') as f:
    data = f.read().splitlines()
    names = dict([parser(line) for line in data])

print(solution("shiny gold", names) - 1)
