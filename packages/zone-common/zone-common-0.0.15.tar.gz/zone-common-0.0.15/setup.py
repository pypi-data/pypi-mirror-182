from setuptools import setup

setup(
    name='zone-common',
    version='0.0.15',
    description='Common utility package for zone c2c',
    author='Shreyas Chorge',
    author_email='shreyaschorge81@gmail.com',
    url='https://github.com/Shreyaschorge/zone_common',
    packages=["zone_common/exceptions", "zone_common/events", "zone_common/middlewares"],
    package_dir={'': 'src'},
    install_requires=['werkzeug',
                      'nats-py',
                      'asyncio',
                      'python-decouple',
                      'pyjwt'
                      ],
)
