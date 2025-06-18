import math
import compas_rrc as rrc
from compas.geometry import Point, Vector, Frame

# Parameters
radius = 150
height = 450
layer_height = 3
segments = 60  # resolution per layer
offset_x = 1500  # offset from robot base
extrusion_on_signal = 1  # Use the appropriate digital signal for extrusion ON/OFF
extrusion_off_signal = 0  # Use the appropriate digital signal for extrusion OFF
speed = 1000  # mm/s
zone = rrc.Zone.FINE  # precise stop
feedback_level = 1    # feedback after each move

# Generate frames
frames = []

for layer in range(int(height / layer_height)):
    z = layer * layer_height

    for i in range(segments):
        theta = 2 * math.pi * (i / segments)
        x = radius * math.cos(theta) + offset_x
        y = radius * math.sin(theta)

        # Tangent direction along circular path = X-axis
        dx = -math.sin(theta)
        dy = math.cos(theta)
        dz = 0

        # Extrusion direction = Y-axis (upward)
        xaxis = Vector(dx, dy, dz)
        yaxis = Vector(0, 0, 1)

        point = Point(x, y, z)
        frame = Frame(point, xaxis, yaxis)
        frames.append(frame)

print(f"Generated {len(frames)} COMPAS frames.")

# Create Ros Client
ros = rrc.RosClient()
ros.run()

# Create ABB Client
abb = rrc.AbbClient(ros, '/rob1')
print("Connected to ABB robot.")

# Start 3D Printing Simulation
for frame in frames:
    # Extrusion ON
    abb.send(rrc.SetDigital(1, extrusion_on_signal))

    # Move to next frame (layer)
    future = abb.send_and_wait(rrc.MoveToFrame(frame, speed, zone, feedback_level))

    # Wait for movement to complete
    done = future.result()
    print(f"Layer {frames.index(frame) + 1} complete. Feedback: {done}")

    # Extrusion OFF after the layer is complete
    abb.send(rrc.SetDigital(1, extrusion_off_signal))

# End of Code
print('Finished 3D printing simulation.')

# Close client
ros.close()
ros.terminate()
