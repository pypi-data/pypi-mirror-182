import versioneer
from setuptools import find_packages, setup, find_namespace_packages

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

with open('README.md') as f:
    long_description = f.read()


setup(
    name='drb-driver-webdav',
    packages=find_namespace_packages(include=['drb.*']),
    description='DRB Web-based Distributed Authoring'
                ' and Versioning driver',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='GAEL Systems',
    author_email='drb-python@gael.fr',
    url='https://gitlab.com/drb-python/impl/webdav',
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'drb.driver': 'webdav = drb.drivers.webdav:DrbWebdavFactory',
        'drb.topic': 'webdav = drb.topics.webdav'
    },
    package_data={
        'drb.topics.webdav': ['cortex.yml']
    },

    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    data_files=[('.', ['requirements.txt'])]
)
