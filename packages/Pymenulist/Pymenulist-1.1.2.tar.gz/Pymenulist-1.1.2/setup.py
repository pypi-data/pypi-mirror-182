import setuptools
with open(r'C:\Users\Admin\PycharmProjects\choto\README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='Pymenulist',
	version='1.1.2',
	author='Rushpy',
	author_email='oivan4218@gmail.com',
	description='Create console menu',
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages=['Pymenulist'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)