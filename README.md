# ComfyUI-Delay

This custom node for ComfyUI provides a simple way to add configurable delays between node operations, which can be useful for debugging, timing control, or managing resource usage in workflows.

## Features

- Adds configurable delays between node operations
- Works with any type of input/output
- Visual progress bar in the ComfyUI UI showing delay progress
- Responds to ComfyUI's Stop button while delaying
- Provides console feedback about delay duration
- Easy to integrate into existing ComfyUI workflows
- No additional dependencies

## Requirements

- ComfyUI
- Python 3.10+

## Installation

### Via ComfyUI-Manager (recommended)

Search for `ComfyUI_Delay` in [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) and click Install, then restart ComfyUI.

### Manual installation

1. Navigate to your ComfyUI custom nodes folder:
   ```
   cd /path/to/ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```
   git clone https://github.com/a-und-b/ComfyUI_Delay.git
   ```
3. Restart ComfyUI

## Usage

After installation, you'll find a new node called "Add Delay" in the utils menu.

1. Add the node anywhere in your workflow where you want to introduce a delay
2. Set the desired delay duration in seconds
3. Connect any input to the node. It will pass through unchanged after the specified delay
4. While the node is running, the ComfyUI UI shows a progress bar for the delay
5. Click ComfyUI's **Stop** button at any time to cancel an in-progress delay
6. The console will show feedback when the delay starts and completes

## Console Output

The node provides feedback in the console:

```
[Delay Node] Starting delay of 1.0 second
[Delay Node] Delay of 1.0 second completed
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## Acknowledgements

- Progress bar and cancellation support contributed by [@obrofg](https://github.com/obrofg) ([#1](https://github.com/a-und-b/ComfyUI_Delay/pull/1))

## License

This project is open-sourced under the MIT License - see the LICENSE file for details.
