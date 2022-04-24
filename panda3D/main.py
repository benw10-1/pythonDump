from math import pi, sin, cos, radians
import numpy as np
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.bullet import BulletWorld
from panda3d.core import Vec3, VBase4, LineSegs, NodePath, AntialiasAttrib, Point3, AmbientLight, BitMask32
from panda3d.core import CollisionBox, CollisionNode, CollisionRay, GeomNode, CollisionTraverser, CollisionHandlerQueue

x_axis = Vec3(1, 0, 0)
y_axis = Vec3(0, 1, 0)
z_axis = Vec3(0, 0, 1)


def getVecMagnitude(vec):
    return (vec[0]**2 + vec[1]**2 + vec[2]**2)**.5


def toOtherSpace(vec):
    if type(vec) == Vec3:
        return Vec3(-vec.y, vec.x, vec.z)
    return Vec3(-vec[1], vec[0], vec[2])


def toThisSpace(vec):
    if type(vec) == Vec3:
        return Vec3(vec.y, -vec.x, vec.z)
    return Vec3(vec[1], -vec[0], vec[2])


def getRotatePoint3D(point, axis_vector, angle, origin=[0, 0, 0], degrees=True):
    if degrees:
        angle = radians(angle)
    x = point[0]
    y = point[1]
    z = point[2]
    a = origin[0]
    b = origin[1]
    c = origin[2]
    u = axis_vector[0]
    v = axis_vector[1]
    w = axis_vector[2]
    bv = b*v
    cw = c*w
    ux = u*x
    vy = v*y
    wz = w*z
    au = a*u
    cv = c*v
    bw = b*w
    wy = w*y
    vz = v*z
    cu = c*u
    aw = a*w
    wx = w*x
    uz = u*z
    bu = b*u
    av = a*v
    vx = v*x
    uy = u*y
    cosT = cos(angle)
    sinT = sin(angle)

    rx = (a * (v**2 + w**2) - u * (bv + cw - ux - vy - wz)) * (1 - cosT) + x * cosT + (-cv + bw - wy + vz) * sinT
    ry = (b * (u**2 + w**2) - v * (au + cw - ux - vy - wz)) * (1 - cosT) + y * cosT + (cu - aw + wx - uz) * sinT
    rz = (c * (u**2 + v**2) - w * (au + bv - ux - vy - wz)) * (1 - cosT) + z * cosT + (-bu + av - vx + uy) * sinT

    return [rx, ry, rz]


def rotate(origin, point, angle):
    cy = origin[0]
    cx = origin[1]
    x = point[0]
    y = point[1]

    rad = radians(angle)

    c = cos(rad)
    s = sin(rad)

    rotated_x = int((x - cx) * c - (y - cy) * s + cx)
    rotated_y = int((x - cx) * s - (y - cy) * c + cy)

    return [rotated_x, rotated_y]


world = BulletWorld()
world.setGravity(Vec3(0, 0, -9.81))


