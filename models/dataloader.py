"""
While uploading data, create directories like this
- train
	- forest(this directory contains all the images of forests)
	- non-forest(this directory contains images corresponding to non-forests)
"""


img_folder=r'/content/drive/MyDrive/Wilderness_Classification/images/train'

dataset = ImageFolder(img_folder, transform=ToTensor())

random_seed = 42
torch.manual_seed(random_seed)
val_size = 2000
train_size = len(dataset) - val_size

train_ds, val_ds = random_split(dataset, [train_size, val_size])


batch_size=10
train_dl = DataLoader(train_ds, batch_size, shuffle=True, num_workers=4, pin_memory=True)
val_dl = DataLoader(val_ds, batch_size*2, num_workers=4, pin_memory=True)