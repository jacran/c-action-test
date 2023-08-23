import os, subprocess

# Settings
TEST_DIR = "/tests"
CODE_FILE = "main.c"
COMPILE_TIMEOUT = 10.0
RUN_TIMEOUT = 10.0

# Create absolute path
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

print("Building")
try:
    ret = subprocess.run(["gcc", code_path, "-o", app_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=COMPILE_TIMEOUT)
except Exception as e:
    print(f"ERROR: Compilation failed: {str(e)}")

#Parse output
output = ret.stdout.decode('utf-8')
print(output)
output = ret.stderr.decode('utf-8')
print(output)

if ret.returncode != 0:
    print("Compilation failed")
    exit(1)

print("Running...")

try:
    ret = subprocess.run([app_path], stdout=subprocess.PIPE, timeout=RUN_TIMEOUT)
except Exception as e:
    print(f"ERROR: Run failed: {str(e)}")

#Parse output
output = ret.stdout.decode('utf-8')
print(f"Output: {output}")

print(f"All tests passed")
exit(0)