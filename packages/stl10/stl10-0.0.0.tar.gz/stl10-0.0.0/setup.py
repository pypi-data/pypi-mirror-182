from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.0'
DESCRIPTION = 'Easy to use stl-10'
LONG_DESCRIPTION = 'build stl-10 dataset'

# Setting up
setup(
    name="stl10",
    version=VERSION,
    author="Shwky Mohamed",
    author_email="shwkym54@gmail.com",
    description=DESCRIPTION,
    # long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'tensorflow', 'numpy', 'cv2'],
    keywords=['python', 'ML', 'dataset', 'stl-10', 'STL10'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)