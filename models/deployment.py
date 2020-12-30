

num_epochs = 50
model.to(device)
opt_func = torch.optim.Adam
lr = 0.00001

history = fit(num_epochs, lr, model, train_dl, val_dl, opt_func)

plot_accuracies(history)
plt.show()

plot_losses(history)
plt.show()