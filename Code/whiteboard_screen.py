"""
   Riya Jonnala, Suraj Narra, Gregory Cohen
   May 6, 2026

   Builds the TaskMaster whiteboard screen.
   This screen gives the user a text area for planning notes and scratch work.
"""

from PySide6.QtWidgets import QPushButton, QTextEdit, QWidget

from screen_helpers import build_button_row, build_page_layout


def build_whiteboard_screen(show_home_screen) -> QWidget:
    """
       build_whiteboard_screen() creates the whiteboard screen.
       inputs:
          show_home_screen: function - function that returns the app to the home screen
       returns a QWidget that contains a notes area for planning
    """

    # Create the main widget that will hold the whiteboard screen
    whiteboard_screen = QWidget()

    # Use the shared page layout so this screen matches the other screens
    layout = build_page_layout("Whiteboard")

    # Create a text area for planning notes
    notes_area = QTextEdit()

    # Add placeholder text that shows the purpose of the whiteboard
    notes_area.setPlaceholderText("Write planning notes or scratch work here")

    # Give the notes area enough room to be useful
    notes_area.setMinimumHeight(300)

    # Create a back button that returns to the home screen
    back_button = QPushButton("Back to Home")

    # Connect the back button to the home screen
    back_button.clicked.connect(show_home_screen)

    # Add the notes area to the screen
    layout.addWidget(notes_area)

    # Add the screen action button
    layout.addLayout(build_button_row([back_button]))

    # Attach the completed layout to the whiteboard screen
    whiteboard_screen.setLayout(layout)

    # Return the finished whiteboard screen
    return whiteboard_screen
