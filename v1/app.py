import tkinter as tk
import customtkinter as ctk
import soundfile as sf
import sounddevice as sd

# pip install git+https://github.com/openai/whisper.git
import whisper

model = whisper.load_model("small")

# Create the app
app = tk.Tk()
app.geometry("532x632")
app.title("Voice to text")
ctk.set_appearance_mode("dark")

main_label = ctk.CTkLabel(
    height=512, width=512, text_color="black", text_font=("Roboto Medium", -16)
)
main_label.place(x=10, y=110)

language_input = ctk.CTkEntry(
    height=40,
    width=512,
    text_font=("Arial", 20),
    text_color="black",
    fg_color="white",
    placeholder_text="Enter language to support model.",
)
language_input.place(x=10, y=10)


def transcribe():
    main_label.configure(text="Transcribing...")
    audio = "/Users/borismeinardus/personal_projects/whisperapp/v1/my_Audio_file.flac"
    # audio = whisper.load_audio(audio)
    # audio = whisper.pad_or_trim(audio)

    # mel = whisper.log_mel_spectrogram(audio).to(model.device)

    if language_input.get():
        language = language_input.get()
        print(language)
    else:
        # _, probs = model.detect_language(mel)
        language = None

    # options = whisper.DecodingOptions(fp16=False, language=language)
    options = {"fp16": False, "language": language, "task": "transcribe"}
    result = model.transcribe(audio, **options)

    print(result["text"])
    main_label.configure(text=result["text"])
    return result["text"]


def translate():
    main_label.configure(text="Translating...")
    audio = "/Users/borismeinardus/personal_projects/whisperapp/v1/my_Audio_file.flac"
    # audio = whisper.load_audio(audio)
    # audio = whisper.pad_or_trim(audio)

    # mel = whisper.log_mel_spectrogram(audio).to(model.device)

    if language_input.get():
        language = language_input.get()
        print(language)
    else:
        # _, probs = model.detect_language(mel)
        language = None

    # options = whisper.DecodingOptions(fp16=False, language=language)
    options = {"fp16": False, "language": language, "task": "translate"}
    result = model.transcribe(audio, **options)["text"]

    print(result)
    main_label.configure(text=result)
    return result


def voice_rec():
    fs = 48000

    # seconds
    duration = 5
    main_label.configure(text="Recording...")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    # Save as FLAC file at correct sampling rate
    sf.write("v1/my_Audio_file.flac", myrecording, fs)
    main_label.configure(text="Recording done")


record = ctk.CTkButton(
    height=40,
    width=120,
    text_font=("Arial", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=voice_rec,
)
record.configure(text="Record")
record.place(x=206, y=60)

transcribeButton = ctk.CTkButton(
    height=40,
    width=120,
    text_font=("Arial", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=transcribe,
)
transcribeButton.configure(text="Transcribe")
transcribeButton.place(x=106, y=150)

translateButton = ctk.CTkButton(
    height=40,
    width=120,
    text_font=("Arial", 20),
    text_color="white",
    fg_color=("white", "gray38"),
    command=translate,
)
translateButton.configure(text="Translate")
translateButton.place(x=306, y=150)

app.mainloop()
