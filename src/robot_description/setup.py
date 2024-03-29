from setuptools import setup

package_name = 'robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/resource/', ['resource/' + 'robot.urdf.xacro']),
        ('share/' + package_name + '/resource/', ['resource/' + 'macros.urdf.xacro']),
        ('share/' + package_name, ['launch/' + 'robot.launch.py']),
        ('share/' + package_name + '/config', ['config/' + 'ekf.yaml'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='delicat.kuba@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
