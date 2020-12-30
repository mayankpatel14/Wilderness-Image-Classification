VGG_types = {
    'VGG11': [64, 'M', 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],
    'VGG13': [64, 64, 'M', 128, 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],
    'VGG16': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M'],
    'VGG19': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 256, 'M', 512, 512, 512, 512, 'M', 512, 512, 512, 512, 'M'],
}

for arch in VGG_types:
  class VGG_net(ImageClassificationBase):
      def __init__(self, in_channels=3, num_classes=2):
          super(VGG_net, self).__init__()
          self.in_channels = in_channels
          self.conv_layers = self.create_conv_layers(VGG_types[arch])
          
          self.fcs = nn.Sequential(
              nn.Linear(512*8*8, 4096),
              nn.ReLU(),
              nn.Dropout(p=0.5),
              nn.Linear(4096, 1024),
              nn.ReLU(),
              nn.Dropout(p=0.5),
              nn.Linear(1024, num_classes)
              )
          
      def forward(self, x):
          x = self.conv_layers(x)        
          x = x.reshape(x.shape[0], -1)
          #print(x.shape)
          x = self.fcs(x)
          return x

      def create_conv_layers(self, architecture):
          layers = []
          in_channels = self.in_channels
          
          for x in VGG_types[arch]:
              if type(x) == int:
                  out_channels = x
                  
                  layers += [nn.Conv2d(in_channels=in_channels,out_channels=out_channels,
                                      kernel_size=(3,3), stride=(1,1), padding=(1,1)),
                            nn.BatchNorm2d(x),
                            nn.ReLU()]
                  in_channels = x
              elif x == 'M':
                  layers += [nn.MaxPool2d(kernel_size=(2,2), stride=(2,2))]
                  
          return nn.Sequential(*layers)
  model=VGG_net()
  model.to(device)
  num_epochs = 50
  opt_func = torch.optim.Adam
  lr = 0.000001
  history = fit(num_epochs, lr, model, train_dl, val_dl, opt_func)
  plot_accuracies(history)
  plt.show()
  plot_losses(history)
  plt.show()