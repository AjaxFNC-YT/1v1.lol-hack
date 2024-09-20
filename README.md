# 1v1.lol HTTP Modifier (or hack)

This project is a Python-based tool designed to modify HTTP requests for the game 1v1.lol, allowing for various tweaks and modifications to the game's behavior.

## Table of Contents
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Editing config.json](#editing-configjson)
- [Installing mitmproxy Certificate](#installing-mitmproxy-certificate)
- [Features](#features)
- [Version Information](#version-information)

## Installation

### Prerequisites
1. **Python 3.9+**: You must have Python installed on your system.

   - Download and install Python from [python.org](https://www.python.org/downloads/).
   - Be sure to check the box for **"Add Python to PATH"** during the installation process.

### Installing from GitHub
1. Go to the GitHub repository: `https://github.com/AjaxFNC-YT/1v1.lol-hack`.
2. Click on the **Code** button and select **Download ZIP**.
3. Extract the downloaded ZIP file to a folder on your computer.

4. Navigate to the project directory where you extracted the files.

5. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

To run the project, navigate to the root folder and run the `run.bat` file by double-clicking it.
## Editing config.json

1. Open the `config.json` file located in the project directory.
2. This file contains the configuration options for running the project.

   **Example structure**:
   ```json
   {
       "weaponLevels": {
           "autosniper": 9999,
           "9mmpistol": 9999,
           "pump_shotgun": 9999,
           "scar": 9999,
           "military_sniper": 9999,
           "flamethrower": 9999,
           "microsmg": 9999,
           "shorty": 9999
       },
       "bodyArmorLevels": {
           "medic": 9999,
           "construction": 9999,
           "basic": 9999,
           "raider": 9999,
           "duelist": 9999,
           "buckshot": 9999,
           "energy": 9999
       },
       "champLevels": {
           "quick": 10,
           "shadow": 10,
           "tron": 10,
           "caesar": 10,
           "jade": 10,
           "frosty": 10
       },
       "gameData": {
           "EquippedWeapons": [
               "lol.1v1.weapons.scar",
               "lol.1v1.weapons.pump_shotgun",
               "lol.1v1.weapons.military_sniper"
           ],
           "Nickname": "",
           "LoLCoins": 999999,
           "Victories": {
               "Showdown": 999,
               "Showdown_Duos": 999,
               "1v1_Clash": 999
           }
       }
   }
   ```

3. Modify the values as necessary, particularly the path to your game and your nickname.
4. Save the file once you've made your changes.

## Installing mitmproxy Certificate

1. Open the project directory.
2. Run the `install_cert.bat` file by double-clicking it. This script will start the proxy, and open the `mitm.it` website in your default browser, from here, install the windows certificate, then run it by double-clicking it.
3. Certificate installer:
- Select "Current User" then "Next"
- Dont change the path (click "Next")
- Dont enter a password or change any options (click "Next")
- Dont change any option, and click "Next"
- Click "Finish"

## Features

- **Changing Weapon Levels**: Adjust the levels of various weapons such as `autosniper`, `9mmpistol`, `pump_shotgun`, and `scar`. Each weapon can be set to any level.

- **Changing Body Armor Levels**: Set the levels for different types of body armor including `medic`, `construction`, `basic`, and `energy`.

- **Changing Champion Levels**: Update the levels of your champions such as `quick`, `shadow`, `tron`, and `frosty`. __Each champion can be set to a maximum level of 10__.

- **Equipped Weapons**: Specify which weapons are currently equipped in the game by modifying the `EquippedWeapons` array. Default options include `scar`, `pump_shotgun`, and `military_sniper`. __EDIT IF YOU DONT HAVE THE "MILITARY SNIPER"__

- **Changing Nickname**: Easily change your in-game nickname by modifying the `Nickname` field in the configuration.

- **Maximizing LoL Coins**: Set your in-game currency (LoLCoins) to the maximum value of 999999, allowing for unlimited purchases.

- **Max Victories**: Set the number of victories in various game modes, including `Showdown`, `Showdown_Duos`, and `1v1_Clash`, to a maximum of 999.


## Other Information

- **Version**: 1.0.0
- **Changelog**: Initial release.

- **NOTE:** This is the first release (also a beta release) some things like Coins, custom name, and win stats go away after one game, things like weapon level and champion level will stay.
- Make sure to edit the config.
- if you dont have the "military_sniper" remove it in your config (dont remove line, just set it to "")
- Ive only added the chamption levels i know the codename for, you can add more and the app will automaticly be able to use them
