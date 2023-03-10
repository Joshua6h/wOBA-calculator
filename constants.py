# Results dictionary is the dictionary giving the possible results of each state
# A state is an ordered pair of a base state and number of outs
# "a": nobody on
# "b": runner on first
# "c": runner on second
# "d": runner on third
# "e": runners on first and second
# "f": runners on first and third
# "g": runners on second and third
# "h": bases loaded
# The key value pairs are a state and a dictionary of outcomes and new states
# "O": out
# "P": productive out - means a runner would score from third with less than two outs
# "K": strikeout - currently not being used
# "W": walk
# "S": single
# "D": double
# "T": triple
# "H": home run
# Details on assumptions are listed in the README

result_dictionary = {
        # nobody on, 0 outs
    ("a", 0): {
        "O": (("a", 1), 0),
        "P": (("a", 1), 0),
        "K": (("a", 1), 0),
        "W": (("b", 0), 0),
        "S": (("b", 0), 0),
        "D": (("c", 0), 0),
        "T": (("d", 0), 0),
        "H": (("a", 0), 1),
    },
    # nobody on, 1 out
    ("a", 1): {
        "O": (("a", 2), 0),
        "P": (("a", 2), 0),
        "K": (("a", 2), 0),
        "W": (("b", 1), 0),
        "S": (("b", 1), 0),
        "D": (("c", 1), 0),
        "T": (("d", 1), 0),
        "H": (("a", 1), 1),
    },
    # nobody on, 2 out
    ("a", 2): {
        "O": (("a", 3), 0),
        "P": (("a", 3), 0),
        "K": (("a", 3), 0),
        "W": (("b", 2), 0),
        "S": (("b", 2), 0),
        "D": (("c", 2), 0),
        "T": (("d", 2), 0),
        "H": (("a", 2), 1),
    },
    # runner on first, nobody out
    ("b", 0): {
        "O": (("b", 1), 0),
        "P": (("b", 1), 0),
        "K": (("b", 1), 0),
        "W": (("e", 0), 0),
        "S": (("e", 0), 0),
        "D": (("c", 0), 1),
        "T": (("d", 0), 1),
        "H": (("a", 0), 2),
    },
    # runner on first, one out
    ("b", 1): {
        "O": (("b", 2), 0),
        "P": (("b", 2), 0),
        "K": (("b", 2), 0),
        "W": (("e", 1), 0),
        "S": (("e", 1), 0),
        "D": (("c", 1), 1),
        "T": (("d", 1), 1),
        "H": (("a", 1), 2),
    },
    # runner on first, two outs
    ("b", 2): {
        "O": (("b", 3), 0),
        "P": (("b", 3), 0),
        "K": (("b", 3), 0),
        "W": (("e", 2), 0),
        "S": (("e", 2), 0),
        "D": (("c", 2), 1),
        "T": (("d", 2), 1),
        "H": (("a", 2), 2),
    },
    # runner on second, nobody out
    ("c", 0): {
        "O": (("c", 1), 0),
        "P": (("c", 1), 0),
        "K": (("c", 1), 0),
        "W": (("e", 0), 0),
        "S": (("b", 0), 1),
        "D": (("c", 0), 1),
        "T": (("d", 0), 1),
        "H": (("a", 0), 2),
    },
    # runner on second, one out
    ("c", 1): {
        "O": (("c", 2), 0),
        "P": (("c", 2), 0),
        "K": (("c", 2), 0),
        "W": (("e", 1), 0),
        "S": (("b", 1), 1),
        "D": (("c", 1), 1),
        "T": (("d", 1), 1),
        "H": (("a", 1), 2),
    },
    # runner on second, two outs
    ("c", 2): {
        "O": (("c", 3), 0),
        "P": (("c", 3), 0),
        "K": (("c", 3), 0),
        "W": (("e", 2), 0),
        "S": (("b", 2), 1),
        "D": (("c", 2), 1),
        "T": (("d", 2), 1),
        "H": (("a", 2), 2),
    },
    # runner on third, nobody out
    ("d", 0): {
        "O": (("d", 1), 0),
        "P": (("a", 1), 1),
        "K": (("d", 1), 0),
        "W": (("f", 0), 0),
        "S": (("b", 0), 1),
        "D": (("c", 0), 1),
        "T": (("d", 0), 1),
        "H": (("a", 0), 2),
    },
    # runner on third, one out
    ("d", 1): {
        "O": (("d", 2), 0),
        "P": (("a", 2), 1),
        "K": (("d", 2), 0),
        "W": (("f", 1), 0),
        "S": (("b", 1), 1),
        "D": (("c", 1), 1),
        "T": (("d", 1), 1),
        "H": (("a", 1), 2),
    },
    # runner on third, two outs
    ("d", 2): {
        "O": (("d", 3), 0),
        "P": (("a", 3), 0),
        "K": (("d", 3), 0),
        "W": (("f", 2), 0),
        "S": (("b", 2), 1),
        "D": (("c", 2), 1),
        "T": (("d", 2), 1),
        "H": (("a", 2), 2),
    },
    # runners on first and second, nobody out
    ("e", 0): {
        "O": (("e", 1), 0),
        "P": (("e", 1), 0),
        "K": (("e", 1), 0),
        "W": (("h", 0), 0),
        "S": (("e", 0), 1),
        "D": (("c", 0), 2),
        "T": (("d", 0), 2),
        "H": (("a", 0), 3),
    },
    # runners on first and second, one out
    ("e", 1): {
        "O": (("e", 2), 0),
        "P": (("e", 2), 0),
        "K": (("e", 2), 0),
        "W": (("h", 1), 0),
        "S": (("e", 1), 1),
        "D": (("c", 1), 2),
        "T": (("d", 1), 2),
        "H": (("a", 1), 3),
    },
    # runners on first and second, two outs
    ("e", 2): {
        "O": (("e", 3), 0),
        "P": (("e", 3), 0),
        "K": (("e", 3), 0),
        "W": (("h", 2), 0),
        "S": (("e", 2), 1),
        "D": (("c", 2), 2),
        "T": (("d", 2), 2),
        "H": (("a", 2), 3),
    },
    # runners on first and third, nobody out
    ("f", 0): {
        "O": (("f", 1), 0),
        "P": (("b", 1), 1),
        "K": (("f", 1), 0),
        "W": (("h", 0), 0),
        "S": (("e", 0), 1),
        "D": (("c", 0), 2),
        "T": (("d", 0), 2),
        "H": (("a", 0), 3),
    },
    # runners on first and third, one out
    ("f", 1): {
        "O": (("f", 2), 0),
        "P": (("b", 2), 1),
        "K": (("f", 2), 0),
        "W": (("h", 1), 0),
        "S": (("e", 1), 1),
        "D": (("c", 1), 2),
        "T": (("d", 1), 2),
        "H": (("a", 1), 3),
    },
    # runners on first and third, two outs
    ("f", 2): {
        "O": (("f", 3), 0),
        "P": (("b", 3), 0),
        "K": (("f", 3), 0),
        "W": (("h", 2), 0),
        "S": (("e", 2), 1),
        "D": (("c", 2), 2),
        "T": (("d", 2), 2),
        "H": (("a", 2), 3),
    },
    # runners on second and third, nobody out
    ("g", 0): {
        "O": (("g", 1), 0),
        "P": (("c", 1), 1),
        "K": (("g", 1), 0),
        "W": (("h", 0), 0),
        "S": (("b", 0), 2),
        "D": (("c", 0), 2),
        "T": (("d", 0), 2),
        "H": (("a", 0), 3),
    },
    # runners on second and third, one out
    ("g", 1): {
        "O": (("g", 2), 0),
        "P": (("c", 2), 1),
        "K": (("g", 2), 0),
        "W": (("h", 1), 0),
        "S": (("b", 1), 2),
        "D": (("c", 1), 2),
        "T": (("d", 1), 2),
        "H": (("a", 1), 3),
    },
    # runners on second and third, two outs
    ("g", 2): {
        "O": (("g", 3), 0),
        "P": (("c", 3), 0),
        "K": (("g", 3), 0),
        "W": (("h", 2), 0),
        "S": (("b", 2), 2),
        "D": (("c", 2), 2),
        "T": (("d", 2), 2),
        "H": (("a", 2), 3),
    },
    # bases loaded, nobody out
    ("h", 0): {
        "O": (("h", 1), 0),
        "P": (("e", 1), 1),
        "K": (("h", 1), 0),
        "W": (("h", 0), 1),
        "S": (("e", 0), 2),
        "D": (("c", 0), 3),
        "T": (("d", 0), 3),
        "H": (("a", 0), 4),
    },
    # bases loaded, one out
    ("h", 1): {
        "O": (("h", 2), 0),
        "P": (("e", 2), 1),
        "K": (("h", 2), 0),
        "W": (("h", 1), 1),
        "S": (("e", 1), 2),
        "D": (("c", 1), 3),
        "T": (("d", 1), 3),
        "H": (("a", 1), 4),
    },
    # bases loaded, two outs
    ("h", 2): {
        "O": (("h", 3), 0),
        "P": (("e", 3), 0),
        "K": (("h", 3), 0),
        "W": (("h", 2), 1),
        "S": (("e", 2), 2),
        "D": (("c", 2), 3),
        "T": (("d", 2), 3),
        "H": (("a", 2), 4),
    }
}