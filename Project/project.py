import cv2
from datetime import datetime
from pathlib import Path


class CameraCapture:
    def __init__(self, camera_index=0):
        self.camera = cv2.VideoCapture(camera_index)

        if not self.camera.isOpened():
            raise RuntimeError("Não foi possível acessar a câmera.")

    def capture(self):
        success, frame = self.camera.read()

        if not success:
            raise RuntimeError("Falha ao capturar a imagem.")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = Path("captures")
        output_dir.mkdir(exist_ok=True)

        filename = output_dir / f"photo_{timestamp}.jpg"

        cv2.imwrite(str(filename), frame)

        return filename

    def release(self):
        self.camera.release()

def main():
    camera = CameraCapture()

    try:
        print("Câmera iniciada.")
        print("Pressione ENTER para capturar uma foto.")

        input()

        photo = camera.capture()
        print(f"Foto salva em: {photo}")

    except RuntimeError as error:
        print(f"Erro: {error}")

    finally:
        camera.release()


if __name__ == "__main__":
    main()