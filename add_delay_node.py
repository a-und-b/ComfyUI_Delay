import time

class AddDelay:
    """Node that adds a configurable delay between operations"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "delay_seconds": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 300.0,
                    "step": 0.1
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "add_delay"
    CATEGORY = "utils"
    
    def add_delay(self, image, delay_seconds):
        # Add the specified delay
        time.sleep(delay_seconds)
        # Return the image unchanged
        return (image,)

NODE_CLASS_MAPPINGS = {
    "Add Delay": AddDelay
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Add Delay": "Add Delay"
} 