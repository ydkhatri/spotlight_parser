# spotlight_parser
This code reads and extracts data from spotlight databases present on macOS and iOS.  

## License
GPL v3

## Latest version
0.9.2 - Download [here](https://github.com/ydkhatri/spotlight_parser/releases)

_**It is recommended to use the mac_apt_artifact_only script/exe (from [mac_apt](https://github.com/ydkhatri/mac_apt)) instead of this project as that uses this same code, but also offers a few extra features like SQLITE output, and creating separate views for ios apps.**_

## Dependencies  
If running from code, you will need python 3.7 and the following python packages installed:

* lz4
* pyliblzfse

These can be installed using the command `pip3 install lz4 pyliblzfse`

## Usage

This script will process individual Spotlight database files which are always named `store.db` and `.store.db`. You will need to provide a path to this file and an output path, with syntax as shown below.

`spotlight_parser.py [-p OUTPUT_PREFIX] <path_to_database>  <output_folder>`

Example:  
`python spotlight_parser.py c:\spot\store.db c:\output`

## Spotlight database locations and types
On macOS, under each volume at location `/.Spotlight-V100/Store-V2/<UUID>` where `<UUID>` represents a store id, you should find files named `store` and `.store` which are the Spotlight databases. Provide these as input to this script.

Since macOS 10.13, there are also spotlight databases for each user under `~/Library/Metadata/CoreSpotlight/index.spotlightV3/` 

iOS spotlight databases are also supported now. These can be found here:
* /private/var/mobile/Library/Spotlight/CoreSpotlight/NSFileProtectionComplete/index.spotlightV2
* /private/var/mobile/Library/Spotlight/CoreSpotlight/NSFileProtectionCompleteUnlessOpen/index.spotlightV2
* /private/var/mobile/Library/Spotlight/CoreSpotlight/NSFileProtectionCompleteUntilFirstUserAuthentication/index.spotlightV2

For iOS databases, you will also need to have the files that begin with `dbStr` (which are available 
in the same folder as store.db). These files are specific to that instance of store.db. Ideally, just extract the whole folder (instead of a single file). 

## Spotlight resources by me
- [Paper - Investigating spotlight internals to extract metadata](https://www.sciencedirect.com/science/article/pii/S1742287618300860)  
- [Slides from NW3C presentation on Spotlight](https://github.com/ydkhatri/Presentations/blob/master/NW3C%20Spotlight%20on%20iOS%20and%20macOS-%20December%202020.pdf)

## Thanks  
Mason Bartle for porting the code to python3.
