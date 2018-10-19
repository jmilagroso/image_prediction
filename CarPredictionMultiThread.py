
# https://github.com/OlafenwaMoses/ImageAI
# https://github.com/fchollet/deep-learning-models/releases

from imageai.Prediction import ImagePrediction
import os
import threading
import sys

execution_path = os.getcwd()

imagesfolder = sys.argv[1]
imagesfiles = os.listdir(imagesfolder)

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath( os.path.join(execution_path + "/deep_learning_models", "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))

class PredictionThread(threading.Thread):

	def init(self):
		threading.Thread.init(self)
		
	def run(self):
		print ("During PredictionThread@run @Current Thread: ", threading.currentThread().name)

		global prediction
		prediction.loadModel()

		for imagefile in imagesfiles:
			if imagefile.endswith(".png") or imagefile.endswith(".jpg"):
				predictions, probabilities = prediction.predictImage(imagesfolder + imagefile, result_count=5)
		
				print ("----------------------------------------------")

				for predict,percent in zip(predictions, probabilities):
					print (imagefile,"|",predict,"|",str(round(percent, 2)), "% probability")

print ("Before PredictionThread call @Current Thread: ", threading.currentThread().name)	
predictionThread = PredictionThread ()
predictionThread.start()
