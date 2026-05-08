"""
   Riya Jonnala, Suraj Narra, Gregory Cohen
   May 6, 2026

   Starts the TaskMaster desktop application and opens the main PySide6 window.
   This file connects the app screens and controls screen navigation.a
"""

import sys
from typing import cast

from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

# import from
from enter_task_screen import build_enter_task_screen
from home_screen import build_home_screen
from schedule_screen import build_schedule_screen
from whiteboard_screen import build_whiteboard_screen


class TaskMasterWindow(QMainWindow):
    """
       TaskMasterWindow() builds the main desktop window for TaskMaster.
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

        # Build every screen before the user starts clicking navigation buttons
        self.home_screen = build_home_screen(
            self.show_enter_task_screen,
            self.show_schedule_screen,
            self.show_whiteboard_screen,
        )
        self.enter_task_screen = build_enter_task_screen(self.show_home_screen)
        self.schedule_screen = build_schedule_screen(self.show_home_screen)
        self.whiteboard_screen = build_whiteboard_screen(self.show_home_screen)

        # Add the home screen as the first screen in the stack
        self.screen_stack.addWidget(self.home_screen)

        # Add the task entry screen to the screen stack
        self.screen_stack.addWidget(self.enter_task_screen)

        # Add the schedule screen to the screen stack
        self.screen_stack.addWidget(self.schedule_screen)

        # Add the whiteboard screen to the screen stack
        self.screen_stack.addWidget(self.whiteboard_screen)

        # Put the screen stack in the center of the main window
        self.setCentralWidget(self.screen_stack)

    def show_home_screen(self) -> None:
        """
           show_home_screen() switches the app to the home screen.
           returns None because it only changes the visible screen
        """

        # Show the home screen in the screen stack
        self.screen_stack.setCurrentWidget(self.home_screen)

    def show_enter_task_screen(self) -> None:
        """
           show_enter_task_screen() switches the app to the task entry screen.
           returns None because it only changes the visible screen
        """

        # Show the task entry screen in the screen stack
        self.screen_stack.setCurrentWidget(self.enter_task_screen)

    def show_schedule_screen(self) -> None:
        """
           show_schedule_screen() switches the app to the schedule screen.
           returns None because it only changes the visible screen
        """

        # Show the schedule screen in the screen stack
        self.screen_stack.setCurrentWidget(self.schedule_screen)

    def show_whiteboard_screen(self) -> None:
        """
           show_whiteboard_screen() switches the app to the whiteboard screen.
           returns None because it only changes the visible screen
        """

        # Show the whiteboard screen in the screen stack
        self.screen_stack.setCurrentWidget(self.whiteboard_screen)


def create_app() -> tuple[QApplication, TaskMasterWindow]:
    """
       create_app() creates the QApplication and main TaskMaster window.
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
       main() starts TaskMaster.
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
