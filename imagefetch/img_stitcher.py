import cv2
import os

def create_video(image_folder, video_filename, output_fps):
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg')])
    if not image_files:
        print("No image files found in the folder.")
        return

    # Get the first image to determine dimensions
    first_image = cv2.imread(os.path.join(image_folder, image_files[0]))
    height, width, _ = first_image.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_filename, fourcc, output_fps, (width, height))

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)
        if image is not None:
            out.write(image)
        else:
            print(f"Failed to read image: {image_path}")

    out.release()

def play_video(video_path):
        # Open the video file for reading
    video_filename = video_path  # Replace with your video filename
    cap = cv2.VideoCapture(video_filename)

    if not cap.isOpened():
        print("Error opening video file.")
        exit()

    while cap.isOpened():
        ret, frame = cap.read()  # Read a frame

        if not ret:
            break  # Break the loop if we reach the end of the video

        cv2.imshow('Frame', frame)  # Display the frame

        # Press 'q' to exit the loop
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()  # Release the video capture object
    cv2.destroyAllWindows()  # Close all OpenCV windows

if __name__ == "__main__":
    image_folder = '/Users/indiram/ASI/images/images2'
    video_filename = 'stitches/sunimagesstitched.avi'
    output_fps = 30  # Adjust the frames per second as needed
    create_video(image_folder, video_filename, output_fps)
    play_video(video_filename)
