import qrcode


class MyQr:
    def __init__(self, size: int = 30, padding: int = 2):

        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str = "black", bg: str = "white"):

        user_input = input("Enter text to encode in the QR code: ")

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
            print(f"Successfully created QR code! Saved as '{file_name}'")
        except Exception as e:
            print(f"Error generating QR code: {e}")


def get_user_input() -> tuple:
    size_qr = get_integer_input("Enter size (default 30): ", default_value=30)
    size_padding = get_integer_input("Enter padding (default 2): ", default_value=2)

    fg_color = input("Enter foreground color (default black): ").strip() or "black"
    bg_color = input("Enter background color (default white): ").strip() or "white"

    return size_qr, size_padding, fg_color, bg_color


def get_integer_input(prompt: str, default_value: int) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"Invalid input. Using default value: {default_value}")
            return default_value


def main() -> None:
    size_qr, size_padding, fg_color, bg_color = get_user_input()
    myqr = MyQr(size=size_qr, padding=size_padding)
    myqr.create_qr(file_name="qrcode.png", fg=fg_color, bg=bg_color)


if __name__ == "__main__":
    main()
