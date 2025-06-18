import compas_rrc as rrc
from compas.geometry import Point, Vector, Frame, cross_vectors

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    point = Point(600.00,-1331.00,991.00)

    xaxis = Vector(0,1,0)
    yaxis = Vector(1,0,0)



    # coordinate system F
    F = Frame(point, xaxis, yaxis)

    speed = 200  # mm/s
    zone = rrc.Zone.Z50  # precise stop
    feedback_level = 1    # get feedback after motion

    # Send command
    future = abb.send_and_wait(rrc.MoveToFrame(F, speed, rrc.Zone.FINE, rrc.Motion.JOINT))

    # Wait for robot to finish
    print("Move complete:", future)
    # frame = abb.send_and_wait(rrc.GetFrame())


 

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()