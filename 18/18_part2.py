lines = [x.strip("\n") for x in open("input.txt").readlines()]


def tokenize(expr):
    return expr.replace("(", " ( ").replace(")", " ) ").split()


def read_tokens(tokens):
    if len(tokens) == 0:
        raise SyntaxError("No tokens")
    token = tokens.pop(0)
    if token == "(":
        token_queue = []
        while tokens[0] != ")":
            token_queue.append(read_tokens(tokens))
        tokens.pop(0)
        return token_queue
    elif token == ")":
        raise SyntaxError("Unexpected )")
    else:
        return token


def parse(expr):
    return read_tokens(tokenize("(" + expr + ")"))


def eval_expr(expr):
    # print(expr)
    if not isinstance(expr, list) or len(expr) == 1:
        try:
            return int(expr[0])
        except TypeError:
            return eval_expr(expr[0])

    for i in range(len(expr)-1, 0, -1):
        if expr[i] == "*":
            return eval_expr(expr[i+1:]) * eval_expr(expr[:i])
    for i in range(len(expr)-1, 0, -1):
        if expr[i] == "+":
            return eval_expr(expr[i+1:]) + eval_expr(expr[:i])


result = 0
for line in lines:
    result += eval_expr(parse(line))

print(result)
