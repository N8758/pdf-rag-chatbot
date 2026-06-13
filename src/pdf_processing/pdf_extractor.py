import fitz  


class PDFExtractor:

    @staticmethod
    def extract_text(pdf_path):
        document = fitz.open(pdf_path)

        pages = []

        for page_num in range(len(document)):
            page = document.load_page(page_num)

            text = page.get_text()

            pages.append({
                "page_number": page_num + 1,
                "text": text
            })

        document.close()

        return pages