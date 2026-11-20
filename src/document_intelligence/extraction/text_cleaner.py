
import re


class TextCleaner:

    def clean(self, text: str) -> str:
        """Normalize extracted text by removing unnecessary whitespace."""
        # Normalize line endings
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        # Remove null characters
        text = text.replace("\x00", "")

        # Replace multiple spaces and tabs with a single space
        text = re.sub(r"[ \t]+", " ", text)

        # Remove spaces around newlines
        text = re.sub(r" *\n *", "\n", text)

        # Replace three or more consecutive newlines with two
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()
