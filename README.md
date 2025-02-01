# 🖼️ SVG Preview Node

This project provides a **custom node** that converts an SVG string into an image tensor using **CairoSVG**, **Pillow (PIL)**, and **PyTorch**. The node includes **inline widgets** to set image width, height, and transparency.

---

## 📦 Requirements

Ensure you have the required dependencies installed:

```sh
pip install -r requirements.txt
```

**Dependencies:**
- [`Pillow`](https://pillow.readthedocs.io/en/stable/) - Image processing
- [`cairosvg`](https://cairosvg.org/) - Converts SVG to PNG
- [`torch`](https://pytorch.org/) - PyTorch for tensor handling
- [`numpy`](https://numpy.org/) - Efficient array operations

---

## 🚀 Usage

This node allows you to convert an **SVG string** into an image tensor. The following features are available:

✅ Accepts **a single SVG string**  
✅ Uses **widgets** for `width`, `height`, and `transparency`  
✅ Outputs a **PyTorch tensor** in the format `(1, C, H, W)`  

---

## 🛠️ Code Overview

### **Class: `SVGPreview`**
- **Inputs:**  
  - `svg_input` (string) - The SVG code  
- **Widgets:**  
  - `width` (int) - Set via UI (default: `100`)  
  - `height` (int) - Set via UI (default: `100`)  
  - `transparency` (bool) - Set via UI (default: `True`)  
- **Outputs:**  
  - A **PyTorch tensor** representing the image  

### **Functions**
- `svg_string_to_image(svg_string, width, height, transparency)`:  
  Converts an SVG string to a PIL image.
- `pil2tensor(image)`:  
  Converts a PIL image to a PyTorch tensor.
- `preview_svg(svg_input)`:  
  The main function that processes the SVG and returns a tensor.

---

## 📜 Example

Here’s an example of how you can use this node:

```python
svg_code = "<svg width='100' height='100'><circle cx='50' cy='50' r='40' fill='blue'/></svg>"

node = SVGPreview()
image_tensor = node.preview_svg(svg_code)
print(image_tensor.shape)  # Output: (1, 4, 100, 100) for RGBA image
```

---

## 📝 Notes
- If `transparency` is **enabled**, the image will be in **RGBA** format.
- If `transparency` is **disabled**, the image will be converted to **RGB** with a white background.
- The output tensor follows the format **(1, C, H, W)** where:
  - `1` = Batch size
  - `C` = Channels (3 for RGB, 4 for RGBA)
  - `H` = Height
  - `W` = Width

---

## 📌 License
This project is released under the **MIT License**.

---

## 💡 Future Enhancements
- [ ] Add support for **SVG file input** (instead of just raw strings).  
- [ ] Improve error handling for **invalid SVGs**.  
- [ ] Add **GPU acceleration** for faster tensor operations.  

---

🚀 **Happy Coding!** 🎨🔥  
