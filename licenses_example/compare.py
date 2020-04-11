# built-in
from itertools import islice
from pathlib import Path
from sys import argv

# project
from textdistance import EntropyNCD


# read files
licenses = dict()
for path in Path('choosealicense.com', '_licenses').iterdir():
    licenses[path.stem] = path.read_text()

# show licenses list if no arguments passed
if len(argv) == 1:
    print(*sorted(licenses.keys()), sep='\n')
    exit(1)

# compare all with one
qval = int(argv[1]) if argv[1] else None
compare_with = argv[2]
distances = dict()
for name, content in licenses.items():
    distances[name] = EntropyNCD(qval=qval)(
        licenses[compare_with],
        content,
    )

# show 5 most similar
sorted_distances = sorted(distances.items(), key=lambda d: d[1])
for name, distance in islice(sorted_distances, 5):
    print('{:20} {:.4f}'.format(name, distance))
