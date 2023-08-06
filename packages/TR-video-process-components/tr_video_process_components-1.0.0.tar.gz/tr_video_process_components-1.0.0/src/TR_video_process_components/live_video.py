import cv2
import threading
import numpy as np

class Live_Video():
    # img = np.empty((2158,4096,3))

    def __init__(self, camera):
        self.camera = camera

        self.event = threading.Event()
        self.alive = True
        self._start_thread_main()
        self.img = None

    #Threading
    def _start_thread_main(self):
        self.thread_main = threading.Thread(target = self._main_func)
        self.thread_main.start()
        print('main function Threading Started')
        print('Thread status', self.thread_main)

    def start(self):
        self.event.set()
        print("Threading Begin")
        print('Thread status', self.thread_main)

    def stop(self):
        self.event.clear()
        print("\n Threading Stopped")
        print('Thread status', self.thread_main)

        # if self.camera.camera.IsGrabbing():
        #     print('Grabbing')
        #     self.camera.camera.StopGrabbing()


    def _main_func(self):
        # スレッドを待機させる(=臨時停止する。）
        # 内部フラグがTrueになるまで、スレッドを待機させる。 is_set()で判別
        self.event.wait()

        while self.alive:

            if self.event.is_set() == True:

                # get frame
                self.img = self.camera.grab(en_print = False)

                # img = cv2.rotate(img, cv2.ROTATE_180)
                # # Crop Image
                # img = img_control.crop_image(img = img, crop_w = self.crop_w, camera_width = self.camera_width,
                #                              camera_height = self.camera_height)
                # if img is None:
                #     time.sleep(0.1)
                #     continue
                # Draw on Canvas
                # self.draw_on_Canvas1(img)
                # print(img.shape)
                # cv2.imshow('test',img)
                # cv2.waitKey(1) & 0xff == ord('q')


                

            else:
                self.event.wait()
                print('stopped...')
