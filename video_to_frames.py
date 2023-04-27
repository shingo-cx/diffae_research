from pathlib import Path
import cv2

# 保存するディレクトリ
output_dir = Path("videos/video1_frames")
output_dir.mkdir(exist_ok=True)

# VideoCapture を作成する。
cap = cv2.VideoCapture("videos/video1.mp4")

n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # フレーム数を取得する。
n_digits = len(str(n_frames))  # フレーム数の桁数を取得する。

while True:
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    if not ret:
        break  # 取得に失敗した場合

    # フレームを画像として保存する。
    frame_no = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

    save_path = output_dir / f"frame_{frame_no:0{n_digits}d}.png"
    cv2.imwrite(str(save_path), frame)

cap.release()