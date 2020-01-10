# spotlight_parser
This code reads and extracts data from spotlight databases present on macOS and iOS.  

## License
GPL v3

## Latest version
0.9.1 - Download [here](https://github.com/ydkhatri/spotlight_parser/releases)

## Dependencies  
If running from code, you will need python 3.7 and the following python packages installed:

* lz4
* enum34
* lzfse

The first two can be installed using the command `pip install lz4 enum34`

You will also need to install the lzfse decompression library. Follow the instructions [here](https://github.com/ydkhatri/mac_apt/tree/master/Libraries_For_Windows) to install it on windows. For linux, follow this [link](https://github.com/ydkhatri/mac_apt/wiki/Installation-for-Python3.7#build-compile-and-install-pylzfse) and only complete the **install pylzfse** part.  
## Usage
This script will process individual Spotlight database files. These files are found under the volume at location `/.Spotlight-V100/Store-V2/<UUID>` where `<UUID>` represents a store id. In that folder you should find files named `store` and `.store` which are the Spotlight databases. Provide these as input to this script.

`spotlight_parser.py [-p OUTPUT_PREFIX] <path_to_database>  <output_folder>`

iOS spotlight databases are also supported now. These can be found here:
* /private/var/mobile/Library/Spotlight/CoreSpotlight/NSFileProtectionComplete/index.spotlightV2
* /private/var/mobile/Library/Spotlight/CoreSpotlight/NSFileProtectionCompleteUnlessOpen/index.spotlightV2
* /private/var/mobile/Library/Spotlight/CoreSpotlight/NSFileProtectionCompleteUntilFirstUserAuthentication/index.spotlightV2

For iOS databases, you will also need to have the files that begin with `dbStr` (which are available 
in the same folder as store.db). These files are specific to that instance of store.db. Ideally, just extract the whole folder (instead of a single file). 

Example:  
`python spotlight_parser.py c:\spot\store.db c:\output`

## Thanks  
Mason Bartle for porting the code to python3.
