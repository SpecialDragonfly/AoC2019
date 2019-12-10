from collections import Counter

from Day8.Util import Util

util = Util()
values = util.parse('input.txt')
width = 25
height = 6

layers = []
start = 0
total = width * height
while True:
    number_slice = values[start: start + total]
    if len(number_slice) == 0:
        break
    layers.append(number_slice)
    start += total

layer_index = -1
zero_count = 999999999999999
for layer in range(0, len(layers)):
    counter = Counter(layers[layer])
    if counter[0] < zero_count:
        layer_index = layer
        zero_count = counter[0]
counter = Counter(layers[layer_index])
print("Layer ", layer_index, "has the fewest zeros: (", zero_count, ") and the answer is ", counter[1] * counter[2])

final = layers[0].copy()
# Loop through the current digits
for digit_idx in range(0, total):
    # if any of the digits are transparent
    if final[digit_idx] == 2:
        # look through the layers for the first one that isn't transparent
        for layer_idx in range(1, len(layers)):
            if layers[layer_idx][digit_idx] != 2:
                final[digit_idx] = layers[layer_idx][digit_idx]
                break

idx = 0
while idx <= total:
    print(final[idx: idx + width])
    idx += width