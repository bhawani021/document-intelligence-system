from dataclasses import dataclass
from pathlib import Path

import pymupdf
from docx import Document

from document_intelligence.extraction.text_cleaner import TextCleaner

@dataclass
class ExtractDocument:
    """ Stores extracted document content and its metadata"""
    filename: str
    file_type: str
    text: str
    page_count: int | None

class DocumentExtractor:
    """Extracts text from supported document formats: PDF, DOCX and TXT."""

    def __init__(self):
        self.text_cleaner = TextCleaner()

    def extract(self, file_path: str | Path) -> ExtractDocument:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        extension = path.suffix.lower()

        if extension == ".pdf":
            result = self._extract_pdf(path)
        elif extension == ".docx":
            result =  self._extract_docx(path)
        elif extension == ".txt":
            result =  self._extract_txt(path)
        else:
            raise ValueError(f"Unsupported file format: {extension}")

        result.text = self.text_cleaner.clean(result.text)

        return result

    def _extract_pdf(self, path: Path) -> ExtractDocument:

        with pymupdf.open(path) as pdf:
            text = "\n".join(page.get_text() for page in pdf)
            page_count = len(pdf)

        return ExtractDocument(
            filename=path.name,
            file_type="pdf",
            text=text,
            page_count=page_count,
        )

    def _extract_docx(self, path: Path) -> ExtractDocument:

        document = Document(path)

        text = "\n".join(
            paragraph.text for paragraph in document.paragraphs
        )

        return ExtractDocument(
            filename=path.name,
            file_type="docx",
            text=text,
            page_count=None,
        )

    def _extract_txt(self, path: Path) -> ExtractDocument:

        text = path.read_text(encoding="uft-8")

        return ExtractDocument(
            filename=path.name,
            file_type=".txt",
            text=text,
            page_count=None,
        )
