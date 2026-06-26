from pathlib import Path


class PromptRegistry:
    _PROMPT_DIR = Path(__file__).parent / "versions"

    @classmethod
    def load(cls, version: str) -> str:
        prompt_file = cls._PROMPT_DIR / f"{version}.txt"

        if not prompt_file.exists():
            raise FileNotFoundError(
                f"Prompt version '{version}' not found."
            )

        return prompt_file.read_text(encoding="utf-8")