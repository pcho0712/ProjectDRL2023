from pybulletgym.envs.roboschool.envs.locomotion.walker_base_env import WalkerBaseBulletEnv
from pybulletgym.envs.roboschool.robots.locomotors import Walker2D


class Walker2DBulletEnv(WalkerBaseBulletEnv):
    def __init__(self):
        self.robot = Walker2D()
        WalkerBaseBulletEnv.__init__(self, self.robot)
        self.obstacle_pos_x = 0.0
        self.obstacle_size_x = 30.0
        self.obstacle_size_z = 0.6

    def collision_check(self)-> bool:
        if self.obstacle_pos_x < self.robot.body_xyz[0] < self.obstacle_pos_x+self.obstacle_size_x and self.robot.body_xyz[2] < self.obstacle_size_z:
            return True
        else:
            return False

