import compas_rrc as rrc
from compas.geometry import Frame, Point, Vector

# Define the frames here (example frames!)
pick_plane_rob1 = Frame(Point(600, -1300, 1000), Vector(0, 1, 0), Vector(1, 0, 0))
place_plane_shared = Frame(Point(700, -1100, 1000), Vector(0, 1, 0), Vector(1, 0, 0))
safe_plane_rob1 = Frame(Point(800, -1000, 1300), Vector(0, 1, 0), Vector(1, 0, 0))

pick_plane_shared = place_plane_shared
place_plane_rob2 = Frame(Point(900, -900, 1000), Vector(0, 1, 0), Vector(1, 0, 0))
safe_plane_rob2 = Frame(Point(1000, -800, 1300), Vector(0, 1, 0), Vector(1, 0, 0))

# Define speed and zone
speed = 300  # mm/s
zone = rrc.Zone.Z5

# Functions for gripper control (replace with your open/close functions)
def open_gripper(robot):
    robot.send_and_wait(rrc.SetDigital('ABB_Scalable_IO_0_DO3', 1))

def close_gripper(robot):
    robot.send_and_wait(rrc.SetDigital('ABB_Scalable_IO_0_DO5', 0))

if __name__ == "__main__":
    # ROS Client
    ros = rrc.RosClient()
    ros.run()

    # ABB Clients
    rob1 = rrc.AbbClient(ros, "/rob1")
    rob2 = rrc.AbbClient(ros, "/rob2")
    print("Connected.")

    # --- ROBOT 1 SEQUENCE ---

    # Move to pick plane
    rob1.send_and_wait(rrc.MoveToFrame(pick_plane_rob1, speed, zone, rrc.Motion.JOINT))
    close_gripper(rob1)

    # Move to shared placing plane
    rob1.send_and_wait(rrc.MoveToFrame(place_plane_shared, speed, zone, rrc.Motion.LINEAR))
    open_gripper(rob1)

    # Move to safe plane
    rob1.send_and_wait(rrc.MoveToFrame(safe_plane_rob1, speed, zone, rrc.Motion.JOINT))

    # --- ROBOT 2 SEQUENCE ---

    # Move to shared pick plane
    rob2.send_and_wait(rrc.MoveToFrame(pick_plane_shared, speed, zone, rrc.Motion.JOINT))
    close_gripper(rob2)

    # Move to placing plane rob2
    rob2.send_and_wait(rrc.MoveToFrame(place_plane_rob2, speed, zone, rrc.Motion.LINEAR))
    open_gripper(rob2)

    # Move to safe plane
    rob2.send_and_wait(rrc.MoveToFrame(safe_plane_rob2, speed, zone, rrc.Motion.JOINT))

    # Close connection
    ros.close()
    ros.terminate()
    print("Finished.")
