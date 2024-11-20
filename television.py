class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        '''
        Inititalizes variables
        '''
        self.__status: bool = False
        self.__muted: bool = False
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME

    def power(self) -> None:
        '''
        switches between on and off
        :return:
        '''
        self.__status = not self.__status

    def mute(self) -> None:
        '''
        Mutes Tv
        :return:
        '''
        if self.__status == True:
            self.__muted = not self.__muted


    def channel_up(self) -> None:
        '''
        Change the channel up
        :return:
        '''
        if self.__status == True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel +=1

    def channel_down(self) -> None:
        '''
        change the channel down
        :return:
        '''
        if self.__status == True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -=1

    def volume_up(self) -> None:
        '''
        increase the volume
        :return:
        '''
        if self.__status == True:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                 self.__volume += 1

    def volume_down(self) -> None:
        '''
        decrease the volume
        :return:
        '''
        if self.__status == True:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1


    def __str__  (self):
        """
        Method to return TV status
        :return: tv status
        """""
        if self.__muted:
            return f"Power = {self.__status},Channel = {self.__channel},Volume = {0}"
        else:
            return f"Power = {self.__status},Channel = {self.__channel},Volume = {self.__volume}"
