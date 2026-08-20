from kwgt_coordinate_adapter import (
    adapt_directional_position,
    adapt_dual_x_position
)


print("=" * 50)
print("   COUNTDOWN OS — KWGT COORDINATE ADAPTER TEST")
print("=" * 50)


# ============================================================
# TEST 1 — COUNTER
# ============================================================

counter = adapt_directional_position(
    195,
    -20
)

print()
print("COUNTER")
print("-" * 50)

print(counter)

assert counter["x_right"] == 195
assert counter["x_left"] == 0
assert counter["y_down"] == 0
assert counter["y_up"] == 20


# ============================================================
# TEST 2 — HEARTS
# ============================================================

hearts = adapt_directional_position(
    -245,
    100
)

print()
print("HEARTS")
print("-" * 50)

print(hearts)

assert hearts["x_right"] == 0
assert hearts["x_left"] == 245
assert hearts["y_down"] == 100
assert hearts["y_up"] == 0


# ============================================================
# TEST 3 — ORIGIN
# ============================================================

origin = adapt_directional_position(
    275,
    100
)

print()
print("ORIGIN")
print("-" * 50)

print(origin)

assert origin["x_right"] == 275
assert origin["x_left"] == 0
assert origin["y_down"] == 100
assert origin["y_up"] == 0


# ============================================================
# TEST 4 — ZERO
# ============================================================

zero = adapt_directional_position(
    0,
    0
)

print()
print("ZERO")
print("-" * 50)

print(zero)

assert zero["x_right"] == 0
assert zero["x_left"] == 0
assert zero["y_down"] == 0
assert zero["y_up"] == 0


# ============================================================
# TEST 5 — PLANE
# ============================================================

plane = adapt_dual_x_position(
    349.1428571428571,
    275,
    93
)

print()
print("PLANE")
print("-" * 50)

print(plane)

assert plane["x_left"] == 349.1428571428571
assert plane["x_right"] == 275
assert plane["y"] == 93


# ============================================================
# RESULT
# ============================================================

print()
print("=" * 50)
print("             🟢 TEST PASSED")
print("=" * 50)