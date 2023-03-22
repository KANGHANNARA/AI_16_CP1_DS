# AI_16_CP1_DS_PROJECT
## 정상차량과 과적차량 object detection

### 노트북과 로컬 환경에서 실행 할 수 있는 레포지토리 입니다.

* 폴더
  * video_samples : 모델 추론의 입력값으로 사용할 영상 파일들이 저장되어 있는 폴더입니다.

  * models : 사전 학습된 모델의 가중치 파일(best.pt)이 저장되어 있습니다.

  * utils : models 내 모델을 통해 영상 내 객체를 탐지하는 object detection을 진행하고 결과를 .mp4 형태로 생성하는 detect 모듈이 저장되어 있습니다.

  * results : detect_cv2.py에 의해 생성된 결과 영상이 해당 폴더에 저장되게 됩니다.

  * test : 해당 레포지토리를 실행하는 test_cv2.py 파일을 포함하고 있습니다.

* AI_16기_강한나라_CP1_DS.ipynb : 모델 학습을 진행했던 노트북입니다 - 실행 x

* requirements.txt : 로컬환경과 노트북에서 필요한 패키지를 모아둔 requirements.txt 입니다.

* test_overload.ipynb : 사전학습된 모델을 통해서 영상을 업로드 후 detect가 잘되는지 확인할 수 있는 노트북입니다.

### 노트북으로 실행 할 때

- test_overload.ipynb 를 직접 다운로드하거나 눌러서 open in colab 확장프로그램을 이용하여 노트북을 엽니다.
- 노트북의 순서에 따라서 번호 밑의 재생버튼을 클릭하거나 ctrl+F9 를 통해서 전체 실행을 해줍니다.
  * 1 : git clone을 이용해서 모델과 requirements.txt 불러와서 로드하는 과정 꼭 한번만 눌러주세요
  * 2 : 테스트 영상를 업로드 하는과정 테스트파일이 없다면 video_samples폴더에서 랜덤으로 다운로드하여 사용합니다.
  * 3 : 업로드한 영상속 화물차량이 불법차량인지 정상차량인지 판단하는 과정. 테스트가 완료된 영상은 AI_16_CP1_DS -> output에서 확인가능합니다 
  * 3.1 : 버튼을 누릅니다. > input 폴더에 검증했던 영상을 삭제합니다. > 2번 부터 다시 시작합니다.
    * 3.1 재시작 버튼은 재시작 할 때 한 번만 눌러야합니다.
    *  모두 실행(ctrl+F9)하였을 때는 누르지 않고 input 폴더에 검증했던 영상을 삭제 후 2번으로 다시시작합니다.

### 로컬 환경에서 실행 할 때

1. 레포지토리 클론
   - `git clone https://github.com/KANGHANNARA/AI_16_CP1_DS`
2. `cd AI_16_CP1_DS`로 폴더로 들어가서 python==3.8로 가상환경을 만듭니다.
   - `pip install -r requirements.txt` 필요한 라이브러리와 모듈을 설치합니다.
3. test/test_cv2.py 파일에서 검증 할 영상의 경로를 입력합니다.
(default는 샘플영상의 ./video_samples/sample5.mp4)
4. `python test/test_cv2.py` 로 실행합니다.
5. 결과영상은 result 폴더에 저장됩니다.
