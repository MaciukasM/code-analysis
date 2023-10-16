def get_occupied_rooms(client: Any):
    cursor = client.find(
        collection = GUEST_COLLECTION,
        search_query = {},
        projection_query = {"keys": {"room_number": 1}}
    )

    occupied_rooms = []
    for doc in cursor:
        for key in doc["keys"]:
            occupied_rooms.append(key["room_number"])

    return occupied_rooms