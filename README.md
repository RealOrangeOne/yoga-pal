# Yoga-Pal [![Circle CI](https://circleci.com/gh/RealOrangeOne/yoga-pal.svg?style=svg)](https://circleci.com/gh/RealOrangeOne/yoga-pal)

Command line tool for controlling screen rotation on Lenovo Yoga laptops. This tool is specifically designed for and test on Yoga laptops, other devices support may vary.

## Requirements
* Python 3
* Pip

## Installation
Clone the repo, `cd` into the directory, and then:

    scripts/build
    sudo pip install -e .
__Note__: Installation must be done with an active internet connection.

## Development
	scripts/build
	source env/bin/activate
	pip install --editable .


## Usage

### Rotate
	yoga rotate screen
	yoga rotate touch
	yoga rotate all
Rotates the screen, touchscreen, or both. All is used by default if no component is givens.

__Note__: Rotating touchscreen is likely done automatically with screen, and cannot be overriden. Only added as a catch-all.

Flags `--flip` and `--default` can be added to this command to specify the orientation required.

### Enable & Disable
    yoga enable trackpad
    yoga disable trackpad

    yoga enable touch
    yoga disable touch

    yoga enable all
    yoga disable all
Disables / Enables the trackpad, touch screen, or both. All is used by default if no component is given.
