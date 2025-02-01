import io
from PIL import Image
import cairosvg
import torch
import numpy as np
from typing import Tuple

class SVGPreview:
    """Processes a single SVG string and returns a PyTorch image tensor."""

    @classmethod
    def INPUT_TYPES(cls):
        """Defines the required input parameters."""
        return {
            "required": {
                "svg_input": ("STRING", {"multiline": False, "default": ""})  # Single SVG input
            }
        }

    # Define widgets for inline UI configuration
    WIDGETS = {
        "width": ("INT", {"default": 100, "min": 16, "max": 2048}),
        "height": ("INT", {"default": 100, "min": 16, "max": 2048}),
        "transparency": ("BOOLEAN", {"default": True})
    }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "preview_svg"
    CATEGORY = "💎TOSVG"

    def svg_string_to_image(self, svg_string: str, width: int, height: int, transparency: bool) -> Image.Image:
        """Converts an SVG string to a PIL Image with widget-defined dimensions and transparency."""
        svg_bytes = svg_string.encode('utf-8')

        if not transparency:
            png_data = cairosvg.svg2png(bytestring=svg_bytes, output_width=width, output_height=height, background_color='white')
        else:
            png_data = cairosvg.svg2png(bytestring=svg_bytes, output_width=width, output_height=height)

        image = Image.open(io.BytesIO(png_data))
        return image.convert("RGBA") if transparency else image.convert("RGB")

    def pil2tensor(self, image: Image.Image) -> torch.Tensor:
        """Converts a PIL Image to a PyTorch tensor in (C, H, W) format."""
        image_np = np.array(image).astype(np.float32) / 255.0
        tensor = torch.from_numpy(image_np)

        # Ensure correct shape: (C, H, W)
        if tensor.ndimension() == 3:
            tensor = tensor.permute(2, 0, 1)  # Moves channel dimension to first

        return tensor.unsqueeze(0)  # Add batch dimension (1, C, H, W)

    def preview_svg(self, svg_input: str, width: int, height: int, transparency: bool) -> Tuple[torch.Tensor]:
        """Generates an image preview from a single SVG string."""
        if not svg_input.strip():
            raise ValueError("SVG input is empty!")

        image = self.svg_string_to_image(svg_input, width=width, height=height, transparency=transparency)
        tensor_image = self.pil2tensor(image)

        return (tensor_image,)
