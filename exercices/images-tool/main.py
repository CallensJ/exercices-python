import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout, QLabel,
)


app = QApplication(sys.argv)


# Fenêtre principale
window = QWidget()
window.resize(700, 300)

window.setStyleSheet("""
    background-color: "green";
    color: white;;

""")


# Container
container = QWidget(window)

container.setStyleSheet("""
    background-color: #F2F2F2;
    border: 2px solid red;
""")

container.setGeometry(50, 50, 600, 150)

#label du container

label = QLabel("container1", container)



# Layout du container
container_layout = QHBoxLayout(container)


#bouton du premier container

left_button = QPushButton("button 1")
right_button = QPushButton("button 2")
left_button.setStyleSheet("color: black;")
right_button.setStyleSheet("color: black;")


#ajoute les boutons au premier container

container_layout.addWidget(left_button)
container_layout.addStretch()
container_layout.addWidget(right_button)
# container_layout.addWidget(label)




#second container
second_container = QWidget(window)

second_container.setStyleSheet("""
    background-color: #F6F6F6;
    border: 2px solid blue;
""")

second_container.setGeometry(150, 150, 600, 150)

#layout du second container
second_container_layout = QHBoxLayout(second_container)





window.show()

sys.exit(app.exec())