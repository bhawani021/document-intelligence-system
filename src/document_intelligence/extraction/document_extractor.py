from dataclasses import dataclass
from pathlib import Path

import pymupdf
from docx import Document


@dataclass
class ExtractDocument:
    """ Stores extracted document content and its metadata"""
    filename: str
    file_type: str
    text: str
    page_count: int | None

class DocumentExtractor:
    """Extracts text from supported document formats: PDF, DOCX and TXT."""

    def extract(self, file_path: str | Path) -> ExtractDocument:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        extension = path.suffix.lower()

        if extension == ".pdf":
            return self._extract_pdf(path)

        if extension == ".docx":
            return self._extract_docx(path)

        if extension == ".txt":
            return self._extract_txt(path)

        raise ValueError(f"Unsupported file format: {extension}")

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





