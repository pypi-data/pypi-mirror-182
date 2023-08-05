import argparse
import os
import urllib.request

def hf_hub_url(repo_id, filename):
    return f"https://huggingface.co/{repo_id}/resolve/main/{filename}"

def main():
    # Parse the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_id", help="The repository ID of the model and filename on the Hugging Face Model Hub (eg. 'xihajun/roberta-base-chinese")
    parser.add_argument("--save-dir", help="The directory where the file should be saved")
    args = parser.parse_args()

    # Create the save directory if it does not exist
    if args.save_dir:
        if not os.path.exists(args.save_dir):
            os.makedirs(args.save_dir)

    # Download the model file
    firstSlashIdx = args.repo_id.find("/")
    repo = args.repo_id[0:firstSlashIdx]
    filename = args.repo_id[firstSlashIdx+1:]
    url = hf_hub_url(repo, filename)
    save_path = filename if not args.save_dir else os.path.join(args.save_dir, filename)
    urllib.request.urlretrieve(url, save_path)

if __name__ == "__main__":
    main()
