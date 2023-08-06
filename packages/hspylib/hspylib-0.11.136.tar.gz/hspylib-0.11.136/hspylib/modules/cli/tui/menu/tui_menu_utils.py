from hspylib.core.namespace import Namespace
from hspylib.core.tools.commons import sysout
from hspylib.modules.cli.keyboard import Keyboard
from hspylib.modules.cli.tui.minput.input_validator import InputValidator
from hspylib.modules.cli.tui.minput.minput import minput, MenuInput
from hspylib.modules.cli.tui.tui_preferences import TUIPreferences
from hspylib.modules.cli.vt100.vt_utils import clear_screen
from hspylib.modules.eventbus import eventbus


class TUIMenuUtils:

    # fmt: off
    PREFS = TUIPreferences.INSTANCE or TUIPreferences()
    MENU_LINE = f"{'┅┅' * PREFS.title_line_length}"
    MENU_TITLE_FMT = (
        f"{PREFS.title_color}"
        f"┍{MENU_LINE}┓%EOL%"
        "┣{title:^" + str(2 * PREFS.title_line_length) + "s}┫%EOL%"
        f"┕{MENU_LINE}┙%EOL%%NC%"
    )
    # fmt: on

    @staticmethod
    def render_app_title() -> None:
        clear_screen()
        eventbus.emit("tui-menu-ui", "render-app-title")

    @staticmethod
    def wait_keystroke(wait_message: str = "%YELLOW%%EOL%Press any key to continue%EOL%%NC%") -> None:
        sysout(wait_message)
        Keyboard.wait_keystroke()

    @classmethod
    def prompt(
        cls,
        label: str,
        dest: str,
        validator: InputValidator = InputValidator.words()) -> Namespace:

        form_fields = MenuInput.builder() \
            .field() \
                .label(label) \
                .dest(dest) \
                .validator(validator) \
                .build() \
            .build()
        ret_val = minput(form_fields)
        cls.render_app_title()
        return ret_val

    @classmethod
    def title(cls, title_msg: str) -> None:
        sysout(cls.MENU_TITLE_FMT.format(title=title_msg or "TITLE"))
