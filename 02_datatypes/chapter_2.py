spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {(spice_mix)}")
spice_mix.add("ginger")
spice_mix.add("cardamom")
print(f"After spice mix id: {(spice_mix)}")
print(f"After spice mix id: {id(spice_mix)}")

# refer chapter_1.py number -> mutable, sets -> immutable