from media_player import MediaPlayer
from states import PlayState, StopState

if __name__ == '__main__':
    player = MediaPlayer()
    player.set_state(StopState(player))
    player.add_track('1')
    player.add_track('2')
    player.add_track('3')
    player.add_track('4')
    player.add_track('5')
    player.add_track('6')

    player.play()
    player.pause()
    player.play()
    player.prev()
    player.next()
    player.next()
    player.prev()
    player.stop()
    player.play()
    player.stop()
