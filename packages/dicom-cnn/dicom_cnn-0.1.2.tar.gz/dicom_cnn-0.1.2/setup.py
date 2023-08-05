import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()
    #remove url
    required.pop(0)
    #remove comments python_version
    requirements = list(map(lambda x: x.split(';')[0], required))

setuptools.setup(
    name="dicom_cnn",
    version="0.1.2",
    author="Pixilib",
    url="https://github.com/Pixilib/dicom_cnn",
    python_requires="~=3.9",
    description="Librairie to sort - process dicom to feed CNN models",
    packages=setuptools.find_packages(where='src'),    # List of all python modules to be installed
    install_requires=requirements,
    package_dir={"": "src"}
)