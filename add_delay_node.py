import time

class add_delay_node:
    """Node that adds a configurable delay between operations"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": ("*",),
                "delay_seconds": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "step": 0.1
                }),
            },
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("input",)
    FUNCTION = "add_delay"
    CATEGORY = "utils"
    
    def add_delay(self, input, delay_seconds):
        delay_text = f"{delay_seconds:.1f} second{'s' if delay_seconds != 1 else ''}"
        print(f"[Delay Node] Starting delay of {delay_text}")
        time.sleep(delay_seconds)
        print(f"[Delay Node] Delay of {delay_text} completed")
        return (input,)

NODE_CLASS_MAPPINGS = {
    "Add Delay": add_delay_node
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Add Delay": "Add Delay"
} 