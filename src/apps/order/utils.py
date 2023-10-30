from django.contrib.gis.geos import GEOSGeometry

def calculate_distance(restaurant_location, order_location):
    restaurant_point = GEOSGeometry(restaurant_location)  # Convert restaurant's location to a GEOSGeometry object
    order_point = GEOSGeometry(order_location)  # Convert order's location to a GEOSGeometry object

    # Calculate the distance between the two points
    distance = restaurant_point.distance(order_point)
    return distance.km 
