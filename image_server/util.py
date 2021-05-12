from PIL import Image, ExifTags


def restore_orientation(img: Image):
    try:
        image = img

        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = image._getexif()

        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)

        return image
    except (AttributeError, KeyError, IndexError):
        return img
    except Exception as e:
        print(e)
        return img
