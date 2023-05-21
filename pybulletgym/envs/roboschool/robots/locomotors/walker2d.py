from pybulletgym.envs.roboschool.robots.locomotors.walker_base import WalkerBase
from pybulletgym.envs.roboschool.robots.robot_bases import MJCFBasedRobot
import numpy as np


class Walker2D(WalkerBase, MJCFBasedRobot):
    foot_list = ["foot", "foot_left"]

    def __init__(self):
        WalkerBase.__init__(self, power=0.40)
        MJCFBasedRobot.__init__(self, "walker2d.xml", "torso", action_dim=6, obs_dim=22)
        self.foot_force = [0]*len(self.foot_list)
        self.foot_3d_orien = [np.array([0,0,0,1])]*len(self.foot_list)
        self.foot_2d_orien = [np.array([1,0])]*len(self.foot_list)

    def alive_bonus(self, z, pitch):
        return +1 if z > 0.8 and abs(pitch) < 1.0 else -1

    def robot_specific_reset(self, bullet_client):
        WalkerBase.robot_specific_reset(self, bullet_client)
        for n in ["foot_joint", "foot_left_joint"]:
            self.jdict[n].power_coef = 30.0

