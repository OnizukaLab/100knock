import collections

with open("hightemp.txt", "r") as f:
    print("\n".join(x[0] for x in sorted(collections.Counter([r.split()[0] for r in f]).items(), key=lambda x:-x[1])))