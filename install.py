import asyncio
import winreg
from mitmproxy import http, options
from mitmproxy.tools.dump import DumpMaster
import webbrowser
import signal
import sys


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
    def request(self, flow: http.HTTPFlow) -> None:
        pass

    def response(self, flow: http.HTTPFlow) -> None:
        pass


async def start_proxy():
    addon = Proxy()

    opts = options.Options(listen_host='127.0.0.1', listen_port=8080)
    m = DumpMaster(opts)
    m.addons.add(addon)

    try:
        print('Proxy running. (INSTALL SCRIPT)\n\nWarning, this is the install script, not the http hack for 1v1 lol. Please configure the "config.json" then run "run.bat"')
        print("Opening mitm.it in your default browser.")

        set_proxy_settings("127.0.0.1:8080", 1)
        webbrowser.open("http://mitm.it")

        await m.run()
    except Exception as e:
        print(f"Error running proxy: {e}")
    finally:
        print("Shutting down proxy...")
        set_proxy_settings("", 0)
        m.shutdown()


def signal_handler(sig, frame):
    print("\nSignal received, shutting down...")
    set_proxy_settings("", 0)
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    asyncio.run(start_proxy())
