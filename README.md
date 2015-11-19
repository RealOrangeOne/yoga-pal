# yoga-pal
Command line tool for controlling screen rotation on Lenovo Yoga laptops

## Development

	scripts/build
	source env/bin/activate
	pip install --editable .

## Usage
	yopa rotate screen
	yopa rotate touch
	yopa rotate all
Rotates the screen, touchscreen, or both. 

Note: Rotating touchscreen is likely done automatically with screen, and cannot be overriden. Only added as a catch-all.

Flags '--flip' and '--default' can be added to this command to specify the orientation required.

