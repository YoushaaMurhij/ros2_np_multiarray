from setuptools import setup

package_name = 'ros2_np_multiarray'

setup(
    name=package_name,
    version='0.1.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Youshaa Murhij',
    maintainer_email='yosha.morheg@gmail.com',
    description='Convert between numpy ndarray and ROS2 multiarray message',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
