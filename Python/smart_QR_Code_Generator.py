import qrcode
from PIL import Image

def generate_custom_qr(data, fill_color="black", back_color="white", logo_path=None):
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1-40, 1 being smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # H for high error correction (30% error tolerance)
        box_size=10,  # Size of each box
        border=4  # Thickness of the border
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
    
    # Optionally add logo to the center
    if logo_path:
        logo = Image.open(logo_path)
        logo = logo.resize((img.size[0] // 5, img.size[1] // 5))  # Adjust logo size
        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos)

    img.save("custom_qrcode.png")
    print("QR code generated and saved as 'custom_qrcode.png'")

if __name__ == "__main__":
    data = input("Enter the data/URL to encode into a QR code: ")
    fill_color = input("Enter the fill color (default is black): ") or "black"
    back_color = input("Enter the background color (default is white): ") or "white"
    logo_path = input("Enter the path to a logo image (optional): ") or None

    generate_custom_qr(data, fill_color, back_color, logo_path)
