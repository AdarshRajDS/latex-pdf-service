def sanitize_latex(content: str) -> str:
    forbidden = ["\\write18", "\\input|", "\\include|", "\\openout", "\\write"]

    for token in forbidden:
        if token in content:
            raise ValueError("Unsafe LaTeX detected")

    return content
