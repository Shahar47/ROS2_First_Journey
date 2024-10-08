from setuptools import setup

package_name = 'turtlesim_catch_them_all'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shahar',
    maintainer_email='your.email@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "turtle_controller = turtlesim_catch_them_all.turtle_controller:main",
            "turtle_spawner = turtlesim_catch_them_all.turtle_spawner:main"
        ],
    },
)
