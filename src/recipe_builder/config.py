from pathlib import Path

# ---------------------------------------------------------------------
# Project Paths
# ---------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
PROMPTS_DIR = PROJECT_ROOT / "prompts"

EVALUATION_LOG_FILE = DATA_DIR / "evaluation_runs.jsonl"


# ---------------------------------------------------------------------
# Default LLM Configuration
# ---------------------------------------------------------------------

DEFAULT_LLM_PROVIDER = "ollama"
DEFAULT_MODEL = "qwen3:8b"

OLLAMA_TEMPERATURE = 0.5
OLLAMA_MAX_TOKENS = 1800