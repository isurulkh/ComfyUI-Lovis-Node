"""
ComfyUI Utility Nodes

Custom nodes for ComfyUI that provide text and audio processing utilities:
- Line Count: Counts the number of lines in text input
- Text to Single Line: Converts multi-line text to single line with customizable separators
- Audio Duration: Analyzes audio files to get duration in seconds or frame count
"""

from .line_count_node import LineCountNode
from .text_to_single_line_node import TextToSingleLineNode
from .audio_duration_node import AudioDurationNode

# Node class mappings for ComfyUI
NODE_CLASS_MAPPINGS = {
    "LineCountNode": LineCountNode,
    "TextToSingleLineNode": TextToSingleLineNode,
    "AudioDurationNode": AudioDurationNode
}

# Display name mappings for the ComfyUI interface
NODE_DISPLAY_NAME_MAPPINGS = {
    "LineCountNode": "Line Count",
    "TextToSingleLineNode": "Text to Single Line",
    "AudioDurationNode": "Audio Duration"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
