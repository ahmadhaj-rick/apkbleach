from setuptools import setup
setup(
    name = 'apkbleach',
    version = '2.0',
    packages=['apkbleach', 'apkbleach.Resources'],           # 1
    package_dir={'apkbleach.Resources': 'apkbleach'},          # 2
    package_data={'apkbleach.Resources': ['../Resources/*']},
    install_requires=[
        'argparse',
        'colorama',
        'pillow',
        'pyfiglet==0.8.post1',
        'requests'
    ],
    entry_points = {
        'console_scripts': [
            'apkbleach = apkbleach.__main__:main'
        ]
    })
