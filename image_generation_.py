# from PIL import Image
#
# # Image size
# width, height = 256, 256
#
# # Create a new image (RGB)
# img = Image.new("RGB", (width, height))
#
# # Fill pixels manually
# for x in range(width):
#     for y in range(height):
#         r = x        # red increases with x
#         g = y        # green increases with y
#         b = (x+y)//2 # blue is mix of both
#         img.putpixel((x, y), (r, g, b))
#
# # Save image
# img.save("gradient.png")
#

# Spot the 3 Differences Prompt Generator

def generate_prompt(theme, differences):
    prompt = f"""
Create a vertical cartoon illustration in flat vector style with a white background.
Show {theme}. 
Display two identical images stacked (top and bottom) for a 'Spot the Difference' puzzle. 
Add exactly 3 and only 3 differences between the two images:

1. {differences[0]}

2. {differences[1]}

3. {differences[2]}

Do not change anything else besides these 3 listed differences. No extra changes allowed.
"""
    return prompt.strip()

# Example: Theme + 3 Differences
theme = "a happy dog sitting beside her owner"
differences = [
    "Dog’s tail is wagging vs tail is still.",
    "Owner’s shirt has a pocket vs no pocket.",
    "Dog’s collar is red vs blue."
]

# Generate and print the prompt
prompt_text = generate_prompt(theme, differences)
print(prompt_text)
