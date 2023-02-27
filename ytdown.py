stil_wants_to_continue = True

while stil_wants_to_continue:
    from pytube import YouTube
    import math
    import os

    # Input the YouTube video URL
    video_url = input("Enter the YouTube video URL: ")

    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the available video and audio streams and print their resolutions
        video_streams = yt.streams.filter(type="video", progressive=True)
        audio_streams = yt.streams.filter(type="audio")
        for i, stream in enumerate(video_streams):
            print(f"{i + 1}. Resolution: {stream.resolution}, File size: {math.floor(stream.filesize / pow(10, 6))} MB")
        for i, stream in enumerate(audio_streams):
            print(
                f"{i + len(video_streams) + 1}. Bitrate: {stream.abr}, File size: {math.floor(stream.filesize / pow(10, 6))} MB")

    except Exception as e:
        print("Error:", e)
        continue

    # Prompt the user to choose a resolution
    while True:
        choice = input("Enter the number of the stream you want to download: ")
        try:
            index = int(choice) - 1
            if index in range(len(video_streams) + len(audio_streams)):
                break
        except ValueError:
            pass
        print("Invalid choice. Try again.")

    # Ask the user to choose a directory
    while True:
        choice = input(
            "Enter the number of the directory to save the video:\n1. Desktop\n2. Downloads\n3. Music\n4. Videos\n")
        try:
            dir_index = int(choice)
            if dir_index in range(1, 5):
                break
        except ValueError:
            pass
        print("Invalid choice. Try again.")

    # Get the chosen directory
    global directory

    if dir_index == 1:
        directory = os.path.join(os.path.expanduser("C:/Users/Ankit/"), "Desktop")
    elif dir_index == 2:
        directory = os.path.join(os.path.expanduser("C:/Users/Ankit/"), "Downloads")
    elif dir_index == 3:
        directory = os.path.join(os.path.expanduser("C:/Users/Ankit/"), "Music")
    elif dir_index == 4:
        directory = os.path.join(os.path.expanduser("E:/"), "Videos")

    # Get the chosen stream and download the video
    if index < len(video_streams):
        stream = video_streams[index]
    else:
        stream = audio_streams[index - len(video_streams)]
    print("Downloading:", yt.title)
    video_size = stream.filesize

    stream.download(output_path=directory)

    # Display resolution and file size after downloading
    print(f"Resolution: {stream.resolution}, File size: {math.floor(video_size / pow(10, 6))} MB")

    print("Download complete!")
    print(directory)
    stii_download = input("would you like to download anything else \n 'y' or 'n'")
    if stii_download.lower() == "n":
        stil_wants_to_continue=False

