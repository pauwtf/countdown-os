# --------------------------------------------------------
# COUNTER → KWGT POSITION
# --------------------------------------------------------

print()
print("KWGT POSITION VALIDATION")
print("-" * 50)

counter_kwgt = counter["kwgt_position"]

print(
    f"• Counter → X Right    "
    f"{counter_kwgt['x_right']}"
)

print(
    f"• Counter → X Left     "
    f"{counter_kwgt['x_left']}"
)

print(
    f"• Counter → Y Down     "
    f"{counter_kwgt['y_down']}"
)

print(
    f"• Counter → Y Up       "
    f"{counter_kwgt['y_up']}"
)

assert counter_kwgt["x_right"] == 195
assert counter_kwgt["x_left"] == 0

# Countdown OS -20 Y = KWGT 20 Y Down
assert counter_kwgt["y_down"] == 20
assert counter_kwgt["y_up"] == 0