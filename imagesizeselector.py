"""
@author: Cyril BOSSELUT
@title: ComfyUI - Image Size Selector
@nickname: Image Size Selector
@description: Custom ComfyUI node for quick image size/aspect ratio selection.
"""

RES_VALUES = {
    "Square (1:1)": {
        "width": 1024, 
        "height": 1024, 
    }, 
    "Banner (16:9)": {
        "width": 1280, 
        "height": 720, 
    }, 
    "Full HD (16:9)": {
        "width": 1920, 
        "height": 1080, 
    }, 
    "Portrait (3:5)": {
        "width": 768, 
        "height": 1280, 
    },
}
 
class SelectImageSize:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "size": ([k for k in RES_VALUES],)
            }
        }
        
    
    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("width", "height",)
    OUTPUT_NODE = True
    FUNCTION = "select_image_size"
    CATEGORY = "utils"
    
    def select_image_size(self, size="Square"):
        width = RES_VALUES[size]["width"]
        height = RES_VALUES[size]["height"]
        return(width, height)
