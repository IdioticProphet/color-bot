def spacify(string):
        return "".join([char.upper()+" " for char in string if char != " "]).strip()
