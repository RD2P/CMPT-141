# ===================== #
# Raphael De Los Reyes
# 11189672
# gld141  
# ===================== #

import numpy as np
import matplotlib.pyplot as plt

# Initialize width and height
w, h = 100, 100

# create 2D array of random integers between 0 and 255
art = np.random.randint(0, 256, size=(w, h))

# Initialize lists to store the lighter and darker pixel art
lighter = []
darker = []
# Iterate through art and append modified pixel values to lighter and darker lists
for i in art:
  lighter.append([x + 30 if x + 30 < 256 else 255 for x in i])
  darker.append([x - 30 if x - 30 >= 0 else 0 for x in i])

# Create arrays from the lists
light_art = np.array(lighter)
dark_art = np.array(darker)

# Create a figure with three subplots side by side
fig, (ax1, ax2, ax3) = plt.subplots(1, 3,  figsize=(15, 5))

# Display the original art
ax1.imshow(art)
ax1.set_title('Original Art')
ax1.axis('off')

# Display the lighter pixel art
ax2.imshow(light_art)
ax2.set_title('Lighter Art')
ax2.axis('off')

# Display the darker pixel art
ax3.imshow(darker)
ax3.set_title('Darker Art')
ax3.axis('off')

# Show
plt.show()