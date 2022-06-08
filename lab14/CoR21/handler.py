from abc import ABC, abstractmethod
import os.path as osp


class BaseHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def open(self, file_name) -> None:
        if self.next_handler is not None:
            self.next_handler.open(file_name)

    def set_next(self, handler):
        print(f"{handler.__class__.__name__} is queued after {self.__class__.__name__}")
        self.next_handler = handler
        return handler


class FileHandler(BaseHandler, ABC):
    @classmethod
    @property
    @abstractmethod
    def supported(cls):
        pass

    def open(self, file_name):
        extension = osp.splitext(file_name)[-1]
        if extension == f".{self.supported}":
            print(f"{self.__class__.__name__} is opening {file_name}.")
        else:
            print(
                f"{self.__class__.__name__} not supported extension {extension} passing to next handler."
            )
            super().open(file_name)


class DOC_Handler(FileHandler):
    supported = "doc"


class DOCX_Handler(FileHandler):
    supported = "docx"


class PDF_Handler(FileHandler):
    supported = "pdf"


class JPG_Handler(FileHandler):
    supported = "jpg"


class PNG_Handler(FileHandler):
    supported = "png"


class PPTX_Handler(FileHandler):
    supported = "pptx"


class XLS_Handler(FileHandler):
    supported = "xls"


class XLSX_Handler(FileHandler):
    supported = "xlsx"

