Those are the sources for the presentation I generated using Googles NotebookLM based on the opensource release files (snapshotted in sources) and a prompt (sources/prompt.txt). 

## Automated Slideshow Generator

This project includes a Python script (`main.py`) that automates the entire NotebookLM slideshow generation process.

### Prerequisites

1. **Install notebooklm-py CLI:**
   ```bash
   pip install notebooklm-py
   ```

2. **Authenticate with Google:**
   ```bash
   notebooklm login
   ```

### Running the Script

```bash
python main.py
```

### What the Script Does

1. **Loads sources** from `sources/sources.json`
2. **Creates a new notebook** titled "OpenChain AI Data Platform"
3. **Adds all 12 sources** - web URLs are added directly, pasted text sources are created as temporary files
4. **Waits for source processing** - polls until all sources are indexed (up to 10 minutes)
5. **Generates slideshow** - uses the prompt from `sources/prompt.txt` (includes retry on rate limiting)
6. **Waits for generation** - polls until the slide deck is ready (may take 5-15 minutes)
7. **Downloads PDF** - saves to `Generated_Presentation.pdf`

### Output

- `Generated_Presentation.pdf` - The final slideshow

### Configuration

You can modify these constants in `main.py`:

| Variable | Default | Description |
|----------|---------|-------------|
| `NOTEBOOK_TITLE` | "OpenChain AI Data Platform" | Notebook title |
| `SOURCE_TIMEOUT` | 600 | Max wait for sources (seconds) |
| `ARTIFACT_TIMEOUT` | 1800 | Max wait for generation (seconds) |
| `OUTPUT_PDF` | `./Generated_Presentation.pdf` | Output file path |

## LICENSE 
The sources from the AI Alliance project are Apache 2.0 Licensed (or compatible). The AI Alliance Logo is trademarked by the AI Alliance. The NotebookLM Logo is a Google trademark.

My Prompt is CC-0 licenced and according to Google's TOS the generated content should also thus be CC-0 licenced.
