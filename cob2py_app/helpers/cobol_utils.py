def format_cobol_source(file_path:str):
    with open(file_path) as f:
        cobol_source = f.read()    
    lines = cobol_source.split('\n')
    fmt_lines = []
    for line in lines:
        # Ignore comment lines
        if line[6:7] == '*':
            continue
        fmt_lines.append(
            line[6:72].rstrip()
        )
    return "\n".join(fmt_lines)