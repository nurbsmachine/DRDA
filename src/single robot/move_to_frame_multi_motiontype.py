import compas_rrc as rrc
from compas.geometry import Point, Vector, Frame

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Define multiple frames
    frames = [
        Frame(Point(600.00, -1331.00, 991.00), Vector(0, 1, 0), Vector(1, 0, 0)),
        Frame(Point(768, -1218, 1486), Vector(0.290866, 0.938115, -0.187983), Vector(0.80699, -0.135005, 0.574927)),
        Frame(Point(-895, -1258, 1755), Vector(0.305927, 0.824484, -0.476062), Vector(0.946093, -0.207403, 0.248781)),
        Frame(Point(-1224, -1190, 1472), Vector(0.305955, 0.824445, -0.476112), Vector(0.946074, -0.207358, 0.248892))
    ]

    # Define motion types for each frame (User specifies this)
    motion_types = [
        rrc.Motion.JOINT,  # First frame: Joint motion
        rrc.Motion.JOINT,  # Second frame: Joint motion
        rrc.Motion.LINEAR,   # Third frame: Linear motion
        rrc.Motion.LINEAR  # Fourth frame: Linear motion
    ]

    speed = 1000  # mm/s
    zone = rrc.Zone.Z20  # stop precisely at each frame

   # Move through each frame one by one
    for i, frame in enumerate(frames):
        print(f"Moving to Frame {i+1}: {frame}")
        result = abb.send_and_wait(rrc.MoveToFrame(frame, speed, zone, motion_types))
        print("  -> Move complete")

    print("All frames completed.")

    # End of Code
    ros.close()
    ros.terminate()