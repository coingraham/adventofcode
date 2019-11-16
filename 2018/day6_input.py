test_coordinates = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

real_coordinates = """77, 279
216, 187
72, 301
183, 82
57, 170
46, 335
55, 89
71, 114
313, 358
82, 88
78, 136
339, 314
156, 281
260, 288
125, 249
150, 130
210, 271
190, 258
73, 287
187, 332
283, 353
66, 158
108, 97
237, 278
243, 160
61, 52
353, 107
260, 184
234, 321
181, 270
104, 84
290, 109
193, 342
43, 294
134, 211
50, 129
92, 112
309, 130
291, 170
89, 204
186, 177
286, 302
188, 145
40, 52
254, 292
270, 287
238, 216
299, 184
141, 264
117, 129"""

coords_dictionary = {}
coords_splitlines = real_coordinates.splitlines()
max_x = 0
max_y = 0
# part one
# adjustment = 300
# max_plane = 900

# part two
adjustment = 0
max_plane = 400
for item in coords_splitlines:
    coords = item.split(", ")
    x = int(coords[0]) + adjustment
    y = int(coords[1]) + adjustment
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    coords_dictionary["{}_{}".format(x, y)] = [x, y]

print(coords_dictionary)

