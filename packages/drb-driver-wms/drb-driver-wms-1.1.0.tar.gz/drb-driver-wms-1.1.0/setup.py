import versioneer
from setuptools import find_namespace_packages, setup

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

with open('README.md') as f:
    long_description = f.read()


setup(
    name='drb-driver-wms',
    packages=find_namespace_packages(include=['drb.*']),
    description='DRB WMS OGC Service Driver',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='GAEL Systems',
    author_email='drb-python@gael.fr',
    url='https://gitlab.com/drb-python/impl/wms',
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'drb.driver': 'wms = drb.drivers.wms:WmsFactory',
        'drb.topic': 'wms = drb.topics.wms',
    },
    package_data={
        'drb.topics.wms': ['cortex.yml']
    },
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    data_files=[('.', ['requirements.txt'])]
)
