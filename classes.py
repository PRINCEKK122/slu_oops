class Television:
    def __init__(self):
        self._powerOn = False
        self._muted = False
        self._volume = 5
        self._channel = 2
        self._prevChan = 2

    def togglePower(self):
        self._powerOne = not self._powerOn

    def isOn(self):
        return self._powerOn

    def toggleMute(self):
        if self._powerOn:
            self._muted = not self._muted

    def isMuted(self):
        return self._muted

    def getVolume(self):
        return self._volume

    def getChannel(self):
        return self._channel

    def __str__(self):
        display = "Current power setting " + str(self._powerOn) + "\n"
        display += "Current channel setting " + str(self._channel) + "\n"
        display += "Current volume setting " + str(self._volume) + "\n"
        display += "Current mute setting " + str(self._muted)
        return display

    def volumeUp(self):
        if self._powerOn:
            if self._volume < 10:
                self._volume += 1
            self._muted = False
            return self._volume

    def volumeDown(self):
        if self._powerOn:
            self._volume -= 1
        self._muted = False
        return self._volume

    def setChannel(self, number):
        if self._powerOn:
            if 2 <= number <= 99:
                self._prevChan = self._channel
                self._channel = number
            return self._channel

    def channelUp(self):
        if self._powerOn:
            self._prevChan = self._channel
            if self._channel == 99:
                self._channel = 2
            else:
                self._channel += 1
            return self._channel

    def channelDown(self):
        if self._powerOn:
            self._prevChan = self._channel
            if self._channel == 2:
                self._channel = 99
            else:
                self._channel -= 1
            return self._channel

    def jumpPrevChannel(self):
        if self._powerOn:
            incoming = self._channel
            self._channel = self._prevChan
            self._prevChan = incoming
            return self._channel


class DeluxeTV(Television):
    def __init__(self):
        super().__init__()
        self._favorites = []

    def addToFavorites(self):
        if self._powerOn and self._channel not in self._favorites:
            self._favorites.append(self._channel)

    def removeFromFavorites(self):
        if self._powerOn and self._channel in self._favorites:
            self._favorites.remove(self._channel)

    def jumpToFavorites(self):
        if self._powerOn and len(self._favorites) > 0:
            closet = max(self._favorites)
            if closet <= self._channel:
                closet = min(self._favorites)
            else:
                for option in self._favorites:
                    if self._channel < option < closet:
                        closet = option
            self.setChannel(closet)
            return closet


class SortedSet(list):
    def __init__(self, initialList=None):
        super().__init__()
        if initialList:
            self.extend(initialList)

    def indexAfter(self, value):
        i = 0
        while i < len(self) and value >= self[i]:
            i += 1
        return i

    def insert(self, value):
        if value not in self:
            place = self.indexAfter(value)
            super().insert(place, value)

    def append(self, value):
        self.insert(value)

    def extend(self, otherList):
        for element in otherList:
            self.insert(element)

    def __add__(self, otherList):
        list3 = SortedSet(self)
        list3.extend(otherList)
        return list3

    def sort(self):
        pass

    def reverse(self):
        raise RuntimeError("SortedSet can't be reversed")

    def __setitem__(self, index, value):
        raise RuntimeError("This syntax is not suppported for the SortedSet class")


custom_list = SortedSet([*range(15, 20)])
from random import randint

for _ in range(10):
    randVal = randint(1, 16)
    custom_list.append(randVal)
    print(randVal)

print(custom_list)
