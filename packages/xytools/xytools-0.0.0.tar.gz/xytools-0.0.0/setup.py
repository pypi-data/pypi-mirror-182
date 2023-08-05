from setuptools import setup, find_packages


setup(
    name='xytools',
    license='MIT',
    author="Xi Yong Teo",
    author_email='diamondraft1575@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/The-Superior-Coding-Teos/tools',
    keywords='',
    install_requires=[
          'os', 'time', 'random', 'sys',
      ],

)
