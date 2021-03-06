# Wilderness Image Classification using Neural Networks

- by <B>Mayank Patel</B>, IIT Kharagpur, India (under supervision of <B>Professor Tomas Maul</B>, University of Nottingham, Malaysia)

<br><br>

### This project reviews the performances of the presently available deep learning models for forest and non-forest/monoculture/agriculture/crop plantation image classification.




### For a brief summary of this report go to [final_report.pdf](https://github.com/mayankpatel14/Wilderness-Image-Classification/blob/master/final_report.pdf).


<br>

## Experiments:
The Experiment has been done in two parts:
- Classification between forest and others (includes every terrain other than forest)
- Classification between forest and monoculture

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
The data has been downloaded from Google Earth Pro (GE). We collected 24 (4800 x 2822) images belonging to category of forest and 24 images that belong to non-forest category. These raw images were sliced into 256 x 256-pixel size images. As a result, we have 2978 images and 4798 images of forest and non-forest(green and others) category. We have separated 2000 images taken randomly out of 7776 images in the validation set for the first experiment. For the second experiment classification has been done using 2978 images of forest and 1980 green images. Green images are images that include monoculture, agriculture and terrains which look similar to forest but are not considered forest.

<br>

## Results
For visualizations of the training and validation accuracies and losses go to [final_report.pdf](https://github.com/mayankpatel14/Wilderness-Image-Classification/blob/master/final_report.pdf).<br>
<br><br>
Table 1. Classification between forest and non-forest images
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Models</th>
    <th class="tg-0pky">Test Accuracy</th>
    <th class="tg-0pky">Test Loss</th>
    <th class="tg-0pky">Training Loss</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Lenet</td>
    <td class="tg-0pky">0.9235</td>
    <td class="tg-0pky">0.2397</td>
    <td class="tg-0pky">0.0000</td>
  </tr>
  <tr>
    <td class="tg-0pky">VGGNet11</td>
    <td class="tg-0pky">0.9984</td>
    <td class="tg-0pky">0.0070</td>
    <td class="tg-0pky">0.0328</td>
  </tr>
  <tr>
    <td class="tg-0pky">VGGNet13</td>
    <td class="tg-0pky">0.9978</td>
    <td class="tg-0pky">0.0378</td>
    <td class="tg-0pky">0.0352</td>
  </tr>
  <tr>
    <td class="tg-0pky">VGGNet16</td>
    <td class="tg-0pky">0.9982</td>
    <td class="tg-0pky">0.0083</td>
    <td class="tg-0pky">0.0434</td>
  </tr>
  <tr>
    <td class="tg-0pky">VGGNet19</td>
    <td class="tg-0pky">0.9971</td>
    <td class="tg-0pky">0.0099</td>
    <td class="tg-0pky">0.0412</td>
  </tr>
  <tr>
    <td class="tg-0pky">ResNet9</td>
    <td class="tg-0pky">0.9975</td>
    <td class="tg-0pky">0.0114</td>
    <td class="tg-0pky">0.0160</td>
  </tr>
  <tr>
    <td class="tg-0pky">Google-Inceptionv1</td>
    <td class="tg-0pky">0.9968</td>
    <td class="tg-0pky">0.0118</td>
    <td class="tg-0pky">0.0225</td>
  </tr>
  <tr>
    <td class="tg-0pky">DenseNet121</td>
    <td class="tg-0pky">0.9650</td>
    <td class="tg-0pky">0.1170</td>
    <td class="tg-0pky">0.2160</td>
  </tr>
  <tr>
    <td class="tg-0pky">MobileNetv2</td>
    <td class="tg-0pky">0.9760</td>
    <td class="tg-0pky">0.0775</td>
    <td class="tg-0pky">0.1645</td>
  </tr>
</tbody>
</table>
<br>
Table 2. Classification between forest and green images
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Models</th>
    <th class="tg-0pky">Test Accuracy</th>
    <th class="tg-0pky">Test Loss</th>
    <th class="tg-0pky">Training Loss</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Lenet</td>
    <td class="tg-0pky">0.9795</td>
    <td class="tg-0pky">0.0710</td>
    <td class="tg-0pky">0.0000</td>
  </tr>
  <tr>
    <td class="tg-0pky">VGGNet11</td>
    <td class="tg-0pky">0.9943</td>
    <td class="tg-0pky">0.0057</td>
    <td class="tg-0pky">0.0148</td>
  </tr>
  <tr>
    <td class="tg-0pky">VGGNet13</td>
    <td class="tg-0pky">0.9990</td>
    <td class="tg-0pky">0.0044</td>
    <td class="tg-0pky">0.0201</td>
  </tr>
  <tr>
    <td class="tg-0pky">VGGNet16</td>
    <td class="tg-0pky">0.9985</td>
    <td class="tg-0pky">0.0047</td>
    <td class="tg-0pky">0.0199</td>
  </tr>
  <tr>
    <td class="tg-0pky">VGGNet19</td>
    <td class="tg-0pky">0.9983</td>
    <td class="tg-0pky">0.0070</td>
    <td class="tg-0pky">0.0206</td>
  </tr>
  <tr>
    <td class="tg-0pky">ResNet9</td>
    <td class="tg-0pky">0.9990</td>
    <td class="tg-0pky">0.0031</td>
    <td class="tg-0pky">0.0048</td>
  </tr>
  <tr>
    <td class="tg-0pky">Google-Inceptionv1</td>
    <td class="tg-0pky">0.9970</td>
    <td class="tg-0pky">0.0125</td>
    <td class="tg-0pky">0.0423</td>
  </tr>
  <tr>
    <td class="tg-0pky">DenseNet121</td>
    <td class="tg-0pky">0.9961</td>
    <td class="tg-0pky">0.0099</td>
    <td class="tg-0pky">0.0328</td>
  </tr>
  <tr>
    <td class="tg-0pky">MobileNetv2</td>
    <td class="tg-0pky">0.9861</td>
    <td class="tg-0pky">0.0469</td>
    <td class="tg-0pky">0.1474</td>
  </tr>
</tbody>
</table>

<br><br><br>

Tags: Image-Classification, forest, non-forest, agriculture, monoculture, trees, computer-vision, machine-learning, deep-learning, Neural-Networks


