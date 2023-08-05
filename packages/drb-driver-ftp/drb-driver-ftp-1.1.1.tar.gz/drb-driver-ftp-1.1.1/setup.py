import versioneer
from setuptools import find_packages, setup, find_namespace_packages

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='drb-driver-ftp',
    packages=find_namespace_packages(include=['drb.*']),
    description='DRB Ftp implementation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='GAEL Systems',
    author_email='drb-python@gael.fr',
    url='https://gitlab.com/drb-python/impl/ftp',
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
        'drb.driver': 'ftp = drb.drivers.ftp:DrbFtpFactory',
        'drb.topic': 'ftp = drb.topics.ftp'
    },
    package_data={
        'drb.topics.ftp': ['cortex.yml']
    },

    use_scm_version=True,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
