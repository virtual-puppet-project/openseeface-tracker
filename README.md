# openseeface-tracker
An [OpenSeeFace](https://github.com/emilianavt/OpenSeeFace) tracker for [vpuppr](https://github.com/virtual-puppet-project/vpuppr).

## Setup

### Windows

1. Download the latest [OpenSeeFace release](https://github.com/emilianavt/OpenSeeFace/releases)
2. Copy everything in the download's `Binary` directory to this repo's `OpenSeeFaceFolder/OpenSeeFace` folder
3. Copy everything in the download's `models` directory to this repo's `OpenSeeFaceFolder/models` folder

### Linux

TBD but the setup is very similar to the instructions for Windows

## Generating a PyInstaller binary

This is a manual setup step that can be performed for OpenSeeFace.

Note: These are instructions for advanced users only. If they are too difficult to follow, just use the prepackaged vpuppr releases

1. Clone the [OpenSeeFace](https://github.com/emilianavt/OpenSeeFace) repo and change directories to that repo
2. Run the appropriate `make_exe` script for your OS
3. Copy the contents of the resulting `dist/facetracker` folder into this repo's `OpenSeeFaceFolder/OpenSeeFace` folder
4. Copy the contents of the OpenSeeFace repo's `models` folder into this repo's `OpenSeeFaceFolder/models` folder

