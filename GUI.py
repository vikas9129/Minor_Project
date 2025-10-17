import sys
import speech_recognition as sr
import pyttsx3
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QPropertyAnimation, QRect


from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QPushButton, QLabel, QScrollArea, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette


class ChatBotUI(QWidget):
    def __init__(self):
        self.tts_engine = pyttsx3.init()  # Initialize the text-to-speech engine

        super().__init__()
        self.setWindowTitle("🤖 Smart ChatBot")
        self.setGeometry(200, 100, 500, 600)
        self.setStyleSheet("background-color: #121212; color: #FFFFFF;")
        self.initUI()

    def initUI(self):
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Title
        title = QLabel("💬 Chat with Bot")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #00BFFF; margin-bottom: 10px;")
        main_layout.addWidget(title)

        # Chat display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Segoe UI", 11))
        self.chat_display.setStyleSheet("""
            QTextEdit {
                background-color: #1E1E1E;
                border-radius: 10px;
                padding: 10px;
                color: #EAEAEA;
            }
        """)
        main_layout.addWidget(self.chat_display)

        # Horizontal layout for input and button
        input_layout = QHBoxLayout()

        self.input_box = QLineEdit()
        self.input_box.setFont(QFont("Segoe UI", 11))
        self.input_box.setPlaceholderText("Type your message here...")
        self.input_box.setStyleSheet("""
            QLineEdit {
                border: 2px solid #00BFFF;
                border-radius: 15px;
                padding: 8px;
                background-color: #2C2C2C;
                color: #FFFFFF;
            }
            QLineEdit:focus {
                border-color: #1E90FF;
            }
        """)
        input_layout.addWidget(self.input_box)
        mic_btn = QPushButton()
        mic_btn.setIcon(QIcon("mic_icon.png"))  # Use a microphone icon file
        mic_btn.setStyleSheet("background-color: #1E90FF; border-radius:15px; padding: 8px;")
        mic_btn.clicked.connect(self.record_voice)  # Link to voice recording method
        input_layout.addWidget(mic_btn)

        send_btn = QPushButton("Send")
        send_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        send_btn.setStyleSheet("""
            QPushButton {
                background-color: #00BFFF;
                color: white;
                border-radius: 15px;
                padding: 8px 20px;
            }
            QPushButton:hover {
                background-color: #1E90FF;
            }
        """)
        send_btn.clicked.connect(self.send_message)
        input_layout.addWidget(send_btn)

        main_layout.addLayout(input_layout)
        self.setLayout(main_layout)

        # Enter key press
        self.input_box.returnPressed.connect(self.send_message)

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def record_voice(self):
        """Record user voice, display full-screen overlay, convert to text, display in chat, and get bot reply"""
        overlay = VoiceOverlay(self)  # Create the full-screen overlay
        overlay.show()               # Show overlay before recording
        QApplication.processEvents()  # Make sure GUI updates

        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=5)  # listen for 5 seconds
                user_msg = recognizer.recognize_google(audio)
                self.display_message("You", user_msg)

            # Bot reply
                bot_reply = self.get_bot_reply(user_msg)
                self.display_message("Bot", bot_reply)
                self.speak(bot_reply)

        except Exception as e:
            self.display_message("System", "❌ Could not recognize voice. Try again.")

        overlay.close()  # Hide overlay after recording


    def send_message(self):
        user_msg = self.input_box.text().strip()
        if not user_msg:
            return

        self.display_message("You", user_msg)
        self.input_box.clear()

        # Simple bot response (you can integrate your NLP model here)
        bot_reply = self.get_bot_reply(user_msg)
        self.display_message("Bot", bot_reply)
        self.speak(bot_reply)

    def display_message(self, sender, message):
        if sender == "You":
            color = "#1E90FF"
        else:
            color = "#32CD32"

        formatted_text = f"<b style='color:{color}'>{sender}:</b> {message}<br>"
        self.chat_display.append(formatted_text)

    def get_bot_reply(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input:
            return "Hi there! 😊 How can I help you today?"
        elif "your name" in user_input:
            return "I'm your smart chatbot created with PyQt5!"
        elif "bye" in user_input:
            return "Goodbye! 👋 Have a great day!"
        else:
            return "I'm not sure I understand that yet 🤔"


class VoiceOverlay(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setModal(True)
        self.setStyleSheet("background-color: rgba(128, 128, 128, 150);")  # semi-transparent black

        # Cover only chat area
        chat_geom = parent.chat_display.geometry()
        self.setGeometry(parent.mapToGlobal(chat_geom.topLeft()).x(),
                         parent.mapToGlobal(chat_geom.topLeft()).y(),
                         chat_geom.width(),
                         chat_geom.height())

        # Round center mic label
        self.mic_label = QLabel(self)
        self.mic_label.setAlignment(Qt.AlignCenter)
        self.mic_label.setStyleSheet("""
            background-color: black;
            border-radius: 75px;
        """)
        self.mic_label.setGeometry(self.width()//2 - 75, self.height()//2 - 75, 150, 150)

        # Mic icon inside the circle
        self.mic_icon = QLabel(self.mic_label)
        self.mic_icon.setPixmap(QIcon("mic-Icon.png").pixmap(80, 80))
        self.mic_icon.setAlignment(Qt.AlignCenter)
        self.mic_icon.setGeometry(35, 35, 80, 80)

        # Pulsing animation
        self.anim = QPropertyAnimation(self.mic_label, b"geometry")
        self.anim.setDuration(700)
        self.anim.setStartValue(QRect(self.width()//2 - 75, self.height()//2 - 75, 150, 150))
        self.anim.setEndValue(QRect(self.width()//2 - 90, self.height()//2 - 90, 180, 180))
        self.anim.setLoopCount(-1)
        self.anim.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatBotUI()
    window.show()
    sys.exit(app.exec_())
