import os
import glob
import subprocess

# Step 1: Extract all imports from Python files
def extract_imports(directory_path):
    imports = set()
    python_files = glob.glob(os.path.join(directory_path, '**', '*.py'), recursive=True)
    for file_path in python_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line.startswith('import ') or line.startswith('from '):
                    imports.add(line.split()[1].split('.')[0])  # Extract the module name
    return imports

# Step 2: Find unused libraries
def find_unused_libraries(requirements_path, imports):
    with open(requirements_path, 'r') as file:
        requirements = [line.strip() for line in file if line.strip()]
    return [lib.split('==')[0] for lib in requirements if lib.split('==')[0] not in imports]

# Step 3: Update the requirements.txt file
def update_requirements(requirements_path, unused_libraries):
    backup_path = f"{requirements_path}.backup"
    os.rename(requirements_path, backup_path)

    with open(backup_path, 'r') as original, open(requirements_path, 'w') as updated:
        for line in original:
            lib = line.strip().split('==')[0]
            if lib not in unused_libraries:
                updated.write(line)

    print(f"Updated {requirements_path}. Backup saved at {backup_path}.")

# Step 4: Uninstall unused libraries
def uninstall_unused_libraries(unused_libraries):
    for lib in unused_libraries:
        print(f"Uninstalling {lib}...")
        subprocess.run(["pip", "uninstall", "-y", lib], check=True)

# Main function to process a service
def process_service(service_name, requirements_path, code_directory):
    print(f"Processing {service_name}...")
    imports = extract_imports(code_directory)
    unused_libraries = find_unused_libraries(requirements_path, imports)

    if unused_libraries:
        print(f"Found {len(unused_libraries)} unused libraries in {service_name}: {unused_libraries}")
        update_requirements(requirements_path, unused_libraries)
        uninstall_unused_libraries(unused_libraries)
    else:
        print(f"No unused libraries found in {service_name}.")

# Run the script for each service
if __name__ == "__main__":
    services = {
        "api_gateway": {
            "requirements": "./api_gateway/requirements.txt",
            "code_directory": "./api_gateway/"
        },
        "order_service": {
            "requirements": "./order_service/requirements.txt",
            "code_directory": "./order_service/"
        },
        "product_service": {
            "requirements": "./product_service/requirements.txt",
            "code_directory": "./product_service/"
        }
    }

    for service, paths in services.items():
        process_service(service, paths["requirements"], paths["code_directory"])