# ============================================================
# COUNTDOWN OS — COMPONENT SYSTEM TEST
# Version: 1.2 Elegance
# ============================================================

from component import Component


# ============================================================
# HEADER
# ============================================================

print("=" * 50)
print("       COUNTDOWN OS — COMPONENT SYSTEM TEST")
print("=" * 50)


# ============================================================
# TEST 1 — BASIC COMPONENT
# ============================================================

component = Component(
    "TestComponent",
    "container",
    position={
        "x": 100,
        "y": 50,
    },
)

print()
print("BASIC COMPONENT")
print("-" * 50)
print(component)

assert component.id == "TestComponent"
assert component.type == "container"
assert component.position["x"] == 100
assert component.position["y"] == 50
assert component.children == []


# ============================================================
# TEST 2 — SIZE
# ============================================================

component.set_size(
    200,
    100,
)

print()
print("SIZE")
print("-" * 50)
print(component.size)

assert component.size["width"] == 200
assert component.size["height"] == 100


# ============================================================
# TEST 3 — PROPERTIES
# ============================================================

component.set_property(
    "opacity",
    0.5,
)

component.set_property(
    "visible",
    True,
)

print()
print("PROPERTIES")
print("-" * 50)
print(component.properties)

assert component.get_property(
    "opacity"
) == 0.5

assert component.get_property(
    "visible"
) is True

assert component.get_property(
    "missing",
    "default",
) == "default"


# ============================================================
# TEST 4 — POSITION
# ============================================================

component.set_position(
    -25,
    -40,
)

print()
print("POSITION")
print("-" * 50)
print(component.position)

assert component.position["x"] == -25
assert component.position["y"] == -40


# ============================================================
# TEST 5 — CHILD COMPONENT
# ============================================================

parent = Component(
    "Header",
    "container",
)

title = Component(
    "Title",
    "text",
)

parent.add_child(title)

print()
print("CHILDREN")
print("-" * 50)
print(parent.children)

assert len(parent.children) == 1
assert parent.children[0] is title
assert parent.children[0].id == "Title"


# ============================================================
# TEST 6 — MULTIPLE CHILDREN
# ============================================================

days = Component(
    "Days",
    "text",
)

parent.add_child(days)

print()
print("MULTIPLE CHILDREN")
print("-" * 50)

for child in parent.children:
    print(f"✓ {child.id}")

assert len(parent.children) == 2
assert parent.children[0].id == "Title"
assert parent.children[1].id == "Days"


# ============================================================
# TEST 7 — NESTED COMPONENTS
# ============================================================

countdown = Component(
    "Countdown",
    "container",
)

header = Component(
    "Header",
    "container",
)

counter = Component(
    "Counter",
    "container",
)

countdown.add_child(header)
countdown.add_child(counter)

header.add_child(title)
header.add_child(days)

print()
print("NESTED COMPONENTS")
print("-" * 50)

print(f"✓ {countdown.id}")

for child in countdown.children:

    print(f"  └── {child.id}")

    for nested in child.children:
        print(f"      └── {nested.id}")


assert len(countdown.children) == 2
assert countdown.children[0].id == "Header"
assert countdown.children[1].id == "Counter"

assert len(header.children) == 2
assert header.children[0].id == "Title"
assert header.children[1].id == "Days"


# ============================================================
# TEST 8 — SERIALIZATION
# ============================================================

serialized = countdown.to_dict()

print()
print("SERIALIZATION")
print("-" * 50)
print(serialized)

assert serialized["id"] == "Countdown"
assert serialized["type"] == "container"

assert "position" in serialized
assert "children" in serialized

assert len(serialized["children"]) == 2

serialized_header = serialized["children"][0]

assert serialized_header["id"] == "Header"
assert serialized_header["type"] == "container"

assert len(
    serialized_header["children"]
) == 2

assert (
    serialized_header["children"][0]["id"]
    == "Title"
)

assert (
    serialized_header["children"][1]["id"]
    == "Days"
)


# ============================================================
# TEST 9 — TYPE VALIDATION
# ============================================================

print()
print("TYPE VALIDATION")
print("-" * 50)

try:

    parent.add_child("invalid")

    raise AssertionError(
        "Component accepted an invalid child"
    )

except TypeError:

    print("✓ Invalid child rejected")


# ============================================================
# TEST 10 — REMOVE CHILD
# ============================================================

parent.remove_child(days)

print()
print("REMOVE CHILD")
print("-" * 50)

print(
    f"Remaining children: "
    f"{len(parent.children)}"
)

assert len(parent.children) == 1
assert parent.children[0].id == "Title"


# ============================================================
# SUCCESS
# ============================================================

print()
print("=" * 50)
print("             🟢 TEST PASSED")
print("=" * 50)
print()