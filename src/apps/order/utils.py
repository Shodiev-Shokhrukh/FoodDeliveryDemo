def calculate_delivery_time(order_data):
    food_items_count = len(order_data.get('items', []))
    # Calculate the total preparation time for the food items
    preparation_time = (food_items_count // 4) * 5  # 4 items prepared every 5 minutes
    if food_items_count % 4 != 0:
        preparation_time += 5  # Additional 5 minutes for the remaining items

    # Calculate the delivery distance in kilometers (considering it's in the order_data)
    delivery_distance = order_data.get('distance', 0)

    # Calculate the total delivery time based on preparation time and distance
    total_delivery_time = preparation_time + (delivery_distance * 3)  # 3 minutes per kilometer

    return total_delivery_time
