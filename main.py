from gui import App
from password_entry import PasswordEntry
from main_page import MainPage
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    with App() as app:
        kdb = app.popover(PasswordEntry())
        print("GROUPS", kdb.groups)

        app.frame(MainPage(kdb))

    app.start()
