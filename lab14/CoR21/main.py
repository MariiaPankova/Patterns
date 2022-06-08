from handler import *


def init_handlers() -> FileHandler:
    root_handler = JPG_Handler()

    root_handler.set_next(JPG_Handler()).set_next(
        PNG_Handler()
    ).set_next(DOCX_Handler()).set_next(
        DOCX_Handler()
    ).set_next(
        XLS_Handler()
    ).set_next(
        XLSX_Handler()
    ).set_next(
        PPTX_Handler()
    ).set_next(
        PDF_Handler()
    )
    return root_handler


if __name__ == '__main__':
    files = [
        "image.jpg",
        "image.png",
        "document.docx",
        "document.doc",
        "table.xls",
        "table.xlsx",
        "presentation.pptx",
        "document.pdf",
    ]
    root_handler = init_handlers()
    for file in files:
        root_handler.open(file)
