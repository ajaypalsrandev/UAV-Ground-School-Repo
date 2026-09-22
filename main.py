from pathlib import Path

import cv2


# 1. Ask the user which image to process.
project_folder = Path(__file__).resolve().parent

entered_path = input(
    "Enter an image path, such as images/test.jpg: "
).strip()

image_path = Path(entered_path).expanduser()

# Interpret relative paths starting from the project folder.
if not image_path.is_absolute():
    image_path = project_folder / image_path

image = cv2.imread(str(image_path))

if image is None:
    raise SystemExit(f"Could not open image: {image_path}")


# 2. Convert the image to HSV.
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# 3. Define the HSV ranges for each color.
color_ranges = {
    "red": [
        ((0, 80, 50), (10, 255, 255)),
        ((170, 80, 50), (179, 255, 255)),
    ],
    "orange": [
        ((11, 80, 50), (24, 255, 255)),
    ],
    "yellow": [
        ((25, 80, 50), (34, 255, 255)),
    ],
    "green": [
        ((35, 80, 50), (85, 255, 255)),
    ],
    "blue": [
        ((86, 80, 50), (130, 255, 255)),
    ],
    "purple_pink": [
        ((131, 80, 50), (169, 255, 255)),
    ],
    "white": [
        ((0, 0, 200), (179, 79, 255)),
    ],
    "gray": [
        ((0, 0, 50), (179, 79, 199)),
    ],
    "black": [
        ((0, 0, 0), (179, 255, 49)),
    ],
}

# 4. Create a folder for the results.
output_folder = project_folder / "output"
output_folder.mkdir(exist_ok=True)

# 5. Display the original image.
cv2.namedWindow("Original image", cv2.WINDOW_NORMAL)
cv2.imshow("Original image", image)

# 6. Process each color.
for color_name, ranges in color_ranges.items():

    mask = cv2.inRange(hsv, (0, 0, 0), (0, 0, 0))
    mask[:] = 0

    for lower_bound, upper_bound in ranges:
        partial_mask = cv2.inRange(hsv, lower_bound, upper_bound)
        mask = cv2.bitwise_or(mask, partial_mask)

    pixel_count = cv2.countNonZero(mask)

    if pixel_count == 0:
        continue

    color_image = cv2.bitwise_and(image, image, mask=mask)

    print(f"{color_name}: {pixel_count} pixels")

    image_saved = cv2.imwrite(
        str(output_folder / f"{color_name}.png"),
        color_image,
    )

    mask_saved = cv2.imwrite(
        str(output_folder / f"{color_name}_mask.png"),
        mask,
    )

    if not image_saved or not mask_saved:
        raise SystemExit(f"Could not save results for {color_name}")

    cv2.namedWindow(color_name, cv2.WINDOW_NORMAL)
    cv2.imshow(color_name, color_image)


print(f"Results saved to: {output_folder}")
print("Click an image window and press any key to close the windows.")

cv2.waitKey(0)
cv2.destroyAllWindows()