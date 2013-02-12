import pyparsing as pp


def parse_keyvalues_file(file_like):
    """An extremely lenient key values file parser

    See: https://developer.valvesoftware.com/wiki/KeyValues
    """
    # a quoted string
    quoted = pp.dblQuotedString.setParseAction(pp.removeQuotes)

    # a data value
    keyval = pp.Dict(pp.Group(quoted + quoted))

    # a hash
    hashstart = pp.Suppress('{')
    hashname = quoted
    hashend = pp.Suppress('}')

    # the nested elements
    expr = pp.Forward()
    value = pp.ZeroOrMore(expr | keyval)
    hashval = pp.Dict(pp.Group(hashname + hashstart + value  + hashend))
    expr << hashval

    # ignore c++ style comments
    expr = expr.ignore(pp.cppStyleComment)

    return expr.parseFile(file_like)


if __name__ == '__main__':
    parse_keyvalues_file('data/items.txt')
