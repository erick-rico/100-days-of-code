import os

def generate_readme_for_day(day_path):
    day_name = os.path.basename(day_path)
    py_files = []
    # Usar os.walk para recorrer todas las subcarpetas
    for root, _, files in os.walk(day_path):
        for file in files:
            if file.endswith('.py'):
                # Almacena la ruta relativa del archivo para que el README sea más claro
                relative_path = os.path.relpath(os.path.join(root, file), day_path)
                py_files.append(relative_path)
    
    # Ordenar los archivos para una salida consistente
    py_files.sort() 

    readme_lines = [f"# {day_name}\n", "## 📄 Python Files"]
    for file in py_files:
        # Asegúrate de que el formato sea legible, usando el nombre del archivo o la ruta si es necesario
        display_name = os.path.basename(file) # Puedes usar 'file' completo si prefieres la ruta relativa
        readme_lines.append(f"- `{display_name}`") # O f"- `{file}`" si quieres la ruta completa

    readme_lines.append("\n## 📝 Notes")
    for file in py_files:
        # Asegúrate de usar solo el nombre del archivo para la lógica de las notas
        base_filename = os.path.basename(file)
        if base_filename.startswith("task"):
            note = f"- Solved the main task: `{base_filename}`."
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