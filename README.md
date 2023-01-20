# Bublo
## Your virtual Python assistant coming to live

Bublo is a virtual assistant, capable of recognizing and interacting with people in its environment.
Unlike other virtual assistants, Bublo will get a real physical body in the long run. 
He is equipped with a camera, microphone and speakers to interact with people. Bublo sometimes has a strange sense of humour and might say things just the way they are, but he means no harm. 


Features:
- Recognize people
- Register new faces and persons
- Interact with ChatGPT to provide great answers
- Tell jokes (altough not the best ones)
- Might be grumpy sometimes

## Troubleshooting

- `Could not build wheels for pyaudio, which is required to install pyproject.toml-based projects`  
See https://stackoverflow.com/questions/68251169/unable-to-install-pyaudio-on-m1-mac-portaudio-already-installed
It is most likely solved by running `brew install portaudio`

- `OSError: FLAC conversion utility not available`.  
Run `brew install flac`
