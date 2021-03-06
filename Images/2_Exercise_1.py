'''
Image Exercise
In the folder "Working with Images" (same folder this notebook is located in) there are two images
we will be working with:

word_matrix.png
mask.png
The word_matrix is a .png image that contains a spreadsheet of words with a hidden message in it.

Your task is to use the mask.png image to reveal the hidden message inside the word_matrix.png.
Keep in mind, you may need to make changes to the mask.png in order for this to work. That is all we'll say
 for now, since we really want you to discover this on your own!

This exercise is more open-ended, so we won't guide you with the steps, instead, letting you explore and
figure things out on your own as you would in a real world situation. However, if you get stuck,
you can always view the solutions video or notebook for guidance. Best of luck!


'''

from PIL import Image
words = Image.open('word_matrix.png')
words.show()

mask = Image.open("mask.png")
mask.show()

# Resize Images to Match
print(mask.size) #(505, 251)
print(words.size) #(1015, 559)
mask = mask.resize((1015,559))
print(mask.size) #(1015, 559)

#Add in alpha parameter
#Now we can't just paste them over, otherwise we won't see what is underneath, we need to add an alpha value.

mask.putalpha(200) # links.putalpha(128)
mask.show()

words.paste(mask,(0,0),mask)
words.show()