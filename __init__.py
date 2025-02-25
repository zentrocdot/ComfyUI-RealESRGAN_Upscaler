'''RealEsrganUpscaler __init__ file.'''

# Import the Python modules.
from .realesrgan.realesrgan_upscaler import *
from .realesrgan.show_data import *

NODE_CLASS_MAPPINGS = { 
    "🚀 Universal RealESRGAN Upscaler": RealEsrganUpscaler,
    "🧳 Show Data": ShowData,
    }
    
WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

# Print message into the terminal window.
print("\033[34mComfyUI RealEsrganUpscaler Nodes: \033[92mLoaded\033[0m")
