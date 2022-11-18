
"""Start.py
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1b44nG7bpC7h1A8IJypGIQxBLhDIPW1Y1
"""

# M O D E L    B U I L D I N G
early_stop_loss = EarlyStopping(monitor='loss', patience=3, verbose=1)
early_stop_val_acc = EarlyStopping(monitor='val_accuracy', patience=3, verbose=1)
model_callbacks=[early_stop_loss, early_stop_val_acc]