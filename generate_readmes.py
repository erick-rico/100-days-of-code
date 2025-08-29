import os

def generate_readme_for_day(day_path):
    day_name = os.path.basename(day_path)
    py_files = []
    ipynb_files = []
    other_files = []

    # Recorrer todas las subcarpetas
    for root, _, files in os.walk(day_path):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), day_path)
            if file.endswith('.py'):
                py_files.append(relative_path)
            elif file.endswith('.ipynb'):
                ipynb_files.append(relative_path)
            elif not file.endswith('.md'):  # evita meter el README mismo
                other_files.append(relative_path)

    # Ordenar listas
    py_files.sort()
    ipynb_files.sort()
    other_files.sort()

    readme_lines = [f"# {day_name}\n"]

    # Sección Python Files
    if py_files:
        readme_lines.append("## 📄 Python Files")
        for file in py_files:
            display_name = os.path.basename(file)
            readme_lines.append(f"- `{display_name}`")

    # Sección Notebook Files
    if ipynb_files:
        readme_lines.append("\n## 📓 Notebook Files")
        for file in ipynb_files:
            display_name = os.path.basename(file)
            readme_lines.append(f"- `{display_name}`")

    # Notas para Python y Notebooks
    readme_lines.append("\n## 📝 Notes")
    for file in py_files + ipynb_files + other_files:
        base_filename = os.path.basename(file)
        if base_filename.startswith("main"):
            note = f"- Solved the final project of the day: `{base_filename}`."
        elif base_filename.startswith("task"):
            note = f"- Solved a mini challenge of the day: `{base_filename}`."
        elif base_filename.startswith("capstone"):
            note = f"- Solved one of the capstone projects of the course: `{base_filename}`."
        elif base_filename.startswith("my"):
            note = f"- Created an extra version or experiment: `{base_filename}`."
        else:
            note = f"- Included utility or support file: `{base_filename}`."
        readme_lines.append(note)

    readme_content = "\n".join(readme_lines)

    with open(os.path.join(day_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

def generate_readmes_for_all_days(base_path="."):
    for entry in os.listdir(base_path):
        full_path = os.path.join(base_path, entry)
        if os.path.isdir(full_path) and entry.lower().startswith("day"):
            generate_readme_for_day(full_path)

if __name__ == "__main__":
    generate_readmes_for_all_days()
