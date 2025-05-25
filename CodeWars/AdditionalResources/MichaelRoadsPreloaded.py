import threading
from queue import Queue


class OverusedSnifferException(Exception):
    pass


class Protocol:
    # yes yes enum exists shush
    sniff_left = "sniff left"
    sniff_right = "sniff right"
    traverse_left = "traverse left"
    traverse_right = "traverse right"
    shutdown = "shutdown"
    overused = "overused sniffer"


class Road:
    def __init__(self, path):
        # private fields don't exist in python, I'm holding the secret state in a
        # thread, erlang style.
        # if that is too overengineered then the next candidate is a closure, or
        # otherwise somewhere nobody would think to look, such as an attribute on
        # some function, why not.
        # but anyway, thread felt like the fun solution.
        #
        # by fun I mean potentially a debugging nightmare for someone :^)
        self._write, self._read = Queue(), Queue()
        threading.Thread(
            target=secret_thread,
            args=[self._write, self._read],
            daemon=True,
        ).start()
        # not passing path as an arg because then it's available on the threading
        # object as an attribute. instead sending it as the first message
        self._write.put(path)

    def _commune(self, msg):
        self._write.put(msg)
        response = self._read.get()
        if response == Protocol.overused:
            raise OverusedSnifferException("Put that snout away, nose boy")
        return response

    def sniff_left(self):
        return self._commune(Protocol.sniff_left)

    def sniff_right(self):
        return self._commune(Protocol.sniff_right)

    def traverse_left(self):
        return self._commune(Protocol.traverse_left)

    def traverse_right(self):
        return self._commune(Protocol.traverse_right)

    def __del__(self):
        # ask the thread to quit
        # not really necessary, doesn't matter if a couple idle threads sit
        # around
        self._write.put(Protocol.shutdown)


def secret_thread(read: Queue, write: Queue):
    path = read.get()
    sniffed = False

    def mksniff(me):
        def sniff():
            nonlocal sniffed
            if sniffed:
                return Protocol.overused
            sniffed = True
            match path:
                case "":
                    return "Pleasant air."
                case s if len(s) == 1 and s[0] == me:
                    return "Michael!"
                case s if len(s) == 1 and s[0] != me:
                    return "I smell Michael on the other road!"
                case s if s[0] == me:
                    return "This one reeks."
                case s if s[0] != me:
                    return "Pleasant air."
                case _:
                    raise ValueError(f"failed to match {path=!r}")

        return sniff

    def mktraverse(me):
        def traverse():
            nonlocal sniffed, path
            sniffed = False
            if path[:1] != me:
                path = ""
            path = path[1:]

        return traverse

    actions = {
        Protocol.sniff_left: mksniff("L"),
        Protocol.sniff_right: mksniff("R"),
        Protocol.traverse_left: mktraverse("L"),
        Protocol.traverse_right: mktraverse("R"),
    }

    while True:
        request = read.get()
        if request == Protocol.shutdown:
            break
        action = actions[request]
        response = action()
        write.put(response)


__all__ = ["Road", "OverusedSnifferException"]