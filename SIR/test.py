import matplotlib.pyplot as plt

font_path = 'NanumGothic.ttf'
font_name = plt.matplotlib.font_manager.FontProperties(fname=font_path).get_name()
print(font_name)