import asyncio

from .room_syncer import main

if __name__ == "__main__":
    """
    Main function to be called with python3 -m chatroom_syncer
    """
    asyncio.run(main())
