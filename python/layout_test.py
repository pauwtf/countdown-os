from layout_engine import build_layout


event = {
    "titleDisplay": "UNTIL ALEX",
    "daysDisplay": "48",
    "progressDisplay": "66%",
    "notesDisplay": "Comprar cacao",
    "progress": 0.6571428571428571
}


layout = build_layout(event)


print(layout)