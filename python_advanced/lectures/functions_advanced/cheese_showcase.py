def sorting_cheeses(**kwargs):
    cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for name, quantities in cheeses:
        result += name + '\n'
        result += '\n'.join([str(x) for x in sorted(quantities, reverse=True)]) + '\n'
    return result
