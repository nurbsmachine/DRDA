import compas_rrc as rrc

if __name__ == "__main__":

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb1 = rrc.AbbClient(ros, "/rob1")
    # abb2 = rrc.AbbClient(ros, "/rob2")
    print("Connected.")

    # Read value of joints
    robot_joints1, external_axes1 = abb1.send_and_wait(rrc.GetJoints())
    # robot_joints2, external_axes2 = abb2.send_and_wait(rrc.GetJoints())

    # Print received values
    print(robot_joints1, external_axes1)
    # print(robot_joints2, external_axes2)

    value = 10

    # Change a joint value [°]
    robot_joints1.rax_1 -= value
    
    # robot_joints2.rax_1 += value

    # Set speed [mm/s]
    speed = 1000

    # Move robot the new pos
    future1 = abb1.send(
        rrc.MoveToJoints(robot_joints1, external_axes1, speed, rrc.Zone.FINE, feedback_level=1)
    )
    # future2 = abb2.send(
    #     rrc.MoveToJoints(robot_joints2, external_axes2, speed, rrc.Zone.FINE, feedback_level=1)
    # )

    # Wait for future feedback
 # Wait for future feedback
    done = future1.result()
    # Print feedback
    print("Feedback = ",done)

    # End of Code
    print("Finished")

    # Close client
    ros.close()
    ros.terminate()
