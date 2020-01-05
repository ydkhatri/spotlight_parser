# spotlight_parser
This code reads and extracts data from spotlight databases on macOS and iOS.  

## License
GPL v3

## Dependencies
<<<<<<< HEAD
The code needs python 3.7, and the following python packages installed:
=======
The code needs python (2.7 or 3.6+) and the following python packages installed:
>>>>>>> e8675b03a516af6d9c7c936982862f8cfbd35f34
* lz4
* enum34
* lzfse

The first two can be installed using the command `pip install lz4 enum34`

You will also need to install the lzfse decompression library. Follow the instructions [here](https://github.com/ydkhatri/mac_apt/tree/master/Libraries_For_Windows) to install it on windows.
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
`python spotlight_parser.py c:\spot\store c:\output`

## Thanks
<<<<<<< HEAD
Mason Bartle for porting the code to python3 earlier.
=======
Mason Bartle for porting the code to python3.
>>>>>>> e8675b03a516af6d9c7c936982862f8cfbd35f34
