def GA_img_visualize():
    import matplotlib.pyplot as plt
  # Создание полотна для рисунка
    plt.figure(1, figsize=(8, 10))

    plt.plot(mean_val, label='Среднее значение точности на проверочной выборке')
    plt.plot(max_val, label='Лучшее значение точности на проверочной выборке')
  # Задание подписей осей 
    plt.xlabel('Эпоха обучения')
    plt.ylabel('Значение точности')
    plt.legend()

  # Фиксация графиков и рисование всей картинки
    plt.show()