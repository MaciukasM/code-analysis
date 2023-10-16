def view_guest_info(client: Any):
    guests = get_all_guests(client)

    guest_choices = [
        Choice(value = index, name = f"{name[0]} {name[1]}") for index, name in enumerate(guests)
    ]
    guest_index = inquirer.select(
        message = "Please select a guest:",
        choices = guest_choices
    ).execute()

    guest_info = list(client.find(
        collection = GUEST_COLLECTION,
        search_query = {"name": guests[guest_index][0], "surname": guests[guest_index][1]}
    ))[0]

    print(f"\nPrinting the info about the guest {guest_info['name']}...")
    print(f"{'name':<20}{guest_info['name']}")
    print(f"{'surname':<20}{guest_info['surname']}")
    print(f"{'phone number':<20}{guest_info['contacts']['phone']}")
    print(f"{'email addresss':<20}{guest_info['contacts']['email']}")
    print(f"{'occupied rooms':<20}{[key['room_number'] for key in guest_info['keys']]}")
