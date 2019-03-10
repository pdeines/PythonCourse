imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psyhco"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

print(imelda[0])
print(imelda[1])
print(imelda[2])
tracks = imelda[3]
for track in tracks:
    print("\t{} {}".format(track[0], track[1]))
