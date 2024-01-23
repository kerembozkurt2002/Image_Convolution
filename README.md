# Image_Convolution

In this project, the program is able to make certain calculations on pixels of images recursively.
The program accepts the PPM and PGM image formats for reading image files. 

1- First Operation:
The program use PGM files for this operation. In PGM files, images are represented with pixels that have a single value which represents the gray levels. This information can be represented as nested lists, where there is a single channel.
When the operation input is 1, the program apply a form of recursive region coloring to the image.
The image will contain black pixels (0 grayscale value) that separate regions. The pixels in a region will contain different grayscale values. The task is to find the average grayscale value of all the pixels in each region and color that entire region to that region's average grayscale value. This needs to be done for all regions in a given image.
An example of what is expected is provided below:


Example Image:


![image](https://github.com/kerembozkurt2002/Image_Convolution/assets/157289283/659da08e-939f-4274-9d97-acfb52b86a84)

Colored Image:

![image](https://github.com/kerembozkurt2002/Image_Convolution/assets/157289283/5b62a272-26d9-45dd-a9d4-f35c95772f48)




