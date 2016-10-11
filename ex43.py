import sys
import random

class Scene(object):

    def enter(self, status):
        print "Please implement this scene."


class Map(object):


    sceneList = ['central_corridor', 'bridge', 'pod', 'weapon']
    
    def __init__(self, start_scene):
        self.currScene = None
        self.status = {'laser':False, 'bomb':False, 'dead':False, 'exploded':False}
        if (start_scene == 'central_corridor'):
            self.currScene = CentralCorridor()
        elif (start_scene == 'bridge'):
            self.currScene = TheBridge()
        elif (start_scene == 'pod'):
            self.currScene = EscapePod()
        elif (start_scene == 'weapon'):
            self.currScene = LaserWeaponArmory()
        elif (start_scene == 'dead'):
            self.currScene = Death();
            
        
    def next_scene(self, scene_name):
        if (scene_name == 'central_corridor'):
            self.currScene = CentralCorridor()
        elif (scene_name == 'bridge'):
            self.currScene = TheBridge()
        elif (scene_name == 'pod'):
            self.currScene = EscapePod()
        elif (scene_name == 'weapon'):
            self.currScene = LaserWeaponArmory()
        elif (scene_name == 'dead'):
            self.currScene = Death();
    
        #self.currScene = scene_name

    def opening_scene(self):
        #print "hi status here", self.status
        self.status = self.currScene.enter(self.status)
        if (self.status['dead']):
            self.next_scene('dead')
        else:
            self.next_scene(Map.sceneList[random.randint(0,len(Map.sceneList)-1)])
        return self.opening_scene()
            







class Engine(object):
    
    
    def __init__(self, scene_map):
        self.map = scene_map

    def play(self):
        self.map.opening_scene()

class Death(Scene):

    def enter(self, status):
        print "You died. lol"
        sys.exit()

class CentralCorridor(Scene):

    def enter(self, status):
        print "you're in a corridor. There's a monster. Fight!"
        raw_input()
        
        if ((random.randint(0,10) + 4 * int(status['laser'] == True)) > 2):
            print "You killed the monster!"
            raw_input()
            return status
        else:
            status['dead'] = True
            return status

class LaserWeaponArmory(Scene):

    def enter(self, status):
        print "you picked up some weaps"
        raw_input()
        if (status['laser']):
            status['bomb'] = True
            print "you picked up the bomb"
        else:
            status['laser'] = True
            print "you picked up the laser"
        raw_input()
        return status
        

class TheBridge(Scene):

    def enter(self, status):
        print "oh look it's a bridge. There's a monster."
        raw_input()
        if ((random.randint(0,10) + 4 * int(status['laser'] == True)) > 5):
            print "You killed the monster!"
            if (status['bomb']):
                status['exploded'] = True
                print "You set us up the bomb!"
            else:
                print "you don't have the bomb yet though"
            raw_input()
        else:
            status['dead'] = True
        return status

class EscapePod(Scene):

    def enter(self, status):
        print "it's the escape pod!"
        if (status['exploded']):
            print "you got the fuck out"
            sys.exit()
        else:
            
            print "Can't leave yet."
            return status




a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
