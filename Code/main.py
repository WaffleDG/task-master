"""
   Riya Jonnala, Suraj Narra, Gregory Cohen
   May 5, 2026

   Starts the TaskMaster desktop application and opens the main PySide6 window.
   This file creates the home screen and navigation controls for the app.
"""

import sys
from typing import cast

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class TaskMasterWindow(QMainWindow):
    """
       TaskMasterWindow() -> QMainWindow builds the main desktop window for TaskMaster.
       returns a QMainWindow object that displays the TaskMaster GUI
    """

    def __init__(self) -> None:
        # Call the QMainWindow setup first so PySide6 can initialize the window correctly
        super().__init__()

        # Set the window title shown in the operating system title bar
        self.setWindowTitle("TaskMaster")

        # Set a reasonable starting size for a student planner desktop window
        self.resize(900, 600)

        # QStackedWidget stores the screens that can be shown in the main window
        self.screen_stack = QStackedWidget()

        # Add the home screen as the first visible screen
        self.screen_stack.addWidget(self.build_home_screen())

        # Put the screen stack in the center of the main window
        self.setCentralWidget(self.screen_stack)

    def build_home_screen(self) -> QWidget:
        """
           build_home_screen() -> QWidget creates the first TaskMaster landing screen.
           returns a QWidget that contains the home screen layout
        """

        # Create the main widget that will hold all home screen content
        home_screen = QWidget()

        # Use a vertical layout so the title, description, and buttons stack neatly
        layout = QVBoxLayout()

        # Keep the home screen from looking cramped against the window edges
        layout.setContentsMargins(80, 80, 80, 80)

        # Add consistent spacing between widgets
        layout.setSpacing(18)

        # Create the main app title
        title_label = QLabel("TaskMaster")

        # Center the title so it feels like the main home screen heading
        title_label.setAlignment(Qt.AlignCenter)

        # Give the title a larger font without needing a separate stylesheet file
        title_label.setStyleSheet("font-size: 36px; font-weight: 700;")

        # Create a short description of the application
        subtitle_label = QLabel("Desktop student planner")

        # Center the subtitle under the title
        subtitle_label.setAlignment(Qt.AlignCenter)

        # Make the subtitle readable but less visually important than the title
        subtitle_label.setStyleSheet("font-size: 18px; color: #555555;")

        # Create the navigation buttons for the main app sections
        enter_tasks_button = QPushButton("Enter Tasks")
        view_schedule_button = QPushButton("View Schedule")
        view_whiteboard_button = QPushButton("View Whiteboard")

        # Keep the buttons a consistent height for a cleaner first screen
        for button in (enter_tasks_button, view_schedule_button, view_whiteboard_button):
            # Set a readable button height for desktop use
            button.setMinimumHeight(44)

        # Add the title and subtitle to the screen
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)

        # Add stretchable empty space so the buttons sit comfortably below the heading
        layout.addStretch()

        # Add the navigation buttons to the screen
        layout.addWidget(enter_tasks_button)
        layout.addWidget(view_schedule_button)
        layout.addWidget(view_whiteboard_button)

        # Add stretchable empty space below the buttons to balance the layout
        layout.addStretch()

        # Attach the completed layout to the home screen widget
        home_screen.setLayout(layout)

        # Return the finished screen so the main window can display it
        return home_screen


def create_app() -> tuple[QApplication, TaskMasterWindow]:
    """
       create_app() -> tuple[QApplication, TaskMasterWindow] creates the QApplication and main TaskMaster window.
       returns a tuple containing QApplication and TaskMasterWindow objects
    """

    # Create the Qt application object that manages the GUI event loop
    app: QApplication = QApplication(sys.argv)

    # Create the main TaskMaster window
    window: TaskMasterWindow = TaskMasterWindow()

    # Return both objects so the program startup stays organized
    return app, window


def main() -> int:
    """
       main() -> int starts TaskMaster.
       returns an int exit code that represents whether the app started successfully
    """

    # Create the application and main window
    app, window = create_app()

    # Show the main window to the user
    window.show()

    # Start the PySide6 event loop and return its exit code
    return cast(int, app.exec())


if __name__ == "__main__":
    # Run the application when this file is executed directly
    sys.exit(main())
