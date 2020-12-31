# Wilderness Image Classification using Neural Networks

- by <B>Mayank Patel</B>, IIT Kharagpur, India (under supervision of <B>Professor Tomas Maul</B>, University of Nottingham, Malaysia)

<br><br>

### This project reviews the performances of the presently available deep learning models for forest and non-forest/monoculture/agriculture/crop plantation image classification.




### For a brief summary of this report go to [final_report.pdf](https://github.com/mayankpatel14/Wilderness-Image-Classification/blob/master/final_report.pdf).


<br>

## Training:
We have trained the following models:
-	LeNet
-	VGGNet11, VGGNet13, VGGNet16, VGGNet19
-	ResNet9
-	Google-Inceptionv1
-	DenseNet
-	MobileNetv2<br>

<br>Find the code to the models in [models](https://github.com/mayankpatel14/Wilderness-Image-Classification/tree/master/models) and the guide to run models.
<br>
<br>
## [Data](https://github.com/mayankpatel14/Wilderness-Image-Classification/tree/master/data)
The data has been downloaded from Google Earth Pro (GE). We collected 24 (4800 x 2822) images belonging to category of forest and 24 images that belong to non-forest category. These raw images were sliced into 256 x 256-pixel size images. As a result, we have 3888 images and 3888 images of forest and non-forest category. We have separated 2000 images taken randomly out of 7776 images in the validation set. 
<br><br>
## Results
For visualizations of the training and validation accuracies and losses go to [final_report.pdf](https://github.com/mayankpatel14/Wilderness-Image-Classification/blob/master/final_report.pdf).

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Models</th>
    <th class="tg-0pky">Validation Accuracy</th>
    <th class="tg-0pky">Validation Loss</th>
    <th class="tg-0pky">Training Loss</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Lenet</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">VGGNet11</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">VGGNet13</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">VGGNet16</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">VGGNet19</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">ResNet9</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Google-Inception</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">DenseNet</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">MobileNet</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
</tbody>
</table>



Tags: Image-Classification, forest, non-forest, agriculture, monoculture, trees, computer-vision, machine-learning, deep-learning, Neural-Networks


