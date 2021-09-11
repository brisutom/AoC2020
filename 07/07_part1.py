def contains_gold(bag, bags):
    for next_bag in bags[bag]:
        if next_bag == "shiny gold":
            return True
        else:
            if contains_gold(next_bag, bags):
                return True
    return False


lines = [x.strip("\n") for x in open("input.txt").readlines()]
bags = {}
for line in lines:
    line = line.replace(" bags", "").replace(" bag", "").replace(".", "")
    container, content = line.split(" contain ")
    content = content.split(", ")
    content_clean = []
    for pre_item in content:
        number, item = pre_item.split(" ", 1)
        if number != "no":
            number = int(number)
            content_clean.append(item)
    bags[container] = content_clean

result = 0
for bag in bags:
    if contains_gold(bag, bags):
        result += 1

print(result)
