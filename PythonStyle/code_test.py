from collections import Sequence, Iterable

tracebacks = {}
key_type = "filename"
frame = ("a.txt", "30")


class Traceback():
    def __init__(self, frames):
        # frames is a tuple of frame tuples: see Frame constructor for the
        # format of a frame tuple
        self._frames = frames
try:
    traceback = tracebacks[frame]
    print(traceback)
except:
    if key_type == 'lineno':
        frames = (frame,)
    else:  # key_type == 'filename':
        print("--filename--")
        frames = ((frame[0], 0),)
        print(frames)

    traceback = Traceback(frames)
    print(traceback)
    tracebacks[frame] = traceback

    print(tracebacks)
    # {('a.txt', '10'): <__main__.Traceback object at 0x10fabd828>}



