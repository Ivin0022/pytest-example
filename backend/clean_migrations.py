import os

PROJECT_DIR = os.getcwd()  # Run this script from the root directory

def delete_migration_files(app_dir):
    migrations_path = os.path.join(PROJECT_DIR, app_dir, "migrations")
    if os.path.exists(migrations_path):
        for filename in os.listdir(migrations_path):
            if filename != "__init__.py" and filename.endswith(".py"):
                file_path = os.path.join(migrations_path, filename)
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            elif filename.endswith(".pyc"):
                os.remove(os.path.join(migrations_path, filename))

# List your Django apps here
APPS = ["tracker", "users"]

for app in APPS:
    delete_migration_files(app)

print("\n✅ Migration files (except __init__.py) removed.")
