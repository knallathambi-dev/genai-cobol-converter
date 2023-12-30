from pathlib import Path
from pylint.lint.run import Run
from black import format_str
from black import Mode

def lint_code(file: Path):
    parent = file.parent
    file_name = file.stem
    output_file = parent / f"{file_name}_lint.txt"
    Run([f"--output={output_file}", file.as_posix()], exit=False)

def format_file(file: Path) -> str:
    assert file is not None
    text = file.read_text()
    formatted = format_str(text, mode=Mode())
    file.write_text(formatted, encoding="utf-8")
    return formatted

if __name__ == '__main__':
    file_path = Path('output/OpenAI_20231230154915/PINVRPT/PINVRPT__conv_python_1.py')
    format_file(file_path)
    lint_code(file_path)
