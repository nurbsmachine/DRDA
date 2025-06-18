import compas_rrc as rrc
from compas.geometry import Point, Vector, Frame

# Start ROS & ABB clients
ros = rrc.RosClient()
ros.run()

abb = rrc.AbbClient(ros, '/rob1')
print('Connected to ABB IRB 6700')

def open_gripper():
    abb.send_and_wait(rrc.SetDigital('ABB_Scalable_IO_0_DO3', 1))
    abb.send_and_wait(rrc.SetDigital('ABB_Scalable_IO_0_DO4', 1))
    print(" → Gripper opened")

def close_gripper():
    abb.send_and_wait(rrc.SetDigital('ABB_Scalable_IO_0_DO5', 0))
    abb.send_and_wait(rrc.SetDigital('ABB_Scalable_IO_0_DO6', 0))
    # wait 2 seconds on the robot controller
    abb.send_and_wait(rrc.WaitTime(2.0))
    print(" → Gripper closed")

# Define frames with matching keys
frames = {
    "home":           Frame(Point(-5.28,   -2174.18, 1839.08),  Vector(0.173042,  0.055946, -0.983324), Vector(0.984443, -0.040716, 0.170922)),
    "safe_plane":     Frame(Point(196.3629, -1990.51,  1560.9089), Vector(0,          1,        0),          Vector(1,        0,        0)),
    "approach_pick":  Frame(Point(-303.6371,-1990.51,  1560.9089), Vector(0,          1,        0),          Vector(1,        0,        0)),
    "pick":           Frame(Point(-303.6371,-1990.51,  1060.9089), Vector(0,          1,        0),          Vector(1,        0,        0)),
    "approach_place": Frame(Point(946.3629, -1990.51,  1560.9089), Vector(0,          1,        0),          Vector(1,        0,        0)),
    "place":          Frame(Point(946.3629, -1990.51,  1060.9089), Vector(0,          1,        0),          Vector(1,        0,        0)),
}

speed_fly    = 1000  # mm/s for transit moves
speed_action =  200  # mm/s for pick/place
zone         = rrc.Zone.Z20

def do_move(step_name, frame, speed, motion):
    abb.send_and_wait(rrc.MoveToFrame(frame, speed, zone, motion))
    print(f" → Step '{step_name}' ({motion}) completed")

# Sequential workflow
do_move("Safe plane",      frames["safe_plane"],     speed_fly,    rrc.Motion.JOINT)
do_move("Approach pick",   frames["approach_pick"],   speed_action, rrc.Motion.LINEAR)
open_gripper()
do_move("Pick",            frames["pick"],           speed_action, rrc.Motion.LINEAR)
close_gripper()
do_move("Retract pick",    frames["approach_pick"],   speed_action, rrc.Motion.LINEAR)
do_move("Approach place",  frames["approach_place"],  speed_fly,    rrc.Motion.JOINT)
do_move("Place",           frames["place"],          speed_action, rrc.Motion.LINEAR)
open_gripper()
do_move("Retract place",   frames["approach_place"],  speed_action, rrc.Motion.LINEAR)
do_move("Return to safe",  frames["safe_plane"],      speed_fly,    rrc.Motion.LINEAR)
do_move("Go home",         frames["home"],           speed_fly,    rrc.Motion.JOINT)

print("All steps completed. Shutting down.")
ros.close()
ros.terminate()
