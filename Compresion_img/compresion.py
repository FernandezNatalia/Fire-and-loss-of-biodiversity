from skimage import io
import cv2

img_path = 'gray.jpeg'
img = cv2.imread(img_path, 0)
img_reverted = cv2.bitwise_not(img)
res = cv2.resize(img, dsize=(200,200), interpolation=cv2.INTER_CUBIC)
#new_img = img_reverted / 255.0

#print(len(new_img[0]))
#print(img_reverted)
print(len(res))

cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
cv2.imshow('dst_rt', res)
cv2.waitKey(0)

# image = io.imread("gray.jpeg", vmin=0,vmax=1)
# print(len(image[0]))
# print(len(image))

# data = {'first_name': image,
#         'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
#         'age': [27, 31, 36, 53, 48, 36, 40, 34],
#         'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
#         'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]
#         }
# df = pd.DataFrame(data, columns = ['first_name', 'last_name', 'age', 'amount_1', 'amount_2'])
# df.to_excel('example.xlsx', sheet_name='example')