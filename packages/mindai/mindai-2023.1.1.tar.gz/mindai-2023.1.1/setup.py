import os , codecs

from setuptools import setup, find_packages

pkg = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(pkg, "README.md"), encoding="utf-8") as fh:
	
    long_description = "\n" + fh.read()


setup(

    name="mindai",
    
    version="2023.1.1",
    
    author="ReBack",
    
    author_email="",
    
    description = ("list of tools using ai."),
    
    long_description_content_type="text/markdown",
    
    url="",
    
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    
    long_description=long_description,
    
    packages=find_packages(),
    
    install_requires=['httpx','uuid'],
    
    keywords=['voice'],
    
    classifiers=[
    
        "Development Status :: 1 - Planning",
        
        "Intended Audience :: Developers",
        
        "Programming Language :: Python :: 3",
        
        "Operating System :: Unix",
        
        "Operating System :: MacOS :: MacOS X",
        
        "Operating System :: Microsoft :: Windows",
    ]
)
