from setuptools import find_packages, setup

package_name = 'skill_booster_4'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml', 'README.md', 'LICENSE']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Skill Booster 4 Student',
    maintainer_email='student@example.com',
    description='UAVs@Berkeley Skill Booster 4: ROS 2 Jazzy Python examples.',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'talker = skill_booster_4.publisher:main',
            'listener = skill_booster_4.subscriber:main',
            'service = skill_booster_4.service:main',
            'client = skill_booster_4.client:main',
        ],
    },
)
