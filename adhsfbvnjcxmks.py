dict={"nice": 69,
    "nice bro": 69420,
    "AGH!": 9000,
    "dude": 420,
    "git gud": 1337}
print(type(sorted(dict, key=dict.__getitem__, reverse=True)))