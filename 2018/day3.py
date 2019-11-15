import day3_input_file

# max_width = 0
# max_height = 0

# for size in day3_input_file.sizes:
#     width = int(size.split("x")[0])
#     height = int(size.split("x")[1])
#
#     if width > max_width:
#         max_width = width
#
#     if height > max_height:
#         max_height = height
#
# print("Maximum Width {} and Height {}".format(max_width, max_height))
#
# max_width = 0
# max_height = 0
#
# for position in day3_input_file.positions:
#     width = int(position.split(",")[0])
#     height = int(position.split(",")[1])
#
#     if width > max_width:
#         max_width = width
#
#     if height > max_height:
#         max_height = height
#
# print("Maximum Position Width {} and Height {}".format(max_width, max_height))

square_inches = {}

for item in range(len(day3_input_file.sizes)):

    width = int(day3_input_file.sizes[item].split("x")[0])
    height = int(day3_input_file.sizes[item].split("x")[1])

    side = int(day3_input_file.positions[item].split(",")[0])
    top = int(day3_input_file.positions[item].split(",")[1])

    for i in range(side, side + width):
        for j in range(top, top + height):
            inch = "{}_{}".format(i, j)
            if inch in square_inches:
                square_inches[inch] += 1
            else:
                square_inches[inch] = 1

filtered_square_inches = {k: v for k, v in square_inches.items() if v > 1}
print("Overlaps: {}".format(len(filtered_square_inches)))

# for item in range(len(day3_input_file.sizes)):
#
#     width = int(day3_input_file.sizes[item].split("x")[0])
#     height = int(day3_input_file.sizes[item].split("x")[1])
#
#     side = int(day3_input_file.positions[item].split(",")[0])
#     top = int(day3_input_file.positions[item].split(",")[1])
#
#     for i in range(side, side + width):
#         for j in range(top, top + height):
#             inch = "{}_{}".format(i, j)
#             if inch in square_inches:
#                 square_inches[inch] = 0
#             else:
#                 square_inches[inch] = day3_input_file.ids[item]
#
# for item in range(len(day3_input_file.ids)):
#     width = int(day3_input_file.sizes[item].split("x")[0])
#     height = int(day3_input_file.sizes[item].split("x")[1])
#     fabric_size = width * height
#     id = day3_input_file.ids[item]
#
#     total_id = sum(1 for x in square_inches.values() if x == id)
#     if fabric_size == total_id:
#         print("The special id: {}".format(id))
