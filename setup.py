import setuptools
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
import os
for requirement in requirements:
    os.system("pip install {}".format(requirement))


from Sentyper import __version__


setuptools.setup(
    name="Sentyper",
    version=__version__,
    license='Private',
    author="Junseo",
    author_email="kojunseo@icloud.com",
    description="Korean Sentence Type Analysis Tool",
    long_description=open('README.md').read(),
    url="http://ec2-3-107-23-23.ap-southeast-2.compute.amazonaws.com:8501",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "kiwipiepy==0.17.0",
        "kiwipiepy-model==0.17.0",
    ],
    extras_require={
        'build': [
            "kiwipiepy==0.17.0",
            "kiwipiepy-model==0.17.0",
        ],
        'test': [
            "kiwipiepy==0.17.0",
            "kiwipiepy-model==0.17.0",
        ],
    },
    python_requires='>=3.8',


)