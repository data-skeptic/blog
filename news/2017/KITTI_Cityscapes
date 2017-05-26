##Towards a Holistic Scene Understanding 

Machine learning has been an essential tool for solving computer vision tasks such as image classification, object detection, instance recognition, and semantic segmentation, among others. The crux of machine learning approaches involves data. Training a machine requires enormous amounts of usable data. Why? Suppose you want to learn about monkeys and apes. Let’s also assume you’ve never seen any monkeys or apes in your lifetime, until one day, someone shows you a picture of a monkey and an ape. It might be difficult to generalize from one picture and discern the differences between a monkey and an ape. If you saw perhaps 50 pictures of each species, you would have a greater chance of noticing that monkeys tend to be smaller than apes and that monkeys tend to have tails, whereas apes do not. Now if you saw thousands of pictures of both monkeys and apes, it might become very clear to you that the two are in fact, very different. For example, you might discover monkeys and apes have different nose structures, upper bodies, feet and so on.

In the world of autonomous vehicles, makers of self-driving car utilize machine learning approaches to teaching their AI systems how to drive a car. One of the most important features of autonomous driving vehicles is the ability to understand the scene and perform complex perception tasks such as detecting and recognizing of lanes, roads, pedestrians, other vehicles, and traffic signs. For example, algorithms employed need to handle complex objects and environments while facing challenging environmental conditions such as direct lighting, reflections from specular surfaces, weather conditions. For these reasons, progress in this field is critically dependent on huge amounts of real-world data guarantee performance of algorithms in real situations. 
 
###KITTI
 
In 2012, researchers from Karlsruhe Institute of Technology and Toyota Technological Institute at Chicago introduced the [KITTI Vision Benchmark](https://www.cs.toronto.edu/~urtasun/publications/geiger_et_al_ijrr13.pdf) for stereo, visual odometer/SLAM or scene flow, and 3D object detection. It is recognized as the first and largest benchmark for testing vision-based autonomous driving algorithms, comprising six hours of recordings using high-resolution color and gray-scale stereo cameras, a Velodyne 3D laser scanner and high-precision GPS/IMU inertial navigation system. The KITTI dataset is also freely available to the public.

The dataset was captured while a car was being driven around Karlsruhe, Germany and includes data from a myriad of sensors on the car. The sensors include: four cameras to capture images and video, annotated 3D boxes, laser scanners as reference sensors, radar devices to capture radar signals, GPS/IMU to capture telemetry, LIDAR devices to capture laser-based distance points data, and so on. Below is the sensor setup used to collect the KITTI dataset.
![Sensor Setup](http://www.cvlibs.net/datasets/kitti/images/setup_top_view.png)

Below is the fully equipped vehicle:
![Fully Equipped](http://www.cvlibs.net/datasets/kitti/images/passat_sensors_920.png)

Tasks Covered in KITTI include: stereo, optical flow, scene flow, visual odometry, object detection, object tracking, and road segmentation. While the KITTI dataset provides a diverse set of science from the city center, rural areas, and highways, it doesn’t fully capture the variability and complexity of real-world inner-city traffic scenes. For instance, the KITTI dataset is limited to scenes from one city in Germany during the daytime and good weather conditions. Furthermore, KITTI only provides instance-level annotations regarding axis-aligned bounding boxes and lacks pixel-level annotations. Such limitations inhibit visual understanding of the complexity of urban street scenarios in the real world. 

Overall, KITTI by itself doesn't contain ground truth for semantic segmentation. The acquisition of ground truth is often labor intensive because very often this kind of information cannot be directly obtained with a sensor but requires tedious manual annotation. However, researchers have manually annotated parts of the KITTI Dataset to fit their necessities. For example, [Alvarez et al.](http://yann.lecun.com/exdb/publis/pdf/alvarez-eccv-12.pdf) generated ground truth for 323 images from the road detection challenge with three classes: road, vertical, and sky. Also, [Zhang et al.](http://ieeexplore.ieee.org/document/5979617/) annotated 252 RGB and Velodyne scan from the tracking problem for buildings, skies, roads, vegetations, sidewalks, cars pedestrians, cyclists, signs/poles, and fences. 

###Cityscapes Benchmark Suite
 
The [Cityscapes benchmark suite and a corresponding dataset]( https://arxiv.org/pdf/1604.01685.pdf) was introduced last year as a benchmark suite and large-scale dataset to train and test approaches for pixel-level and instance-level semantic labeling and understanding, as well as address the shortcomings of KITTI and other datasets. The Cityscapes dataset was tailored for autonomous driving in urban environments, featuring a more diverse range of backgrounds, complex inner-city traffic from 50 different cities worldwide during various seasons, and dense traffic conditions with wide roads and wide intersections. In contrast, KITTI has mainly composed less busy suburban traffic scenes and therefore significantly fewer flat ground structures, fewer humans, and more nature.
 
The Cityscapes dataset features two subsets: 5,000 detailed, pixel-level labeled images and 20,000 coarsely annotation images. The dataset is also annotated with 30 categories, of which 19 categories are included for training and evaluation. The training, validation, and test set contains 2975, 500, and 1525 high quality images, respectively. An additional 20000 images with coarse (polygonal) annotations are also provided but are only used for training. To date, Cityscapes is the largest and most diverse datasets for semantic segmentation of urban street scenes. 
 
![Fine annotation](https://www.cityscapes-dataset.com/wordpress/wp-content/uploads/2015/07/tuebingen00.png)
 
![Coarse annotation](https://www.cityscapes-dataset.com/wordpress/wp-content/uploads/2015/07/saarbrucken01.png)
 
[![Video and GPS metadata](https://www.cityscapes-dataset.com/wordpress/wp-content/uploads/2016/02/gpsMotionMeta_thumb.jpg](https://www.cityscapes-dataset.com/wordpress/wp-content/uploads/videos/gpsMotionMeta.mp4?id=3)

Creating large datasets, like Cityscapes, with pixel-wise semantic labels is known to be extremely challenging
due to the amount of human effort required to accurately trace object boundaries. High-quality semantic labeling for the Cityscapes dataset was reported to require 90 minutes per image!

Datasets have played a vital role in the progress of exciting research in machine learning and computer vision by providing problem specific examples with the ground truth that allow for the quantitative evaluation of approaches. That’s why efforts like the KITTI and Cityscapes datasets are so important.
