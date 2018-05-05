import matplotlib.pyplot as plt
from skimage.measure import structural_similarity as ssim
import cv2
import numpy as np


# compute image diffs based on structural similarity
def compute_diff(A, B):
    imageA = cv2.imread(A)
    imageB = cv2.imread(B)

    imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    return ssim(imageA, imageB)


# mean squared error
def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageB.shape[1])

    return err

# compute image diffs and render images side by side with scores
def compare_images(imageA, imageB, title):
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)

    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")

    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")

    plt.show()


def main():
    imageA = cv2.imread("plate_full.png")
    imageB = cv2.imread("plate_empty.png")

    imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    images = ("Full", imageA), ("Empty", imageB)

    fig = plt.figure("Images")

    for (i, (name, image)) in enumerate(images):
        ax = fig.add_subplot(1, 3, i + 1)
        ax.set_title(name)
        plt.imshow(image, cmap=plt.cm.gray)
        plt.axis("off")

    plt.show()

    compare_images(imageA, imageA, "full vs full")
    compare_images(imageB, imageB, "empty vs empty")
    compare_images(imageA, imageB, "full vs empty")

    return


if __name__ == "__main__":
    main()
