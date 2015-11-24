from setuptools import setup

setup (
	name='yoga-pal',
	version='0.1',
	install_requires=[
		'click'
	],
	entry_points='''
		[console_scripts]
		yoga=project.cli:cli
	''',
)