class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disableMouse()
        base.setFrameRateMeter(True)
        base.setBackgroundColor(.5,.5,1)

        # Apply scale and position transforms on the model.

        self.sqr = self.loader.loadModel("/c/Users/benja/PycharmProjects/panda3D/models/rubiksCube.bam")
        self.sqr.reparentTo(self.render)

        self.sqr.setPos(0, 0, 0)
        self.sqr.setAntialias(AntialiasAttrib.MAuto)

        self.picker = CollisionTraverser()
        self.pq = CollisionHandlerQueue()

        self.pickerNode = CollisionNode("mouseRay")
        self.pickerNP = self.camera.attachNewNode(self.pickerNode)
        self.pickerNode.setFromCollideMask(BitMask32.bit(1))
        print(self.sqr)
        for x in self.sqr.getChildren():
            x.setCollideMask(BitMask32.bit(1))

        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        self.picker.addCollider(self.pickerNP, self.pq)

        self.dummy = NodePath("dummy")
        self.dummy.reparentTo(self.sqr)

        self.camera.reparentTo(self.dummy)
        self.camera.setPos(0, -5, 0)

        amb_light = AmbientLight("ambient light")
        amb_light.setColor((.8,.8,.8,1))
        self.amb_light_node = self.render.attachNewNode(amb_light)
        self.render.setLight(self.amb_light_node)

        self.r_hold = False
        self.l_hold = False
        self.d_mouse = (0, 0)
        self.mousePrev = (0, 0)
        self.accept("mouse1", self.leftClick)
        self.accept("mouse1-up", self.leftClick)
        self.accept("mouse3", self.rightClick)
        self.accept("mouse3-up", self.rightClick)
        self.radius = 5
        self.vertical_rotation_axis = x_axis
        self.sensitivity = .6

        self.axis = None
        self.selected = None
        self.face = None
        self.cubeGrp = []
        self.pivotPoint = None
        self.side_dummy = NodePath("side dummy")
        self.side_dummy.reparentTo(self.sqr)
        self.side_dummy.setPos(0, 0, 0)

        self.accept("space", self.printCamPos)

        """
        self.accept('arrow_right', self.orbitCam, [0, 1])
        self.accept('arrow_up-repeat', self.rotateCam, [0, 1])
        self.accept('arrow_right', self.rotateCam, [-1, 0])
        self.accept('arrow_right-repeat', self.rotateCam, [-1, 0])
        self.accept('arrow_left', self.rotateCam, [1, 0])
        self.accept('arrow_left-repeat', self.rotateCam, [1, 0])
        self.accept('arrow_down', self.rotateCam, [0, -1])
        self.accept('arrow_down-repeat', self.rotateCam, [0, -1])"""

        self.taskMgr.add(self.updateTask, "update")
        self.render.setShaderAuto()

    def leftClick(self):
        self.l_hold = not self.l_hold
        if not self.l_hold:
            used_poses = []
            used_rotations = []
            for x in self.cubeGrp:
                used_poses.append([round(p, 5) for p in x.getPos(self.render)])
                used_rotations.append([round(p, 5) for p in x.getHpr(self.render)])
            for i, x in enumerate(self.cubeGrp):
                x.reparentTo(self.sqr)
                x.setPos(used_poses[i][0], used_poses[i][1], used_poses[i][2])
                x.setHpr(-used_rotations[i][0], -used_poses[i][1], -used_poses[i][2])
            self.axis = None
            self.selected = None
            self.face = None
            self.cubeGrp = []
            return
        if base.mouseWatcherNode.hasMouse():
            mpos = base.mouseWatcherNode.getMouse()

            self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())
            self.picker.traverse(self.render)

            if self.pq.getNumEntries() > 0:
                self.pq.sortEntries()
                pickedObj = self.pq.getEntry(0).getIntoNodePath()
                self.face = pickedObj.getParent().getParent().getPos(self.render) - pickedObj.getPos(self.render)
                self.selected = pickedObj.getParent().getParent()

    def rightClick(self):
        self.r_hold = not self.r_hold
        if not self.r_hold:
            return

    def updateTask(self, task):
        md = self.win.getPointer(0)
        if self.l_hold or self.r_hold:
            self.d_mouse = [md.x - self.mousePrev[0], md.y - self.mousePrev[1]]

        if self.r_hold:
            self.orbitCam(self.d_mouse[0], self.d_mouse[1])

        if self.selected and not self.cubeGrp:
            if self.axis != None:
                to_check = round(self.selected.getPos(self.render)[self.axis], 5)
                for x in self.sqr.getChildren():
                    if round(x.getPos(self.render)[self.axis], 5) == to_check:
                        if "dummy" not in x.name:
                            self.cubeGrp.append(x)
                c_x = 0
                c_y = 0
                c_z = 0
                for x in self.cubeGrp:
                    c_x += x.getX()
                    c_y += x.getY()
                    c_z += x.getZ()
                c_x /= len(self.cubeGrp)
                c_y /= len(self.cubeGrp)
                c_z /= len(self.cubeGrp)
                c_x = round(c_x, 5)
                c_y = round(c_y, 5)
                c_z = round(c_z, 5)
                for x in self.cubeGrp:
                    u_x = round(x.getPos()[0], 5)
                    u_y = round(x.getPos()[1], 5)
                    u_z = round(x.getPos()[2], 5)
                    if u_x == round(c_x, 5) and u_y == round(c_y, 5) and u_z == round(c_z, 5):
                        self.pivotPoint = [u_x, u_y, u_z]
                        print(self.pivotPoint)
                    else:
                        print(u_x, u_y, u_z)
                self.side_dummy.setHpr(0,0,0)
                for x in self.cubeGrp:
                    x.reparentTo(self.side_dummy)

            else:
                if self.d_mouse != [0, 0]:
                    up = abs(self.d_mouse[1]) > abs(self.d_mouse[0])
                    if round(abs(self.face[1]), 5) == .2:
                        if up:
                            self.axis = 0
                        else:
                            self.axis = 2
                    if round(abs(self.face[0]), 5) == .2:
                        if up:
                            self.axis = 1
                        else:
                            self.axis = 2
                    if round(abs(self.face[2]), 5) == .2:
                        used = self.camera.getHpr(self.render)[0]
                        if -45 >= used > -135:
                            if up:
                                self.axis = 1
                            else:
                                self.axis = 0
                        else:
                            if up:
                                self.axis = 0
                            else:
                                self.axis = 1

        if self.pivotPoint and not self.r_hold:
            if self.axis == 0:
                self.side_dummy.setHpr(self.side_dummy.getHpr()[0], self.side_dummy.getHpr()[1] + self.d_mouse[1], self.side_dummy.getHpr()[2])
            if self.axis == 1:
                self.side_dummy.setHpr(self.side_dummy.getHpr()[0], self.side_dummy.getHpr()[1], self.side_dummy.getHpr()[2] + self.d_mouse[1])
            if self.axis == 2:
                self.side_dummy.setHpr(self.side_dummy.getHpr()[0] + self.d_mouse[0], self.side_dummy.getHpr()[1], self.side_dummy.getHpr()[2])

        self.mousePrev = [md.x, md.y]
        dt = globalClock.getDt()
        # world.doPhysics(dt)
        return Task.cont

    def printCamPos(self):
        print(self.camera.getPos(self.render), self.camera.getHpr(self.render))

    def rotateCam(self, x, y):
        self.camera.setHpr(self.camera.getHpr()[0] + x, self.camera.getHpr()[1] + y, 0)

    def orbitCam(self, x, y):
        x *= self.sensitivity
        y *= self.sensitivity
        dir_x = -1
        dir_y = -1
        if abs(self.camera.getHpr(self.render)[2]) == 180:
            dir_x = 1
        self.dummy.setHpr(self.dummy.getHpr()[0] + (x * dir_x), self.dummy.getHpr()[1] + (y * dir_y), self.dummy.getHpr()[2])
        self.camera.lookAt(self.sqr)


app = MyApp()
app.run()
