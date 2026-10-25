# storage_estimator.py
# Estimates how much storage is needed for a number of files.

def main():
    print("=== Storage Estimator ===")
    num_files = int(input("Number of files: "))
    size_mb = float(input("Average size of one file (MB): "))
    total_mb = num_files * size_mb
    size_gb = size_mb / 1024
    print("Size in GB:", size_gb)
    print("Total storage needed:", total_mb, "MB")
    print("Hello, this is a storage estimator program.")

main()