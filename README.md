# Image_Convolution

In this project, the program is able to make certain calculations on pixels of images recursively.
The program accepts the PPM and PGM image formats for reading image files. 

# First Operation:
The program use PGM files for this operation. In PGM files, images are represented with pixels that have a single value which represents the gray levels. This information can be represented as nested lists, where there is a single channel.
When the operation input is 1, the program apply a form of recursive region coloring to the image.
The image will contain black pixels (0 grayscale value) that separate regions. The pixels in a region will contain different grayscale values. The task is to find the average grayscale value of all the pixels in each region and color that entire region to that region's average grayscale value. This needs to be done for all regions in a given image.
An example of what is expected is provided below:


Example Image:


![image](https://github.com/kerembozkurt2002/Image_Convolution/assets/157289283/659da08e-939f-4274-9d97-acfb52b86a84)

Colored Image:

![image](https://github.com/kerembozkurt2002/Image_Convolution/assets/157289283/5b62a272-26d9-45dd-a9d4-f35c95772f48)


Important details are provided below:
*Black pixels (0 value) should not be included in the averaging operation.
*While applying division to find the average color use integer division, not rounding.

Test Case Example:


![den](https://github.com/kerembozkurt2002/Image_Convolution/assets/157289283/a6fbb159-eac2-4721-8790-2c9483ca79a8)

To provide a visual explanation, below is how the input image ex8.pgm looks.

![image](https://github.com/kerembozkurt2002/Image_Convolution/assets/157289283/bcf95f7f-825f-4496-bea9-28f4fa4717ba)


Below is how the output pixels would look as an image.


![image](https://github.com/kerembozkurt2002/Image_Convolution/assets/157289283/1aac89d1-6261-46f0-a223-e9fcfcc90b94)



# Second Operation:

The program use PPM files for this operation. In PPM files, images are represented with pixels that have 3 values each which represents the 3 main colors: red (R), green (G) and blue (B). This information can be represented as nested lists, where each main color corresponds to a separate color channel, as you can see in the image below.

![image](https://github.com/kerembozkurt2002/Image_Convolution/assets/157289283/f69c9be0-9ef3-46af-b001-9bef39e547be)


When the operation input is 2, the program apply the convolution operation recursively to the image.
Convolution is an operation that performs a weighted sum based on the values of a given kernel (filter) which is a 2-dimensional list of numbers, and the pixel values of a given image.
After a single weighted summation is complete, the filter moves on the image sideways by an amount named stride, and the operation is performed again until we arrive at the end of the line. After that, the filter is moved down by the amount of stride, and moved back to the beginning of the line, and the operation continues.
Meanwhile, the results of the weighted sum operations are recorded as they will form the resulting filtered image.
The image below visually demonstrates the process on an example where stride is 1:


![image](https://github.com/kerembozkurt2002/Image_Convolution/assets/157289283/542e0347-09fb-4827-8ffb-e35e937a692a)

The program need two additional inputs which it needs to take from the user: the first is the filename of the filter which will be located under the src folder
and the second is the stride parameter, an integer which denotes how many steps the filter will move after each summation is complete. Each input should be given in a separate line.
Important details are provided below:
*If the weighted sum exceeds the image maximum color value or becomes less than 0, the program clips it such that it is always between 0 and maximum color value.
*If the weighted sum is not an integer, the program casts it to an integer instead of rounding it.
*Filters can have different sizes, but their length and width will always should be the same, like m x m where m is an odd number.

To provide a visual explanation, below is how the input image img3.ppm looks.

![image](https://github.com/kerembozkurt2002/Image_Convolution/assets/157289283/388683bd-0d86-4d87-9d62-23329a57bee1)


Below is how the input image img3.ppm passed through a horizontal filter would look like. Note that this shows the horizontal features of the image.


![image](https://github.com/kerembozkurt2002/Image_Convolution/assets/157289283/224ecfdc-8a68-420a-96f1-af43b5333db9)


Below is how the input image img3.ppm passed through a vertical filter would look like. Note that this shows the vertical features of the image.


![image](https://github.com/kerembozkurt2002/Image_Convolution/assets/157289283/9fb8c31d-4104-4498-8526-117c453f44e1)



The program provides with the function img_printer(img) which is a function that prints 3-dimensional lists in a specific manner. The program use this and only this function to output the results. Images are provided just for easier understanding.













