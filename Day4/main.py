# However, they do remember a few key facts about the password:
#
# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:
#
# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
from Day4.classes.Numbers import Numbers

start = 138241
end = 674034
print("Initial search space: " + str(end-start))

new_start = 138888  # numbers don't decrease
new_end = 669999  # numbers don't decrease
print("Search space: " + str(new_end-new_start))

limits = range(new_start, new_end + 1)  # range is exclusive of the last number
new_limits = []

for i in filter(Numbers.increasing, limits):
    new_limits.append(i)
print("Search space: " + str(len(new_limits)))

limits = []
for i in new_limits:
    if Numbers.duplicate_number(i):
        limits.append(i)
print("Search space: " + str(len(limits)))