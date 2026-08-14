import threading
import subprocess
import webview
import os
import sys

if getattr(sys, 'frozen', False) or '__compiled__' in globals():
    bundle_dir = os.path.dirname(__file__)
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))


class Api:
    def __init__(self):
        self.mocha = None
        self.mocha_path = os.path.join(bundle_dir, "mocha")
        print(self.mocha_path)
        self.start_mocha()

    def start_mocha(self):
        thread = threading.Thread(target=self.run_mocha)
        thread.daemon = True
        thread.start()

    def run_mocha(self):
        try:
            self.mocha = subprocess.Popen(
               [f"{self.mocha_path}"],
               stdout=subprocess.PIPE,
               stderr=subprocess.STDOUT,
               text=True
            ) 

            for line in iter(self.mocha.stdout.readline, ''):
               clean = line.strip()
               escaped = clean.replace('\\', '\\\\').replace('"', '\\"')
               if webview.window:
                   active = webview.windows[0]
                   active.evaluate_js(f"setHeader('{clean}')")

            self.mocha.stdout.close()
            self.mocha.wait()
            self.mocha.terminate()

        except Exception as e:
           print(e)