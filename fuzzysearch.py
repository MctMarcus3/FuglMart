l = [
    {
        "upc": "123456789012",
        "name": "Soda Chips",
        "category": "Snacks",
        "price": "12.12",
        "stock": "12",
    },
    {
        "upc": "123456789112",
        "name": "Xmas Gifts",
        "category": "Instant",
        "price": "34.20",
        "stock": "122",
    },
    {
        "upc": "123456782012",
        "name": "Pondering Stars",
        "category": "Drinks",
        "price": "31.12",
        "stock": "112",
    },
    {
        "upc": "123453789012",
        "name": "Rice",
        "category": "Staple",
        "price": "43.42",
        "stock": "120",
    }
]

print([d for d in l if any("ip" in v for v in d.values())])
