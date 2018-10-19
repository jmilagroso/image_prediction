# image_prediction
Simple image prediction using ImageAI library to determine car class/type.

```sh
➜  prediction git:(master) python CarPredictionMultiThread.py /usr/share/nginx/html/prediction/images/
Before PredictionThread call @Current Thread:  MainThread
During PredictionThread@run @Current Thread:  Thread-1
2018-10-19 17:17:05.026991: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
----------------------------------------------
Mitsubishi_Lancer.jpg | minivan | 28.23 % probability
Mitsubishi_Lancer.jpg | beach_wagon | 16.22 % probability
Mitsubishi_Lancer.jpg | limousine | 12.44 % probability
Mitsubishi_Lancer.jpg | car_wheel | 9.91 % probability
Mitsubishi_Lancer.jpg | grille | 7.74 % probability
----------------------------------------------
Toyota_Hilux.jpg | pickup | 96.86 % probability
Toyota_Hilux.jpg | jeep | 2.73 % probability
Toyota_Hilux.jpg | tow_truck | 0.07 % probability
Toyota_Hilux.jpg | grille | 0.05 % probability
Toyota_Hilux.jpg | car_wheel | 0.05 % probability
----------------------------------------------
Toyota_HiAces.png | minibus | 79.8 % probability
Toyota_HiAces.png | recreational_vehicle | 12.33 % probability
Toyota_HiAces.png | minivan | 3.48 % probability
Toyota_HiAces.png | moving_van | 2.46 % probability
Toyota_HiAces.png | jeep | 0.95 % probability
----------------------------------------------
Toyota_Wigo.jpg | beach_wagon | 17.23 % probability
Toyota_Wigo.jpg | pickup | 14.88 % probability
Toyota_Wigo.jpg | sports_car | 13.23 % probability
Toyota_Wigo.jpg | convertible | 10.05 % probability
Toyota_Wigo.jpg | car_wheel | 9.45 % probability
----------------------------------------------
Toyota_Vios.jpg | minivan | 48.08 % probability
Toyota_Vios.jpg | beach_wagon | 17.38 % probability
Toyota_Vios.jpg | pickup | 11.57 % probability
Toyota_Vios.jpg | car_wheel | 11.22 % probability
Toyota_Vios.jpg | grille | 4.34 % probability
```

Using [ImageAI](https://github.com/OlafenwaMoses/ImageAI)

