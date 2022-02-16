import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lotr-one",                    
    version="0.0.1",                        
    author="Perry Asibey-Bonsu",                     
    description="SDK creation project",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),                                  
    python_requires='>=3.6',                
    py_modules=["lotr"],             
    package_dir={'':'lotr/src'},     
    install_requires=[]                     
)