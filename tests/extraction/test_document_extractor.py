import pytest

from document_intelligence.extraction.document_extractor import (
    DocumentExtractor,
)

def test_extract_txt(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello Document AI", encoding="uft-8")

    result = DocumentExtractor().extract(file_path)

    assert result.filename == "sample.txt"
    assert result.file_type == "txt"
    assert result.text == "Hello Document AI"
    assert result.page_count is None

def test_unsupported_file():
    with pytest.raises(ValueError):
        DocumentExtractor().extract("sample.xlsx")

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        DocumentExtractor.extract("missing.txt")
