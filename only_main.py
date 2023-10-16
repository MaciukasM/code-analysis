def main():
    # initialising DB
    hotel_db = HotelMongoDBClient(CONNECTION_STRING, DB_NAME)
    hotel_db.drop_db()

    db_backfill_conf = {
        ACCOMMODATION_COLLECTION: "src/data/accommodations_data.json",
        GUEST_COLLECTION: "src/data/guest_data.json"
    }

    hotel_db.seed_db(db_backfill_conf)

    # main program loop
    print("\nWelcome to the Fishing Resort Hotel management console!")
    while True:
        action = inquirer.select(
            message = "Select an action:",
            choices = [
                Choice(value = 0, name = "Get all the currently occupied rooms"),
                Choice(value = 1, name = "Get all the currently available rooms"),
                Choice(value = 2, name = "Get the total price of all occupied rooms (Aggregation Pipeline)"),
                Choice(value = 3, name = "Get the total price of all occupied rooms (MapReduce)"),
                Choice(value = 4, name = "View room info"),
                Choice(value = 5, name = "View guest info"),
            ]
        ).execute()


        if action == 0:
            occupied_rooms = get_occupied_rooms(hotel_db)
            if occupied_rooms:
                print("These are the currently occupied rooms:", occupied_rooms)
            else:
                print("There are no currently occupied rooms!")
        if action == 1:
            unoccupied_rooms = get_available_rooms(hotel_db)
            if unoccupied_rooms:
                print("These are the currently free rooms: ", unoccupied_rooms)
            else:
                print("There are no currently free rooms!")

        if action == 2:
            total_booking_price = get_total_booked_room_price_with_aggregate_pipeline(hotel_db)
            print("The currently occupied total price is:", total_booking_price)

        if action == 3:
            total_booking_price = get_total_booked_room_price_with_map_reduce(hotel_db)
            print("The currently occupied total price is:", total_booking_price)

        if action == 4:
            view_room_info(hotel_db)

        if action == 5:
            view_guest_info(hotel_db)

        print("\n" + "-"*40)
        proceed = inquirer.confirm(
            message="Would you like to query something else?",
        ).execute()
        if not proceed:
            break
        os.system('clear')
