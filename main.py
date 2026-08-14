import webview
import os
import threading
import socket
from flask import Flask, render_template
from api import Api

# Disable the problematic WebKit DMA-BUF renderer
os.environ["WEBKIT_DISABLE_DMABUF_RENDERER"] = "1"

# Optional: fallback to older GL sync if explicit sync fails on Nvidia
os.environ["__NV_DISABLE_EXPLICIT_SYNC"] = "1"

# Optional: force GTK to use the standard GL renderer instead of Vulkan
os.environ["GSK_RENDERER"] = "gl"

app = Flask(__name__)

def get_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port

@app.route("/")
def root():
    return render_template("index.html")

def run_flask(port):
    app.run(host="0.0.0.0", port=port, debug=False)

if __name__ == "__main__":
    port = get_free_port()
    server_thread = threading.Thread(target=run_flask, args=(port,) ,daemon=True)
    server_thread.start()

    api = Api()
    webview.create_window("Latte", f"http://localhost:{port}", width=1280, height=800, resizable=False, js_api=api)
    webview.start(gui="gtk")