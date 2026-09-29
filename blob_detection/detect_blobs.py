from pathlib import Path

import cv2


# 1. Find the images and make a folder for our results.
folder = Path(__file__).resolve().parent
output_folder = folder / "simple_results"
output_folder.mkdir(exist_ok=True)

image_names = ["polka_dots_1.png", "polka_dots_2.jpg", "polka_dots_3.jpg"]

# 2. Set up the blob detector.
params = cv2.SimpleBlobDetector_Params()
params.minThreshold = 10
params.maxThreshold = 255
params.thresholdStep = 5

# Filter by size. Change minArea to 5000 to keep only larger dots.
params.filterByArea = True
params.minArea = 60
params.maxArea = 25000

# Look for round blobs.
params.filterByCircularity = True
params.minCircularity = 0.65
params.filterByConvexity = True
params.minConvexity = 0.85
params.filterByInertia = True
params.minInertiaRatio = 0.5

# Allow both light and dark dots.
params.filterByColor = False

detector = cv2.SimpleBlobDetector_create(params)

# 3. Repeat the same steps for each image.
for image_name in image_names:
    image = cv2.imread(str(folder / "images" / image_name))

    if image is None:
        print("Could not open:", image_name)
        continue

    # Convert to gray and smooth out some of the image texture.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Find the blobs and draw red circles around them.
    blobs = detector.detect(gray)
    result = cv2.drawKeypoints(
        image, blobs, None, (0, 0, 255),
        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )

    print(image_name, "- blobs found:", len(blobs))

    # Save the picture so we can open it after the script finishes.
    saved = cv2.imwrite(str(output_folder / image_name), result)
    if not saved:
        print("Could not save:", image_name)

print("Results folder:", output_folder)
