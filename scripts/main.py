from processor import process_data
from uploader import upload_to_drive

def run_pipeline():
    output = process_data()

    if output:
        upload_to_drive(output)
    else:
        print(" Nothing processed")

def run_pipeline():
    output = process_data()

    print("OUTPUT FILE:", output)   # 👈 ADD THIS

    if output:
        upload_to_drive(output)
    else:
        print("Nothing processed")

if __name__ == "__main__":
    run_pipeline()