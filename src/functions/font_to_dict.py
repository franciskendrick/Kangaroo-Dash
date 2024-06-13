from .clip_image import clip


def clip_font_to_dict(font_set, order, separator_color=(255, 0, 0, 255)):
    characters = {}
    character_wd = 0
    idx = 0

    # Loop Over Every Top Pixel in Fontset
    for x in range(font_set.get_width()):
        pixel = font_set.get_at((x, 0))

        # Found a Separator
        if pixel == separator_color:
            # Get Letter Image
            img = clip(
                font_set,
                (x - character_wd, 0),
                (character_wd, font_set.get_height())
            )

            # Append Image to Characters
            characters[order[idx]] = img

            # Update Variables
            character_wd = 0
            idx += 1
        else:
            # Update Variables
            character_wd += 1

    # Return
    return characters