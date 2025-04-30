# Image-Restoration
This is a midterm project completed by me and two teammates from our Introduction to Image Processing course. Using OpenCV, we repaired damaged or flipped images. The project includes techniques such as image flipping, masking, sharpening, bilateral filtering, and contrast correction.


# Image Repair Lab
**OpenCV-based Restoration of Flipped, Blurred, and Overexposed Images** 

---

## Project Overview 

This is a **midterm project** from our **Image Processing course**, completed by a team of three students. We selected three different damaged images and applied suitable image restoration techniques using **Python and OpenCV**.

---

## Project Goals 

- Repair flipped or reversed image blocks  
- Enhance overly bright or high-contrast grayscale images  
- Restore blurred regions while preserving edge details

---

## Repaired Photos 

### 1️⃣ Flipped Blocks Restoration  
- Selected corrupted regions using mouse  
- Flipped each ROI (region of interest) using `cv2.flip()`  
- Masked the flipped image back into the original

Before ![image](https://github.com/user-attachments/assets/3f46a43b-c042-4c13-a159-2957532aa353)
After  ![image](https://github.com/user-attachments/assets/4b0bcf12-dc9d-47df-9f60-ffd421590e2b)

---

### 2️⃣ Contrast Enhancement in Grayscale  
- Inverted grayscale values  
- Applied gamma and beta correction to restore balance

Before ![image](https://github.com/user-attachments/assets/40debf33-e943-4798-b69c-4d91e49b8c18)
After  ![image](https://github.com/user-attachments/assets/00f55384-eab7-4a2b-b0f7-857bb5c1309e)


---

### 3️⃣ Blurring and Smoothing Recovery  
- Sharpened object edges with custom filters  
- Applied bilateral filtering to reduce noise while maintaining edges

Before ![image](https://github.com/user-attachments/assets/1049f682-cb53-43a5-8e2e-529bfce12620)
After  ![image](https://github.com/user-attachments/assets/2406de65-c56b-4a71-81ac-10b9b127833d)

---

## 🛠️ Tools and Libraries 

- Python 3.11  
- OpenCV (cv2)  
- Numpy  

---

## 👩‍💻 Team Members 
- 邱旻君
- 陳珮綺
- 何霆威
---

## 💡 Learning Outcomes 

- Gained hands-on experience with interactive region selection  
- Applied advanced OpenCV functions for real-world image repair  
- Practiced team-based problem solving and report documentation





