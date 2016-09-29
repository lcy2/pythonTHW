import sys
import random


class Scene(object):

    def enter(self):
        print "Please implement this scene."


class Engine(object):
    
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        print "You died. lol"
        sys.exit()

class CentralCorridor(Scene):

    def enter(self):
        print "you're in a corridor. You go straight."
        raw_input()

class LaserWeaponArmory(Scene):

    def enter(self):
        print "you picked up some weaps"
        raw_input()

class TheBridge(Scene):

    def enter(self):
        print "oh look it's a bridge"
        raw_input()

class EscapePod(Scene):

    def enter(self):
        print "you got the fuck out"
        sys.exit()


class Map(object):

    Scene currScene
    sceneList = ['central_corridor', 'bridge', 'pod', 'weapon']
    def __init__(self, start_scene):
        if (start_scene == 'central_corridor'):
            currScene = CentralCorridor()

    def next_scene(self, scene_name):
        currScene = scene_name

    def opening_scene(self):
        pass



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
