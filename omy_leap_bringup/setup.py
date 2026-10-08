from glob import glob

from setuptools import find_packages, setup

package_name = 'omy_leap_bringup'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/urdf', glob('urdf/*.xacro')),
        ('share/' + package_name + '/config', glob('config/*.yaml')),
        ('share/' + package_name + '/launch', glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='SHAPE-UP Tactile',
    maintainer_email='chlgkals0730@gmail.com',
    description='OMY F3M follower bringup without the gripper (end unit mocked).',
    license='Apache-2.0',
)
