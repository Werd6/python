class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME

    def power(self) -> None:
        self.__status = not self.__status

    def mute(self) -> None:
        if self.__status == True:
            self.__muted = not self.__muted


    def channel_up(self) -> None:
        if self.__status == True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel +=1

    def channel_down(self) -> None:
        if self.__status == True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -=1

    def volume_up(self) -> None:
        if self.__status == True:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                 self.__volume += 1

    def volume_down(self) -> None:
        if self.__status == True:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1


    def __str__  (self):
        """
        Mathod to return TV status
        :return: tv status
        """""
        if self.__muted:
            return f"Power = {self.__status},Channel = {self.__channel},Volume = {0}"
        else:
            return f"Power = {self.__status},Channel = {self.__channel},Volume = {self.__volume}"
