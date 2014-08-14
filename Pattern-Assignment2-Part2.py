import matplotlib.pyplot as pylab
from PIL import Image
import ImageChops
import numpy


STANDARD_SIZE = (160, 160)

def image_lists(image):
    listx =[0]*STANDARD_SIZE[0]
    listy =[0]*STANDARD_SIZE[1]
    for x in range(STANDARD_SIZE[0]):
        for y in range(STANDARD_SIZE[1]):
            px = image[x, y]
            if ( px == 255):
                listx[x] = listx[x]+1;
                listy[y] = listy[y]+1;
    return listx , listy
  
def get_image_data(filename):
    img = Image.open(filename)
    img = img.convert('1')
    img = trim(img,'white')
    img = img.resize(STANDARD_SIZE, Image.ANTIALIAS) # best down-sizing filter
    img=img.load()
    return img
  
def trim(im, border):
    bg = Image.new(im.mode, im.size, border)
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

#training_data
training_list=[]
img0 = get_image_data("0.jpg");
training_list= training_list + [img0]  
img1 = get_image_data("1.jpg");
training_list= training_list + [img1]      
img2 = get_image_data("2.jpg");  
training_list= training_list + [img2]  
img3 = get_image_data("3.jpg");
training_list= training_list + [img3]  
img4 = get_image_data("4.jpg");
training_list= training_list + [img4]  
img5 = get_image_data("5.jpg");
training_list= training_list + [img5]  
img6 = get_image_data("6.jpg");
training_list= training_list + [img6]  
img7 = get_image_data("7.jpg");
training_list= training_list + [img7]     
img8 = get_image_data("8.jpg");
training_list= training_list + [img8]     
img9 = get_image_data("9.jpg");
training_list= training_list + [img9]



#input image
test_list=[]

img0_test = get_image_data("0 - Copy.jpg");
test_list= test_list + [img0_test]  

img1_test = get_image_data("1 - Copy.jpg");
test_list= test_list + [img1_test] 

img2_test = get_image_data("2 - Copy.jpg");
test_list= test_list + [img2_test]  

img3_test = get_image_data("3 - Copy.jpg");
test_list= test_list + [img3_test]

img4_test = get_image_data("4 - Copy.jpg");
test_list= test_list + [img4_test]

img5_test = get_image_data("5 - Copy.jpg");
test_list= test_list + [img5_test] 

img6_test = get_image_data("6 - Copy.jpg");
test_list= test_list + [img6_test]

img7_test = get_image_data("7 - Copy.jpg");
test_list= test_list + [img7_test]  

img8_test = get_image_data("8 - Copy.jpg");
test_list= test_list + [img8_test]  

img9_test = get_image_data("9 - Copy.jpg");
test_list= test_list + [img9_test]  

 

true = 0;

results =[];
for k in test_list:
    diff = 0;
    diff_list =[];
    for x in training_list:   
        for i in range(STANDARD_SIZE[0]):
            for j in range(STANDARD_SIZE[1]):              
                diff = diff+(abs(k[i,j] -x[i,j]));
        diff_list.append(diff);
        diff = 0;
   
    index = numpy.argmin(diff_list)
    if (index == len(results)):
        true = true +1;
    results.append(index);
   
print results
print "Accuracy on testing data = " , true*100/10 ,'%'
    