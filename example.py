from gesture_recognizer import GestureRecognizer as gr
import time
rec = gr.GestureRecognizer(print_pos=False)
rec.start_recognizing()
time.sleep(5)
print(rec.gesture.x_dir)
time.sleep(10)