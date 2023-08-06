from setuptools import setup
from setuptools import find_packages
with open('README.md','r') as f:
    long_description=f.read()
REQUIRED = [
     'pillow'
]
VERSION = '10.1.2'
# Package meta-data.
NAME = 'mycolour'
DESCRIPTION='This is a library of images to 2D lists'
URL = 'https://github.com/15989116376/mycolour'
EMAIL = 'lsd.bb770819.com@outlook.com'    # 你的邮箱
AUTHOR = '赖宸铭'     # 你的名字
REQUIRES_PYTHON = '>=3.6.0' # 项目支持的python版本


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    #packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    py_modules=['mycolour'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    #extras_require=[],
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
)