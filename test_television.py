import pytest
from television import Television  # Assuming your Television class is in a file named television.py

class TestTelevision:
    def setup_method(self):
        """Setup method to initialize the Television object."""
        self.tv = Television()

    def teardown_method(self):
        """Teardown method to clean up the Television object."""
        del self.tv

    def test_init(self):
        """Test the initialization of the Television class."""
        assert self.tv._Television__status == False
        assert self.tv._Television__muted == False
        assert self.tv._Television__channel == Television.MIN_CHANNEL
        assert self.tv._Television__volume == Television.MIN_VOLUME

    def test_power(self):
        """Test the power method."""
        self.tv.power()
        assert self.tv._Television__status == True
        self.tv.power()
        assert self.tv._Television__status == False

    def test_mute(self):
        """Test the mute method."""
        self.tv.power()  # Turn on the TV to enable muting
        self.tv.mute()
        assert self.tv._Television__muted == True
        self.tv.mute()
        assert self.tv._Television__muted == False

    def test_channel_up(self):
        """Test the channel_up method."""
        self.tv.power()  # Turn on the TV
        self.tv.channel_up()
        assert self.tv._Television__channel == Television.MIN_CHANNEL + 1

        # Wrap around to the first channel
        for _ in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL):
            self.tv.channel_up()
        assert self.tv._Television__channel == Television.MIN_CHANNEL

    def test_channel_down(self):
        """Test the channel_down method."""
        self.tv.power()  # Turn on the TV
        self.tv.channel_down()  # Wrap around to the last channel
        assert self.tv._Television__channel == Television.MAX_CHANNEL

        self.tv.channel_down()
        assert self.tv._Television__channel == Television.MAX_CHANNEL - 1

    def test_volume_up(self):
        """Test the volume_up method."""
        self.tv.power()  # Turn on the TV

        # Increment volume until the max
        for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME + 1):
            self.tv.volume_up()
        assert self.tv._Television__volume == Television.MAX_VOLUME

    def test_volume_down(self):
        """Test the volume_down method."""
        self.tv.power()  # Turn on the TV

        # Decrement volume until the min
        for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME + 1):
            self.tv.volume_down()
        assert self.tv._Television__volume == Television.MIN_VOLUME
