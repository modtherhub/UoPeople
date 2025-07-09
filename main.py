def display_catalog():
    # Individual item prices
    item1 = 200.0
    item2 = 400.0
    item3 = 600.0

    # Display header
    print("Output:\n")
    print("Online Store")
    print("-" * 30)
    print("Product(S)\t\tPrice")

    # Display individual items (no discount)
    print(f"Item 1\t\t\t{item1}")
    print(f"Item 2\t\t\t{item2}")
    print(f"Item 3\t\t\t{item3}")

    # Calculate 10% discount for any two-item combo
    combo1 = (item1 + item2) * 0.9
    combo2 = (item2 + item3) * 0.9
    combo3 = (item1 + item3) * 0.9

    # Calculate 25% discount for all three items (gift pack)
    combo4 = (item1 + item2 + item3) * 0.75

    # Display combo packs
    print(f"Combo 1(Item 1 + 2)\t{combo1}")
    print(f"Combo 2(Item 2 + 3)\t{combo2}")
    print(f"Combo 3(Item 1 + 3)\t{combo3}")
    print(f"Combo 4(Item 1 + 2 + 3)\t{combo4}")
    
    print("_" * 30)
    print("For delivery Contact:98764678899")

# Call the function to display the catalog
display_catalog()
