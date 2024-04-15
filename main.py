import os, glob, cv2

file_list = glob.glob(os.path.join("clips", "*.mp4"))
img_num = 0
count = 0
output_folder = "out_images"
for vid in file_list:
    vid_name = os.path.basename(vid).split('.')[0]
    vidcap = cv2.VideoCapture(vid)
    success = True
    while success:
        count += 1
        success, image = vidcap.read()
        if success == False:
            continue
        # image = cv2.resize(image, (800, 600), interpolation=cv2.INTER_AREA)
        if count % 15 == 0:
            cv2.imwrite(
                os.path.join(output_folder, "%s_frame_%d.jpg" % (vid_name, img_num)), 
                image)
            img_num += 1
