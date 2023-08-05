import versioneer
from setuptools import find_packages, setup, find_namespace_packages

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='drb-driver-netcdf',
    packages=find_namespace_packages(include=['drb.*']),
    description='DRB NetCDF driver',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='GAEL Systems',
    author_email='drb-python@gael.fr',
    url='https://gitlab.com/drb-python/impl/netcdf',
    install_requires=REQUIREMENTS,
    test_suite='tests',
    data_files=[('.', ['requirements.txt'])],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.8',
    entry_points={
        'drb.driver': 'netcdf = drb.drivers.netcdf:DrbNetcdfFactory',
        'drb.topic': 'netcdf = drb.topics.netcdf'
    },
    package_data={
        'drb.topics.netcdf': ['cortex.yml']
    },

    use_scm_version=True,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    project_urls={
        'Documentation': 'https://drb-python.gitlab.io/impl/netcdf',
        'Source': 'https://gitlab.com/drb-python/impl/netcdf',
    }
)
