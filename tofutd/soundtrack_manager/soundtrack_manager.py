""" Contains the SoundtrackManager class, the class responsible for playing soundtracks. """

# Package imports.
import threading
import time

# TTD imports.


# Classes.
class SoundtrackManager:
    """ Manages soundtrack playing. Allows for the soundtrack to be managed by a thread separate from the main Python
    process, which will allow for smoother transition between soundtracks. """

    # Convert SoundtrackManager into a Singleton.
    __instance = None

    def __init__(self):
        """ Constructor. """
        self._stop_flag = threading.Event()

    def __new__(cls):
        """ Create a new instance of the soundtrack manager if none exist. Otherwise, return the existing instance of
        SoundtrackManager. """

        if cls.__instance is None:
            cls.__instance = super(SoundtrackManager, cls).__new__(cls)
        return cls.__instance

    @classmethod
    def get_instance(cls):
        """ Get the SoundtrackManager instance.

        Returns:
            (SoundtrackManager | None): The instance of SoundtrackManager or None.
        """
        return cls.__instance

    def start(self):
        """ Starts the SoundtrackManager. """

        # Unless the stop flag is set, continue to play soundtracks.
        while not self._stop_flag.is_set():
            pass


    def stop(self):
        """ Stops the SoundtrackManager. """
        self._stop_flag.set()
