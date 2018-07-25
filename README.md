# spotlight_parser
This code reads and extract data from macOS spotlight databases.  

## License
GPL v3

## Dependencies
The code needs the following python packages installed:
* lz4
* enum34

Both can be installed using the command `pip install lz4 enum34`

## Usage
This script will process individual Spotlight database files. These files are found under the volume at location `/.Spotlight-V100/Store-V2/<UUID>` where <UUID> represents a store id. In that folder you should find files named `store` and `.store` which are the Spotlight databases. Provide these as input to this script.

Example:
`python spotlight_parser.py c:\spot\store c:\output`
