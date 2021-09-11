def count_bags(bag, bags):
    result = bag[1]
    for next_bag in bags[bag[0]]:
        result += bag[1] * count_bags(next_bag, bags)

    return result


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
            content_clean.append((item, number))
    bags[container] = content_clean

print(count_bags(("shiny gold", 1), bags)-1)
