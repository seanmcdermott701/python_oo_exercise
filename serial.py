"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=1):
        self.start = start
        self.current_serial = start
    
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start + 1}"
    
    def generate(self):
        t = self.current_serial
        self.current_serial += 1
        return t

    def reset(self):
        self.current_serial = self.start
    