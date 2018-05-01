from setuptools import setup

setup(name='jo',
      version='0.1',
      description='The funniest joke in the world?',
      url='http://github.com/storborg/funniest',
      author='John Lhota',
      author_email='johnlhota@example.com',
      license='MIT',
      packages=['jo'],
      install_requires=[
          'opencv-python',
      ],
      include_package_data=True,
      zip_safe=False)