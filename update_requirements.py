import subprocess
import os

def upgrade_packages(requirements_file='requirements.txt'):
    if not os.path.exists(requirements_file):
        print(f"❌ File '{requirements_file}' not found.")
        return

    print("📦 Installing/upgrading packages...")
    with open(requirements_file, 'r') as file:
        packages = [line.strip().split('==')[0] for line in file if line.strip() and not line.startswith('#')]

    for package in packages:
        print(f"🔄 Upgrading {package}...")
        subprocess.run(['pip', 'install', '--upgrade', package])

    print("📌 Freezing new requirements...")
    with open(requirements_file, 'w') as file:
        result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE, text=True)
        file.write(result.stdout)

    print("✅ requirements.txt updated with latest versions.")

if __name__ == "__main__":
    upgrade_packages()


