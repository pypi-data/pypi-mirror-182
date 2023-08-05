from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='CalimaPython',
      version='2.2.0',
      description='Python interface for Pax Calima Fan',
      long_description=readme(),
      keywords='pax calima fan bluetooth ble',
      author='Super',
      author_email='unknown@unknown.com',
      url='https://github.com/PotatisGrizen/pycalima',
      license='Apache 2.0',
      packages=['pycalima'],
      install_requires=['bleak'],
      entry_points ={
        'console_scripts': ['calimapython=pycalima.cmdline:main'],
      },
      include_package_data=True)
