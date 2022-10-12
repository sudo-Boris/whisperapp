import tkinter as tk
import customtkinter as ctk
import soundfile as sf
import sounddevice as sd

# pip install git+https://github.com/openai/whisper.git
import whisper

# Select from the following models: "tiny", "base", "small", "medium", "large"
model = whisper.load_model("small")

# create the app
app = tk.Tk()
app.geometry("532x632")
app.title("Voice to text")
ctk.set_appearance_mode("dark")

main_label = ctk.CTkLabel(
    height=512, width=512, text_color="black", text_font=("Roboto Medium", -16)
)
main_label.place(x=10, y=110)


def voice_rec():
    fs = 48000

    # seconds
    duration = 5
    main_label.configure(text="Recording...")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    # Save as FLAC file at correct sampling rate
    sf.write("my_Audio_file.flac", myrecording, fs)
    main_label.configure(text="Recording done")


def transcribe():
    audio = "my_Audio_file.flac"

    # You can provide the language to the model if it is a bit to "exotic" to predict
    options = {"fp16": False, "language": None, "task": "transcribe"}
    results = model.transcribe(audio, **options)

    print(results["text"])
    main_label.configure(text=results["text"])


def translate():
    audio = "my_Audio_file.flac"

    # You can provide the language to the model if it is a bit to "exotic" to predict
    options = {"fp16": False, "language": None, "task": "translate"}
    results = model.transcribe(audio, **options)

    print(results["text"])
    main_label.configure(text=results["text"])


recordButton = ctk.CTkButton(
    height=40,
    width=120,
    text_font=("Roboto Medium", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=voice_rec,
)
recordButton.configure(text="Record")
recordButton.place(x=206, y=60)

transcribeButton = ctk.CTkButton(
    height=40,
    width=120,
    text_font=("Roboto Medium", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=transcribe,
)
transcribeButton.configure(text="Transcribe")
transcribeButton.place(x=106, y=150)

translateButton = ctk.CTkButton(
    height=40,
    width=120,
    text_font=("Roboto Medium", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=translate,
)
translateButton.configure(text="Translate")
translateButton.place(x=306, y=150)


# run app
app.mainloop()
