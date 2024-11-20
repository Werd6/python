import pytest
from television import Television  # Assuming your Television class is in a file named television.py

def test_init():
    """Test the initialization of the Television class."""
    tv = Television()
    assert tv._Television__status == False
    assert tv._Television__muted == False
    assert tv._Television__channel == Television.MIN_CHANNEL
    assert tv._Television__volume == Television.MIN_VOLUME

def test_power():
    """Test the power method."""
    tv = Television()
    tv.power()
    assert tv._Television__status == True
    tv.power()
    assert tv._Television__status == False

def test_mute():
    """Test the mute method."""
    tv = Television()
    tv.power()  # Turn on the TV to enable muting
    tv.mute()
    assert tv._Television__muted == True
    tv.mute()
    assert tv._Television__muted == False

def test_channel_up():
    """Test the channel_up method."""
    tv = Television()
    tv.power()  # Turn on the TV
    tv.channel_up()
    assert tv._Television__channel == 1
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  # Should wrap around to the first channel
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_channel_down():
    """Test the channel_down method."""
    tv = Television()
    tv.power()  # Turn on the TV
    tv.channel_down()  # Should wrap around to the last channel
    assert tv._Television__channel == Television.MAX_CHANNEL
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL - 1

def test_volume_up():
    """Test the volume_up method."""
    tv = Television()
    tv.power()  # Turn on the TV
    tv.volume_up()
    assert tv._Television__volume == Television.MIN_VOLUME + 1
    tv.volume_up()
    tv.volume_up()  # Should stop at MAX_VOLUME
    assert tv._Television__volume == Television.MAX_VOLUME

def test_volume_down():
    """Test the volume_down method."""
    tv = Television()
    tv.power()  # Turn on the TV
    tv.volume_down()  # Should not go below MIN_VOLUME
    assert tv._Television__volume == Television.MIN_VOLUME
    tv._Television__volume = Television.MAX_VOLUME  # Set volume to max for testing
    tv.volume_down()
    assert tv._Television__volume == Television.MAX_VOLUME - 1
