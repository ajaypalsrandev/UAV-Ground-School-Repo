# UAVs@Berkeley — Skill Booster 4

A complete ROS 2 Jazzy Python package implementing the publisher/subscriber
and service/client examples from the official tutorials.

This submission contains the source code and package configuration. Installing
or running ROS is not required for the updated assignment. ROS was not installed
or run while preparing this package; runtime behavior has not been verified.

## Contents

```text
skill_booster_4/
├── skill_booster_4/
│   ├── __init__.py
│   ├── publisher.py
│   ├── subscriber.py
│   ├── service.py
│   └── client.py
├── resource/
│   └── skill_booster_4     # intentionally empty ament index marker
├── setup.py
├── setup.cfg
├── package.xml
├── README.md
└── LICENSE
```

| File | Executable | Behavior |
| --- | --- | --- |
| `publisher.py` | `talker` | Publishes numbered `Hello World` messages every 0.5 seconds. |
| `subscriber.py` | `listener` | Logs each received message. |
| `service.py` | `service` | Adds the two integers in each request. |
| `client.py` | `client` | Sends two command-line integers and logs their sum. |

The topic pair uses `std_msgs/msg/String` on `topic`, with queue depth 10.
The service pair uses `example_interfaces/srv/AddTwoInts` on `add_two_ints`.
The client waits for availability and sends its request asynchronously.

## Package configuration

`package.xml` declares `ament_python` as the build tool and `rclpy`, `std_msgs`,
and `example_interfaces` as runtime dependencies. ROS dependencies belong in
this manifest; they are not pip requirements. `setup.py` uses `setuptools`,
installs the resource marker and manifest, and registers all four executables.
`setup.cfg` places executables where `ros2 run` expects them.

The maintainer name and email in `setup.py` and `package.xml` are neutral
placeholders (`Skill Booster 4 Student`, `student@example.com`), not a real
contact. You may replace both consistently with your submission identity.

## Optional future build and run

These commands are for a Linux machine with ROS 2 Jazzy, colcon, and the listed
dependencies already installed. They are not required for this submission.

Place this extracted package folder at `~/ros2_ws/src/skill_booster_4`.
From the workspace root:

```bash
source /opt/ros/jazzy/setup.bash
cd ~/ros2_ws
colcon build --packages-select skill_booster_4
source install/setup.bash
```

In each new terminal, source both the ROS installation and workspace:

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
```

Run the publisher and subscriber in separate terminals:

```bash
ros2 run skill_booster_4 talker
```

```bash
ros2 run skill_booster_4 listener
```

Run the service and client in separate terminals:

```bash
ros2 run skill_booster_4 service
```

```bash
ros2 run skill_booster_4 client 2 3
```

The expected client result is `Result of add_two_ints: for 2 + 3 = 5`.
This is illustrative output, not a recorded execution. Supply two valid signed
64-bit integers whose sum also fits that range. Stop persistent nodes with Ctrl+C.

## Official references and attribution

- [Jazzy Python publisher/subscriber tutorial](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)
- [Jazzy Python service/client tutorial](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html)
- [Official publisher/subscriber example source, Jazzy branch](https://github.com/ros2/examples/tree/jazzy/rclpy/topics)
- [Official service/client tutorial source, Jazzy branch](https://github.com/ros2/ros2_documentation/blob/jazzy/source/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.rst)

Publisher and subscriber code comes from the official Jazzy examples and retains
its original copyright/license headers. Service and client code follows the
complete code blocks in the official Jazzy tutorial. Files are renamed and both
tutorials are packaged together as `skill_booster_4`; the tutorial node names,
interfaces, behavior, and executable names are retained. See `LICENSE` for the
Apache License 2.0 text.
