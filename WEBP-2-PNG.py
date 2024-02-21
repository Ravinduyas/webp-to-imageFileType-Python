from tkinter import Tk, Label, Button, filedialog
from PIL import Image

class WebpToPngConverter:
    def __init__(self, master):
        self.master = master
        master.title("WebP to PNG Converter")

        self.label = Label(master, text="Select WebP file:")
        self.label.pack()

        self.convert_button = Button(master, text="Convert", command=self.convert)
        self.convert_button.pack()

    def convert(self):
        webp_file_path = filedialog.askopenfilename(
            title="Select a WebP file",
            filetypes=[("WebP files", "*.webp"), ("All files", "*.*")]
        )

        if webp_file_path:
            png_file_path = filedialog.asksaveasfilename(
                title="Save as PNG",
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
            )

            if png_file_path:
                try:
                    with Image.open(webp_file_path) as webp_image:
                        webp_image.save(png_file_path, 'PNG')
                    print(f"Conversion successful: {webp_file_path} -> {png_file_path}")
                except Exception as e:
                    print(f"Error converting {webp_file_path} to {png_file_path}: {e}")

if __name__ == "__main__":
    root = Tk()
    app = WebpToPngConverter(root)
    root.mainloop()
