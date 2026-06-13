import fitz
import pytesseract
from PIL import Image
import io


class OCRProcessor:

    @staticmethod
    def extract_text_from_scanned_pdf(pdf_path):

        document = fitz.open(pdf_path)

        extracted_pages = []

        for page_num in range(len(document)):

            page = document.load_page(page_num)

            pix = page.get_pixmap()

            image_bytes = pix.tobytes("png")

            image = Image.open(io.BytesIO(image_bytes))

            text = pytesseract.image_to_string(image)

            extracted_pages.append({
                "page_number": page_num + 1,
                "text": text
            })

        document.close()

        return extracted_pages