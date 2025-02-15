```
 /$$      /$$ /$$$$$$$  /$$      /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$   /$$$$$$  /$$$$$$$  /$$     /$$
| $$$    /$$$| $$__  $$| $$$    /$$$| $$_____/|__  $$__//$$__  $$ /$$__  $$| $$__  $$|  $$   /$$/
| $$$$  /$$$$| $$  \ $$| $$$$  /$$$$| $$         | $$  | $$  \ $$| $$  \__/| $$  \ $$ \  $$ /$$/ 
| $$ $$/$$ $$| $$$$$$$/| $$ $$/$$ $$| $$$$$      | $$  | $$$$$$$$|  $$$$$$ | $$$$$$$/  \  $$$$/  
| $$  $$$| $$| $$____/ | $$  $$$| $$| $$__/      | $$  | $$__  $$ \____  $$| $$____/    \  $$/   
| $$\  $ | $$| $$      | $$\  $ | $$| $$         | $$  | $$  | $$ /$$  \ $$| $$          | $$    
| $$ \/  | $$| $$      | $$ \/  | $$| $$$$$$$$   | $$  | $$  | $$|  $$$$$$/| $$          | $$    
|__/     |__/|__/      |__/     |__/|________/   |__/  |__/  |__/ \______/ |__/          |__/    
                                                                                                 
                               We know where you live!                                                                               
                                                                         
                                  (c) Maxproton Labs
                            Licensed under Apache License 2.0

              Please do not use in military or for illegal purposes.
         (This is the wish of the author and non-binding. Many people working
          in these organizations do not care for laws and ethics anyways.
               You are not one of the "good" ones if you ignore this.)
```

## Overview

This tool requires a list of urls, (use MpRecon) and searches for images on the urls, it then analysis them for meta data and captures it. 
## Features

- Analyze a given list looking for images.
- Captures meta data
- Flags when locations are provided in this meta data
- Generates a report afterwards

## Installation

Ensure you have Python installed (>=3.6). Clone this repository and navigate into the directory:

Run the install bash.

Please note!! --break-system-packages is used!
```bash
git clone https://github.com/maxproton/mpmetaspy
cd mpmetaspy
bash install.sh
```
## Usage
### Basic
```bash
python main.py --file [url-list] --verbose (optional)
```

## Licence
Licensed under Apache License 2.0