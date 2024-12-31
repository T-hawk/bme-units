PREFIXES = {
    "E": 1e18,
    "P": 1e15,
    "T": 1e12,
    "G": 1e9,
    "M": 1e6,
    "k": 1e3,
    "h": 1e2,

    "d": 1e-1,
    "c": 1e-2,
    "m": 1e-3,
    "u": 1e-6,
    "n": 1e-9,
    "p": 1e-12,
    "f": 1e-15,
    "a": 1e-18,
}

SI = [
    "m",
    "Pa"
]

TYPES = {
    "pressure": {
        "Pa": 1,
        "mmHg": 7.50062e-3,
        "atm": 9.86923e-6
    },
    "distance": {
        "m": 1.0,
        "ft": 3.28084,
        "in": 39.3701
    }
}

class Number:
    def __init__(self, value, unit):
        self.value = value
        self.type = ""

        for type in TYPES:
            if unit in TYPES[type]:
                self.type = type

        self.full_unit = unit

        # Find type and validate unit
        prefix = ""
        if not self.type:
            prefix = unit[0]
            unit = unit[1:]
            for type in TYPES:
                if unit in TYPES[type]:
                    self.type = type

        if not self.type: raise Exception("'" + unit + "' not a valid unit.")

        self.unit = unit

        # Validate prefix

        self.prefix_factor = 1

        if not prefix:
            self.prefix_factor = 1
        elif prefix in PREFIXES:
            self.prefix_factor = PREFIXES[prefix]
        else:
            raise Exception("'" + prefix + "' not a valid prefix")

        self.prefix = prefix

        if self.prefix and self.unit not in SI: raise Exception("'" + self.unit + "' cannot have a prefix")

    # Returns another Number
    def convert(self, other_unit):
        if self.type != other_unit.type: raise Exception("Unit types do not match")

        conversion_factor = (self.prefix_factor * TYPES[other_unit.type][other_unit.unit]) / (other_unit.prefix_factor * TYPES[self.type][self.unit])
        new_value = self.value * conversion_factor
        return Number(new_value, other_unit.full_unit)
