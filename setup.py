from setuptools import setup

setup(name='lazylog',
      version='0.1',
      description='A lazy logging library',
      url='http://github.com/ymbirtt/lazylog',
      author='Ymbirtt',
      license='MIT',
      packages=['lazylog'],
      install_requires=[
          'logging',
      ],
      zip_safe=False)
