import os

def generate_readme_for_day(day_path):
    day_name = os.path.basename(day_path)
    py_files = [f for f in os.listdir(day_path) if f.endswith('.py')]

    readme_lines = [f"# {day_name}\n", "## 📄 Python Files"]
    for file in py_files:
        readme_lines.append(f"- `{file}`")

    readme_lines.append("\n## 📝 Notes")
    for file in py_files:
        if file.startswith("task"):
            note = f"- Solved the main task: `{file}`."
        elif file.startswith("my"):
            note = f"- Created an extra version or experiment: `{file}`."
        else:
            note = f"- Included utility or support file: `{file}`."
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
