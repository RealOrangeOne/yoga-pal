# yoga-pal
Command line tool for controlling screen rotation on Lenovo Yoga laptops. This tool is specifically designed for and test on Yoga laptops, other devices support may vary.

## Development

	scripts/build
	source env/bin/activate
	pip install --editable .

## Usage
### Rotate
	yoga rotate screen
	yoga rotate touch
	yoga rotate all
Rotates the screen, touchscreen, or both.

Note: Rotating touchscreen is likely done automatically with screen, and cannot be overriden. Only added as a catch-all.

Flags '--flip' and '--default' can be added to this command to specify the orientation required.

### Disable
    yoga disable trackpad
    yoga disable touch
    yoga disable all
Disables the trackpad, touch screen, or both

Flags '--enable' and '--disable' can be added to this command to specify the status required.
