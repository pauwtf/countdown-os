from layout_engine import resolve_plane_position


TEST_VALUES = [
    0,
    0.25,
    0.5,
    0.75,
    1,
    -1,
    2,
    None
]


print("")
print("==============================================")
print("       COUNTDOWN OS — PROGRESS TEST")
print("==============================================")

print("")
print("PROGRESS → PLANE POSITION")
print("----------------------------------------------")

for progress in TEST_VALUES:

    result = resolve_plane_position(progress)

    print(
        f"Progress: {str(progress):<6}"
        f" | X Left: {result['x_left']}"
        f" | X Right: {result['x_right']}"
        f" | Y: {result['y']}"
    )


# ============================================================
# VALIDATION
# ============================================================

assert resolve_plane_position(0)["x_left"] == 0

assert resolve_plane_position(0.25)["x_left"] == 130

assert resolve_plane_position(0.5)["x_left"] == 260

assert resolve_plane_position(0.75)["x_left"] == 390

assert resolve_plane_position(1)["x_left"] == 520


# ============================================================
# BOUNDARY VALIDATION
# ============================================================

assert resolve_plane_position(-1)["x_left"] == 0

assert resolve_plane_position(2)["x_left"] == 520

assert resolve_plane_position(None)["x_left"] == 0


print("")
print("==============================================")
print("             🟢 TEST PASSED")
print("==============================================")
print("")