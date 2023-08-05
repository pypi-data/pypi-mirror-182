import versioneer
from setuptools import find_packages, setup, find_namespace_packages

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='drb-driver-zip',
    packages=find_namespace_packages(include=['drb.*']),
    description='DRB Zip driver',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='GAEL Systems',
    author_email='drb-python@gael.fr',
    url='https://gitlab.com/drb-python/impl/zip',
    install_requires=REQUIREMENTS,
    test_suite='tests',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.8',
    entry_points={
        'drb.driver': 'zip = drb.drivers.zip:DrbZipFactory',
        'drb.topic': 'zip = drb.topics.zip'
    },
    package_data={
        'drb.topics.zip': ['cortex.yml']
    },
    version=versioneer.get_version(),
    data_files=[('.', ['requirements.txt'])],
    cmdclass=versioneer.get_cmdclass(),
    project_urls={
        'Documentation': 'https://drb-python.gitlab.io/impl/zip',
        'Source': 'https://gitlab.com/drb-python/impl/zip',
    }
)
