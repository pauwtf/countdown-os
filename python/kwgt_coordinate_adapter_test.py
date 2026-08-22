# ============================================================
# COUNTDOWN OS — KWGT COORDINATE ADAPTER TEST
# Version: 1.2 Elegance
# ============================================================

from kwgt_coordinate_adapter import (
    adapt_directional_position,
    adapt_dual_x_position,
)


print("=" * 50)
print("   COUNTDOWN OS — KWGT COORDINATE ADAPTER TEST")
print("=" * 50)


# ============================================================
# COORDINATE CONVENTION
# ============================================================
#
# COUNTDOWN OS:
#
#   +X = derecha
#   -X = izquierda
#   +Y = arriba
#   -Y = abajo
#
# KWGT:
#
#   x_right = derecha
#   x_left  = izquierda
#   y_up    = arriba
#   y_down  = abajo
#
# ============================================================


# ============================================================
# TEST 1 — COUNTER
# ============================================================

counter = adapt_directional_position(
    195,
    -20,
)

print()
print("COUNTER")
print("-" * 50)
print(counter)

assert counter["x_right"] == 195
assert counter["x_left"] == 0

# Countdown OS -20Y = KWGT 20Y Down
assert counter["y_down"] == 20
assert counter["y_up"] == 0


# ============================================================
# TEST 2 — HEARTS
# ============================================================

hearts = adapt_directional_position(
    -245,
    100,
)

print()
print("HEARTS")
print("-" * 50)
print(hearts)

# Countdown OS -245X = KWGT 245X Left
assert hearts["x_right"] == 0
assert hearts["x_left"] == 245

# Countdown OS +100Y = KWGT 100Y Up
assert hearts["y_down"] == 0
assert hearts["y_up"] == 100


# ============================================================
# TEST 3 — ORIGIN
# ============================================================

origin = adapt_directional_position(
    275,
    100,
)

print()
print("ORIGIN")
print("-" * 50)
print(origin)

assert origin["x_right"] == 275
assert origin["x_left"] == 0

# Countdown OS +100Y = KWGT 100Y Up
assert origin["y_down"] == 0
assert origin["y_up"] == 100


# ============================================================
# TEST 4 — ZERO
# ============================================================

zero = adapt_directional_position(
    0,
    0,
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
# TEST 5 — POSITIVE Y
# ============================================================

positive_y = adapt_directional_position(
    0,
    50,
)

print()
print("POSITIVE Y")
print("-" * 50)
print(positive_y)

# +Y = arriba
assert positive_y["x_right"] == 0
assert positive_y["x_left"] == 0
assert positive_y["y_down"] == 0
assert positive_y["y_up"] == 50


# ============================================================
# TEST 6 — NEGATIVE Y
# ============================================================

negative_y = adapt_directional_position(
    0,
    -50,
)

print()
print("NEGATIVE Y")
print("-" * 50)
print(negative_y)

# -Y = abajo
assert negative_y["x_right"] == 0
assert negative_y["x_left"] == 0
assert negative_y["y_down"] == 50
assert negative_y["y_up"] == 0


# ============================================================
# TEST 7 — PLANE
# ============================================================

plane = adapt_dual_x_position(
    349.1428571428571,
    275,
    93,
)

print()
print("PLANE")
print("-" * 50)
print(plane)

assert plane["x_left"] == 349.1428571428571
assert plane["x_right"] == 275
assert plane["y"] == 93


# ============================================================
# TEST 8 — PLANE ZERO VALIDATION
# ============================================================

plane_zero = adapt_dual_x_position(
    0,
    0,
    0,
)

print()
print("PLANE ZERO")
print("-" * 50)
print(plane_zero)

assert plane_zero["x_left"] == 0
assert plane_zero["x_right"] == 0
assert plane_zero["y"] == 0


# ============================================================
# RESULT
# ============================================================

print()
print("=" * 50)
print("             🟢 TEST PASSED")
print("=" * 50)