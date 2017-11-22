from model import Model
from generator import Generator
from keras.optimizers import Adam
from keras.callbacks  import ModelCheckpoint


opt   = Adam(lr=1.0e-5)
gen   = Generator().make(20)
model = Model().make(3, [40, 40, 40], 3)

chkpt = ModelCheckpoint(filepath       = 'model_weights.h5', 
                        verbose        = True, 
                        save_best_only = True, 
                        monitor        = 'mse'
)

model.compile(optimizer = opt, 
              loss      = 'mse', 
              metrics   = ['mse']
)

model.summary()

model.fit_generator(gen, 
                    steps_per_epoch = 20, 
                    epochs          = 10, 
                    callbacks       = [chkpt]
)
