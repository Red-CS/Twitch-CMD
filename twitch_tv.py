import sys
import logging
import json
from helix import Helix
from usage import CommandUsage

def ttv():
    """Processes and executes command paramters"""

    # Set up logging
    logging.basicConfig(filename='log.log', level=logging.INFO)

    # Load request keys
    keys = json.load(open('./keys.json'))

    # Set up Helix api
    api = Helix(
        user_name = keys['username'],
        client_id = keys['client_id'],
        access_token = keys['access_token'])

    # Param info (temp)
    """
    Required Parameters:
        list - Lists active streamers ranked (aplhabetically? by num viewers?), then lists non active streamers
        open [name] - Opens streamer in browser, active or not
        follow - Follow a streamer
        check - check if a specific streamer is live
    """

    # Process params
    command_length = len(sys.argv)
    command_tag = str(sys.argv[1])
    if command_length < 2:
        print("No paramters given. Showing usage")
        sys.exit(1)
    
    elif command_tag == "list":
        if command_length > 2:
            print("Incorrect usage of list. Showing usage")
            sys.exit(1)
        else:
            print(api.get_streams())
            sys.exit(0)

    elif command_tag == "open":
        if command_length != 3:
            print("Incorrect usage of open. Showing usage")
            sys.exit(1)
        else:
            api.open_stream(str(sys.argv[2]))
            sys.exit(0)
    elif command_tag == "check":
        if command_length != 3:
            print("Incorrect usage of check. Showing usage")
            sys.exit(1)
        else:
            status = api.check_stream(str(sys.argv[2]))
            print(status)
            sys.exit(0)
    else:
        print("Parameter not recognized")
        sys.exit(1)


if __name__ == "__main__":
    ttv()