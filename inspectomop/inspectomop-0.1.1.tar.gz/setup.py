import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

#load version info
with open('inspectomop/VERSION.txt') as fh:
	version = fh.read().strip()
print(version)
setuptools.setup(
        #descriptors
        name='inspectomop',
        version=version,
        description='Database query tool for the OMOP Common Data Model',
        long_description=long_description,
        long_description_content_type="text/markdown",
        author='Jonathan Badger',
        author_email='jonathancbadger@gmail.com',
        url='https://github.com/jbadger3/inspectomop',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            ],

	#extra_inclustions
    	package_data={'': ['VERSION.txt','*.sqlite3']},
    	include_package_data=True,
        #requirements/dependencies
        python_requires='>=3.0',
        install_requires=['SQLAlchemy>=1.2','pandas'],
        packages=setuptools.find_packages(),
        )
