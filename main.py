# Created by AjaxFNC-YT

import asyncio
import json
import os
import time
import sys
import ctypes
import winreg
import win32api
import psutil
from mitmproxy import http, options
from mitmproxy.tools.dump import DumpMaster
import subprocess


def get_config():
    config_path = "config.json"
    if not os.path.exists(config_path):
        print("Error: config.json file not found.")
        sys.exit(1)

    try:
        with open(config_path, "r") as file:
            config = json.load(file)

        if config['appData']['1v1LolPath'] == "":
            print("1v1 LOL Path not set, please set your path in the config.")
            input("press enter to continue.")
            sys.exit(1)
        if config['gameData']['Nickname'] == "":
            print("Nickname not set, please set your nickname in the config.")
            input("press enter to continue.")
            sys.exit(1)

            
        return config
    except json.JSONDecodeError as e:
        print(f"Error reading config.json: {e}")
        sys.exit(1)


def launch_1v1_lol():
    config = get_config()
    if not config['appData']['1v1LolPath']:
        os.system("cls")
        print("Please add your 1v1 lol path in the config..")
        time.sleep(3)
        sys.exit(1)
        return

    path = config['appData']['1v1LolPath']

    try:
        subprocess.Popen(path)
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error launching 1v1 LOL: {e}")
        sys.exit(1)


def on_exit(signal_type):
    set_proxy_settings("", 0)
    print("Proxy disabled on exit.")
    kill_process_by_name("1v1_LOL.exe")


def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)


def kill_process_by_name(name):
    for proc in psutil.process_iter(['pid', 'name']):
        if name.lower() in proc.info['name'].lower():
            try:
                proc.kill()
            except psutil.NoSuchProcess:
                pass


def set_proxy_settings(proxy_server, enable_proxy):
    reg_path = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'ProxyServer', 0, winreg.REG_SZ, proxy_server)
        winreg.SetValueEx(key, 'ProxyEnable', 0, winreg.REG_DWORD, enable_proxy)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Error setting proxy: {e}")


class Proxy:
    def __init__(self):
        self.config = get_config()

    def request(self, flow: http.HTTPFlow) -> None:
        url = flow.request.pretty_url
        print(f"URL: {url}")

    def response(self, flow: http.HTTPFlow) -> None:
        try:
            url = flow.request.pretty_url
            modified = False
            
            if "/login?device=" in url.lower():
                jsonData = flow.response.get_text()
                body = json.loads(jsonData)

                # nickname and lol coins
                body['GeneralData']['Nickname'] = self.config['gameData']['Nickname']
                body['GeneralData']['HardCurrency'] = self.config['gameData']['LoLCoins']

                # wins
                body['GeneralData']['Stats']['Victories']['Showdown'] = self.config['gameData']['Victories']['Showdown']
                body['GeneralData']['Stats']['Victories']['Showdown_Duos'] = self.config['gameData']['Victories']['Showdown_Duos']
                body['GeneralData']['Stats']['Victories']['1v1_Clash'] = self.config['gameData']['Victories']['1v1_Clash']

                # equipped weapons
                if 'Equipment' in body and 'Loadouts' in body['Equipment'] and len(body['Equipment']['Loadouts']) > 0:
                    if 'EquippedWeapons' in body['Equipment']['Loadouts'][0]:
                        body['Equipment']['Loadouts'][0]['EquippedWeapons'] = self.config['gameData']['EquippedWeapons']

                # weapon levels
                weapon_levels = self.config['weaponLevels']
                equipment = body.get('Equipment', {}).get('Equipment', {})

                for weapon, level in weapon_levels.items():
                    weapon_key = f'lol.1v1.weapons.{weapon}'
                    if weapon_key in equipment:
                        equipment[weapon_key]['level'] = level

                # armor levels
                armor_levels = self.config['bodyArmorLevels']
                for armor, level in armor_levels.items():
                    armor_key = f'lol.1v1.armors.body.{armor}'
                    if armor_key in equipment:
                        equipment[armor_key]['level'] = level


                # champ levels
                champs = body.get('Champions', {}).get('OwnedChampions', {})
                champ_levels = self.config['champLevels']
                for champ, level in champ_levels.items():
                    champ_key = f'lol.1v1.champions.{champ}'
                    if champ_key in champs:
                        champs[champ_key]['level'] = level

                modified_json = json.dumps(body)
                flow.response.set_text(modified_json)
                modified = True

            if modified:
                print(f"\n\033[92mModified response for {url}\033[0m\n")

        except Exception as e:
            print(f"Error: {e}")


async def start_proxy():
    addon = Proxy()

    opts = options.Options(listen_host='127.0.0.1', listen_port=8080)
    m = DumpMaster(opts)
    m.addons.add(addon)

    try:
        print("Atria has hooked into 1v1 LOL")
        print("Closing this window will terminate 1v1 LOL")

        set_proxy_settings("127.0.0.1:8080", 1)
        set_console_title("1v1 LOL LAUNCHER | Created by AjaxFNC-YT")

        launch_1v1_lol()

        win32api.SetConsoleCtrlHandler(on_exit, True)
        await m.run()
    except Exception as e:
        print(f"Error running proxy: {e}")
    finally:
        set_proxy_settings("", 0)
        m.shutdown()


if __name__ == "__main__":
    asyncio.run(start_proxy())
