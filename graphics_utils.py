from screen_config import margin, width, height, screen


def draw_image_in_square(square_row, square_column, image):
    square_x = margin + (margin + width) * square_column
    square_y = margin + (margin + height) * square_row
    screen.blit(image, (square_x, square_y))