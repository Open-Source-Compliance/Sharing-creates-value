#!/usr/bin/env python3
"""
NotebookLM Slideshow Generator

Creates a new NotebookLM notebook, adds sources from the sources/ directory,
and generates a slideshow based on prompt.txt.
"""

import json
import os
import subprocess
import sys
import time
import tempfile
from pathlib import Path
from typing import Optional


SOURCES_DIR = Path(__file__).parent / "sources"
SOURCES_JSON = SOURCES_DIR / "sources.json"
PROMPT_FILE = SOURCES_DIR / "prompt.txt"
OUTPUT_PDF = Path(__file__).parent / "Generated_Presentation.pdf"

NOTEBOOK_TITLE = "OpenChain AI Data Platform"
SOURCE_TIMEOUT = 600
ARTIFACT_TIMEOUT = 1800


def run_notebooklm(args: list[str], check: bool = True, capture_output: bool = True) -> subprocess.CompletedProcess:
    cmd = ["notebooklm"] + args
    result = subprocess.run(
        cmd,
        capture_output=capture_output,
        text=True
    )
    if check and result.returncode != 0:
        print(f"Error running command: {' '.join(cmd)}", file=sys.stderr)
        print(f"stdout: {result.stdout}", file=sys.stderr)
        print(f"stderr: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return result


def load_json(filepath: Path) -> dict:
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def get_prompt() -> str:
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()


def wait_for_all_sources(notebook_id: str, timeout: int = SOURCE_TIMEOUT) -> bool:
    print(f"Waiting for all sources in notebook to be ready...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        result = run_notebooklm(["source", "list", "--json", "-n", notebook_id])
        data = json.loads(result.stdout)
        sources = data.get("sources", [])
        
        if not sources:
            print("No sources found in notebook")
            time.sleep(15)
            continue
        
        sources_status = {s["id"]: s.get("status", "unknown") for s in sources}
        
        all_ready = True
        for sid, status in sources_status.items():
            if status != "ready":
                all_ready = False
                print(f"  Source {sid[:8]}... status: {status}")
        
        if all_ready:
            print(f"All {len(sources)} sources are ready!")
            return True
        
        print(f"Waiting for sources to process... ({len([s for s in sources_status.values() if s == 'ready'])}/{len(sources)} ready)")
        time.sleep(15)
    
    print(f"Timeout waiting for sources after {timeout}s", file=sys.stderr)
    return False


def wait_for_artifact(notebook_id: str, artifact_id: str, timeout: int = ARTIFACT_TIMEOUT) -> bool:
    print(f"Waiting for artifact {artifact_id[:8]}... to complete...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        result = run_notebooklm(["artifact", "list", "--json", "-n", notebook_id])
        data = json.loads(result.stdout)
        artifacts = data.get("artifacts", [])
        
        for art in artifacts:
            if art["id"] == artifact_id:
                status = art.get("status", "unknown")
                print(f"  Artifact status: {status}")
                if status == "completed":
                    return True
                if status in ("failed", "unknown"):
                    print(f"Artifact generation failed: {status}", file=sys.stderr)
                    return False
        
        print("Waiting for artifact to complete...")
        time.sleep(30)
    
    print(f"Timeout waiting for artifact after {timeout}s", file=sys.stderr)
    return False


def add_source(notebook_id: str, source_info: dict, source_content: str) -> Optional[str]:
    source_id = source_info["id"]
    source_type = source_info.get("type", "")
    url = source_info.get("url")
    
    if "WEB_PAGE" in source_type and url:
        print(f"  Adding web source: {url[:60]}...")
        result = run_notebooklm(["source", "add", url, "--json", "-n", notebook_id])
        data = json.loads(result.stdout)
        return data.get("source_id")
    else:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as tmp:
            tmp.write(source_content)
            tmp_path = tmp.name
        
        try:
            print(f"  Adding pasted text source: {source_info.get('title', 'untitled')[:40]}...")
            result = run_notebooklm(["source", "add", tmp_path, "--json", "-n", notebook_id])
            data = json.loads(result.stdout)
            return data.get("source_id")
        finally:
            os.unlink(tmp_path)


def main():
    print("=" * 60)
    print("NotebookLM Slideshow Generator")
    print("=" * 60)
    
    if not SOURCES_JSON.exists():
        print(f"Error: {SOURCES_JSON} not found", file=sys.stderr)
        sys.exit(1)
    
    if not PROMPT_FILE.exists():
        print(f"Error: {PROMPT_FILE} not found", file=sys.stderr)
        sys.exit(1)
    
    print("\n[1/6] Loading sources from sources.json...")
    sources_data = load_json(SOURCES_JSON)
    source_list = sources_data.get("sources", [])
    print(f"Found {len(source_list)} sources")
    
    print(f"\n[2/6] Creating notebook '{NOTEBOOK_TITLE}'...")
    result = run_notebooklm(["create", NOTEBOOK_TITLE, "--json"])
    notebook_data = json.loads(result.stdout)
    notebook_id = notebook_data.get("id")
    print(f"Created notebook: {notebook_id}")
    
    print(f"\n[3/6] Adding sources to notebook...")
    for i, source_info in enumerate(source_list, 1):
        source_file = SOURCES_DIR / f"{source_info['id']}.json"
        if not source_file.exists():
            print(f"  Warning: Source file not found: {source_file}, skipping")
            continue
        
        source_json = load_json(source_file)
        source_content = source_json.get("content", "")
        
        added_id = add_source(notebook_id, source_info, source_content)
        if added_id:
            print(f"    Added source {i}/{len(source_list)}")
        else:
            print(f"    Failed to add source {i}/{len(source_list)}")
        
        time.sleep(2)
    
    print(f"\nAdded all sources")
    
    if not wait_for_all_sources(notebook_id):
        print("Warning: Not all sources ready, continuing anyway...")
    
    print(f"\n[4/6] Generating slideshow (this may take 5-15 minutes)...")
    prompt = get_prompt()
    
    max_retries = 2
    retry_delay = 300
    artifact_id = None
    
    for attempt in range(max_retries + 1):
        if attempt > 0:
            print(f"Retry {attempt}/{max_retries} after {retry_delay}s...")
            time.sleep(retry_delay)
        
        cmd = f"notebooklm generate slide-deck --json -n {notebook_id} -- {repr(prompt)}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            try:
                task_data = json.loads(result.stdout)
                artifact_id = task_data.get("artifact_id") or task_data.get("task_id")
                if artifact_id:
                    break
            except json.JSONDecodeError:
                pass
        
        if "rate" in result.stderr.lower() or "limit" in result.stderr.lower():
            print(f"Rate limited, retrying...")
            continue
        
        print(f"Error: {result.stderr}", file=sys.stderr)
        if attempt == max_retries:
            sys.exit(1)
    
    if not artifact_id:
        print(f"Error: No artifact_id in response: {result.stdout}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Generated artifact: {artifact_id}")
    
    if not wait_for_artifact(notebook_id, artifact_id):
        print("Error: Artifact generation failed or timed out", file=sys.stderr)
        sys.exit(1)
    
    print(f"\n[5/6] Downloading PDF to {OUTPUT_PDF}...")
    result = run_notebooklm([
        "download", "slide-deck",
        str(OUTPUT_PDF),
        "-a", artifact_id,
        "-n", notebook_id
    ])
    
    print(f"\n[6/6] Complete!")
    print(f"PDF saved to: {OUTPUT_PDF.absolute()}")
    
    if OUTPUT_PDF.exists():
        size = OUTPUT_PDF.stat().st_size
        print(f"File size: {size:,} bytes")


if __name__ == "__main__":
    main()