# Live-Reconhecimento-Faces

Projeto desenvolvido em live para criar um código de reconhecimento de faces. Para acessar a live descrevendo completamente o projeto, clique na imagem abaixo.

<p align="center">
  <a href="https://youtu.be/7ELvYSHCAc4"><img src="https://img.youtube.com/vi/t9Et8YwKHgU/maxresdefault.jpg"></a>
</p>

## Instalação

Após baixar o repositório, invoque o comando pip install -r requirements.txt para instalar os pacotes necessários para uso.

## Criação de dataset

Para criar o dataset para reconhecimento facial, execute o script createDataset.py. Os parâmetros são: URL de vídeo no YouTube, a pasta em que as detecções ficarão salvas e o nome da pessoa com o nome salvo.

Segue exemplos abaixo:
```console
C:\github\Face Recognition>python createDataset.py https://www.youtube.com/watch?v=2DAIe1SlLMo Atila/ Atila
```

```console
C:\github\Face Recognition>python createDataset.py https://www.youtube.com/watch?v=wVWkT4X0h0A ana_nv1c/ Ana
```

```console
C:\github\Face Recognition>python createDataset.py https://www.youtube.com/watch?v=SlixLsmWKn4 laura_nv1c/ Laura
```

## Reconhecimento de Faces

Para reconhecer face em vídeo de YouTube, deve se informar a URL do vídeo com o argumento -y, além do nome de arquivo de saída de vídeo com o parâmetro -o.

Siga os exemplos abaixo:
```console
C:\github\Face Recognition>python faceRecognition.py -y https://www.youtube.com/watch?v=YINTTVjBrY4 -o saida.avi
```

```console
C:\github\Face Recognition>python faceRecognition.py -y https://www.youtube.com/watch?v=19bXX_NbHVQ -o saida2.avi
```

No caso de detecção em imagens, deve se informar o caminho da imagem em disco com o argumento -i, além do nome de arquivo de saída de imagem com o parâmetro -o.

```console
C:\github\Face Recognition>python faceRecognition.py -i atila.jpg -o saida.jpg
```

```console
C:\github\Face Recognition>python faceRecognition.py -i laura.jpg -o saida2.jpg
```
