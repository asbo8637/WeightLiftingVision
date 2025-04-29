import os
import subprocess

# Set the folder path where your videos are located
VIDEO_FOLDER = "./videos/wide_left"  # Change this to your folder path
OUTPUT_PREFIX = "flipped_"  # Prefix instead of suffix

# Supported video file extensions
VIDEO_EXTENSIONS = (".mp4", ".mov", ".avi", ".mkv", ".flv")

def flip_video(input_path, output_path):
    command = [
        "ffmpeg", "-i", input_path,
        "-vf", "hflip",
        "-c:a", "copy",  # copy audio without re-encoding
        output_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    for filename in os.listdir(VIDEO_FOLDER):
        if filename.lower().endswith(VIDEO_EXTENSIONS):
            input_path = os.path.join(VIDEO_FOLDER, filename)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(VIDEO_FOLDER, f"{OUTPUT_PREFIX}{name}{ext}")
            print(f"Flipping {filename} -> {os.path.basename(output_path)}")
            flip_video(input_path, output_path)

if __name__ == "__main__":
    main()
