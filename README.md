# arduino-stream-team 


#### This is a WIP realtime streaming cli for arduino using pubnub and pyfirmata. 

`arduino-stream-team` is a tool to help facilitate the process of realtime data manipulation. Currently `arduino-stream-team` only supports publish and subscribe functionality. More to come soon!  

### Installation

To install `arduino-stream-team`, cd into the `arduino-stream-team` directory and run:

	$ ./configure
	$ sudo make
	$ sudo make install

### Usage

       usage: arduino-stream-team [-h] [-p [PUB] | -s [SUB]] [-v] channel publish subscribe

       arduino-stream-team

       positional arguments:
         channel               channel
         publish               publish
         subscribe             subscribe

       optional arguments:
         -h, --help            show this help message and exit
         -p [PUB], --pub [PUB]
                               Value must be yes
         -s [SUB], --sub [SUB]
                               Value must be yes
         -v, --version         show program's version number and exit
       

'arduino-stream-team' under GPLv3

See the COPYING file for the full license text.

TODO: Add data channel selectors.

TODO: Add graphics/plotting capibility.

TODO: Add requirements.txt.

TODO: Add database recording capibilities.
