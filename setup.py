from setuptools import setup, find_packages

setup(
    name='LINQ-cython',
    version="0.2.3",
    description=(
        '和c#一样使用方式的linq,并经使用cython进行加速',
        'the linq like c#,and will speed up  by cython'
    ),
    long_description=open('README.rst','rb').read(),
    author='卞辉（beincy）',
    author_email='bianhui0524@sina.com',
    maintainer='卞辉(beincy)',
    maintainer_email='bianhui0524@sina.com',
    license='MIT',
    packages=['PYLINQ'],
    platforms=["all"],
    url='https://github.com/beincy/PYLINQ',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)