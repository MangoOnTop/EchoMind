"""
EchoMind Executable Builder
Compiles EchoMind into a standalone Windows .exe using PyInstaller.

Usage:
    python build_exe.py
"""
import sys
import os
import subprocess

def main():
    print("=" * 60)
    print("  EchoMind - Windows Executable Builder (.exe)")
    print("=" * 60)

    # 1. Check if PyInstaller is available
    try:
        import PyInstaller
        print("[✓] PyInstaller is installed.")
    except ImportError:
        print("[!] PyInstaller is not installed.")
        print("[*] Installing PyInstaller...")
        ret = subprocess.call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        if ret != 0:
            print("[X] Failed to install PyInstaller automatically.")
            print("    Please run: pip install pyinstaller")
            return 1

    # 2. Project root & target script
    project_root = os.path.dirname(os.path.abspath(__file__))
    target_script = os.path.join(project_root, "gui.py")
    exe_name = "EchoMind"

    print(f"\n[*] Compiling '{target_script}' -> '{exe_name}.exe'...")

    # 3. Build command
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--noconsole",                # Hide terminal window on launch
        "--onefile",                  # Single standalone executable
        "--name", exe_name,           # Output name: EchoMind.exe
        "--clean",                    # Clean cache before build
        "--paths", project_root,      # Include project root in module search path
        target_script
    ]

    print(f"[*] Running: {' '.join(cmd)}\n")
    result = subprocess.call(cmd, cwd=project_root)

    if result == 0:
        dist_path = os.path.join(project_root, "dist", f"{exe_name}.exe")
        print("\n" + "=" * 60)
        print("  BUILD SUCCESSFUL!")
        print("=" * 60)
        print(f"Your executable is ready at:")
        print(f"  --> {dist_path}")
        print("\nYou can double-click EchoMind.exe to run the application anywhere!")
    else:
        print("\n[X] Build failed with exit code:", result)

    return result

if __name__ == "__main__":
    sys.exit(main())
