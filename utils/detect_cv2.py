import cv2
import torch
from tqdm import tqdm 

def detection(input_video, output_video, model):
    cap = cv2.VideoCapture(input_video) # 저장된 비디오파일 재생. 
    
    codec = cv2.VideoWriter_fourcc(*'mp4v') # mp4v->.mp4
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 프레임 가로 크기
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 프레임 세로 크기
    fps = int(cap.get(cv2.CAP_PROP_FPS)) # 초당 프레임의 수
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 비디오 파일의 총 프레임의 수

    out = cv2.VideoWriter(output_video, codec, fps, (width, height)) # 비디오 저장을 위한 객체 생성

    with tqdm(total=total_frames, desc="Processing", unit="frame") as pbar:
        while cap.isOpened(): 
            ret, frame = cap.read() 
            
            if not ret: # 새로운 프레임을 못 받아 왔을때 break 
                break
            results = model(frame)
            result_frame = results.render()[0]
            out.write(result_frame) 
            pbar.update(1)

    cap.release() 
    out.release() 
    cv2.destroyAllWindows() 