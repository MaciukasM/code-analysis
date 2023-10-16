def view_room_info(client: Any):
    room_keys = get_all_rooms(client)
    room_key = inquirer.select(
        message = "Please select a room:",
        choices = room_keys
    ).execute()

    room_info = list(client.find(
        collection = ACCOMMODATION_COLLECTION,
        search_query = {"room_number": room_key}
    ))[0]
    room_type_info = list(client.find(
        collection = ACCOMMODATION_COLLECTION,
        search_query = {"type_id": room_info["type_id"]}
    ))[0]

    print(f"\nPrinting the info about the room {room_key}...")
    print(f"{'room type':<20}{room_type_info['type']}")
    print(f"{'number of beds':<20}{room_type_info['beds']}")
    print(f"{'number of tv':<20}{room_type_info['tv']}")
    print(f"{'has pool':<20}{bool(room_type_info['tv'])}")
    print(f"{'price of the night':<20}{room_info['price']}")
