import re

class TextCleaner:

    def clean(self, text: str) -> str:
        """Normalize extracted text by removing unnecessary whitespace."""
        # Normalize line endings
        text = text.replace("\n\r", "\n").replace("\r", "\n")

        # Remove null characters
        text = text.replace("\x00", "")

        # replace multiple spaces and tabs with a single space
        text = re.sub(r"[ \t]+", " ", text)

        # Remove spaces around newlines
        text = re.sub(r" *\n *", "\n", text)

        # Remove three or more consecutive new lines with two
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()

