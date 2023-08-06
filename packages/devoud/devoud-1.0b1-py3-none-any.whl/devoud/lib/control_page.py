from .devoud_data import *
from .devoud_data import __version__, program_name
from .styles import StylizedWindow
from .browser_embedded_view import EmbeddedPage, EmbeddedWidget
import os
import sys


class ControlPage(EmbeddedPage):
    title = 'Панель управления'
    url = 'devoud://control'

    def __init__(self, parent):
        super().__init__(parent)
        self.theme = StylizedWindow(FS.user_settings, FS.get_option('theme'))

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.sections_panel = QListWidget(self)
        self.sections_panel.setObjectName('sections_panel')
        self.sections_panel.setFrameShape(QListWidget.NoFrame)
        self.sections_panel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sections_panel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main_layout.addWidget(self.sections_panel)

        self.stacked_widget = QStackedWidget(self)  # всё что справа от панели вкладок
        self.stacked_widget.setObjectName('stacked_widget')
        self.sections_panel.currentRowChanged.connect(self.stacked_widget.setCurrentIndex)
        self.sections_panel.setCurrentRow(0)
        self.main_layout.addWidget(self.stacked_widget)

        self.settings_section = self.Section(self.stacked_widget, './ui/custom/svg/settings.svg')
        self.history_section = self.Section(self.stacked_widget, './ui/custom/svg/history.svg')
        self.bookmarks_section = self.Section(self.stacked_widget, './ui/custom/svg/bookmark_empty.svg')
        self.downloads_section = self.Section(self.stacked_widget, './ui/custom/svg/downloads.svg')

        # Виджет "О программе"
        self.about_widget = EmbeddedWidget(self.settings_section, 'О программе')
        self.browser_icon = QLabel(self.about_widget)
        self.browser_icon.setPixmap(QPixmap("./ui/svg/browser_icon.svg"))
        self.browser_icon.setFixedSize(QSize(85, 85))
        self.browser_icon.setScaledContents(True)
        self.about_widget.content_layout.addWidget(self.browser_icon, 0, 0)
        self.about_widget.content_layout.addWidget(QLabel(self.about_widget,
                                                          text=f'{program_name} {__version__} \nРазработал OneEyedDancer\nс '
                                                               f'использованием '
                                                               f'PySide6 под лицензией GPL3'), 0, 1)

        # Виджет настроек
        self.settings_widget = EmbeddedWidget(self.settings_section, 'Настройки')

        # Кнопка перезапуска
        self.restart_button = QPushButton(self.settings_widget, icon=QIcon('./ui/custom/svg/restart.svg'), text='!')
        self.restart_button.setFixedSize(40, 22)
        self.restart_button.setObjectName('widget_title_button')
        self.restart_button.setToolTip('Для применения настроек требуется перезапуск')
        self.restart_button.setHidden(True)
        self.restart_button.clicked.connect(lambda: os.execv(sys.executable, ['python'] + sys.argv))
        self.settings_widget.title_layout.addWidget(self.restart_button)

        self.history_checkbox = self.CheckBox('Сохранять историю', 'saveHistory', self.save_history,
                                              'При выключении удаляет историю')
        self.settings_widget.content_layout.addWidget(self.history_checkbox, 0, 0)
        self.tabs_checkbox = self.CheckBox('Восстанавливать вкладки', 'restoreTabs',
                                           lambda: FS.save_option('restoreTabs'),
                                           'Восстанавливает последнюю сессию браузера')
        self.settings_widget.content_layout.addWidget(self.tabs_checkbox, 1, 0)
        self.easyprivacy_checkbox = self.CheckBox('EasyPrivacy', 'easyprivacy', self.easy_privacy,
                                                  'Блокирует шпионские трекеры, может вызвать медленную работу браузера')
        self.settings_widget.content_layout.addWidget(self.easyprivacy_checkbox, 2, 0)
        self.systemframe_checkbox = self.CheckBox('Системная рамка окна', 'systemWindowFrame', self.system_window_frame)
        self.settings_widget.content_layout.addWidget(self.systemframe_checkbox, 3, 0)

        self.home_lineedit = QLineEdit(self.settings_widget)
        self.home_lineedit.setFixedSize(QSize(215, 24))
        self.home_lineedit.setFocusPolicy(Qt.ClickFocus)
        self.home_lineedit.textEdited.connect(lambda: FS.save_option('homePage', self.home_lineedit.text()))
        self.home_lineedit.setText(FS.get_option('homePage'))
        self.settings_widget.content_layout.addWidget(self.home_lineedit, 4, 0)
        self.settings_widget.content_layout.addWidget(QLabel(self.settings_widget, text='Домашняя страница'), 4, 1)

        self.new_page_box = QComboBox(self.settings_widget)
        [self.new_page_box.addItem(text) for text in new_page_dict.keys()]
        self.new_page_box.setFixedSize(QSize(215, 24))
        self.new_page_box.setFocusPolicy(Qt.ClickFocus)
        self.new_page_box.setCurrentText(FS.get_option('newPage'))
        self.new_page_box.currentIndexChanged.connect(self.change_new_page)
        self.settings_widget.content_layout.addWidget(self.new_page_box, 5, 0)
        self.settings_widget.content_layout.addWidget(QLabel("Новая страница"), 5, 1)

        self.search_box = QComboBox(self.settings_widget)
        [self.search_box.addItem(QIcon(search_engines[key][2]), key) for key in search_engines.keys()]
        self.search_box.setFixedSize(QSize(215, 24))
        self.search_box.setFocusPolicy(Qt.ClickFocus)
        self.search_box.setCurrentText(FS.get_option('searchEngine'))
        self.search_box.currentIndexChanged.connect(self.change_default_search)

        self.save_button = QPushButton(self.settings_widget)
        self.save_button.setFixedSize(self.save_button.iconSize().width() + 20, 22)
        self.save_button.setObjectName('widget_title_button')
        self.save_button.setToolTip('Сохранить файл конфигурации вне каталога программы')
        self.save_button.setHidden(FS.os_user_path_exist())
        self.save_button.clicked.connect(self.save_data)
        self.settings_widget.title_layout.addWidget(self.save_button)

        self.settings_widget.content_layout.addWidget(self.search_box, 6, 0)
        self.settings_widget.content_layout.addWidget(
            QLabel(self.settings_widget, text='Поисковая система по умолчанию'), 6,
            1)

        # Виджет тем
        self.themes_widget = EmbeddedWidget(self.settings_section, 'Темы')
        self.themes_buttons_list = []
        self.create_themes_buttons()
        self.themes_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.themes_widget.content_layout.addItem(self.themes_spacer, 0, 5)

        # Scroll Spacer
        self.content_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.settings_section.layout().addItem(self.content_spacer)

        # История и закладки
        self.lists = [self.EmbeddedWidgetList(self.history_section, 'История', 'history'),
                      self.EmbeddedWidgetList(self.bookmarks_section, 'Закладки', 'bookmarks')]

        self.change_style()
        self.update_lists()

    def create_themes_buttons(self):
        for root, dirs, files_ in os.walk("./ui/themes"):
            for count, filename in enumerate(files_):
                with open(f"{root}/{filename}", 'r') as theme_file:
                    data = json.load(theme_file)
                    btn = QPushButton(self)
                    btn.setFixedSize(20, 20)
                    btn.setObjectName(filename.rpartition('.')[0])
                    btn.setStyleSheet(f"""
                            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                            stop:0 {data['tab_widget']['bg_select']}, 
                            stop:1 {data['tab_widget']['bg']});
                            border-radius: 10px;""")
                    btn.clicked.connect(self.apply_theme)
                    self.themes_buttons_list.append(btn)
                    self.themes_widget.content_layout.addWidget(btn, 0, count)

        self.set_select_icon(FS.get_option('theme'))

    def change_style(self):
        self.setStyleSheet(self.theme.control_page())

        # обновить цвет иконок
        self.settings_section.tab_item.setIcon(QIcon('./ui/custom/svg/settings.svg'))
        self.history_section.tab_item.setIcon(QIcon('./ui/custom/svg/history.svg'))
        self.bookmarks_section.tab_item.setIcon(QIcon('./ui/custom/svg/bookmark_empty.svg'))
        self.downloads_section.tab_item.setIcon(QIcon('./ui/custom/svg/downloads.svg'))
        self.restart_button.setIcon(QIcon('./ui/custom/svg/restart.svg'))
        self.save_button.setIcon(QIcon('./ui/custom/svg/save.svg'))
        [widget.clean_button.setIcon(QIcon('./ui/custom/svg/clean.svg')) for widget in self.lists]

    def set_select_icon(self, select_theme=FS.default_settings['theme']):
        for button in self.themes_buttons_list:
            if button.objectName() == select_theme:
                button.setIcon(QIcon("./ui/custom/svg/select.svg"))
            else:
                button.setIcon(QIcon("./ui/png/void.png"))

    def apply_theme(self):
        selected_theme = self.sender().objectName()
        FS.save_option('theme', selected_theme)
        self.theme = StylizedWindow(FS.user_settings, FS.get_option('theme'))

        self.window().change_style(self.theme)
        self.change_style()
        self.set_select_icon(selected_theme)
        print('[Стили]: Применена тема', selected_theme)

    def update_lists(self):
        for widget in self.lists:
            widget.list.clear()
            with open(f'{FS.config_dir()}/{widget.file_name}', 'r') as file:
                items = file.read().splitlines()
            items.reverse()
            for site in range(len(items)):
                widget.list.addItem(items[site])

    def change_default_search(self):
        FS.save_option('searchEngine', self.search_box.currentText())
        global new_page
        new_page = new_page_dict.get(FS.get_option('newPage'))()

    def change_new_page(self):
        global new_page
        page = self.new_page_box.currentText()
        FS.save_option('newPage', page)
        new_page = new_page_dict.get(page)()

    def save_history(self):
        if FS.get_option('saveHistory'):
            with open(f'{FS.config_dir()}/history', 'w') as history_file:
                history_file.write('')
                self.lists[0].list.clear()
        FS.save_option('saveHistory')

    def easy_privacy(self):
        self.restart_button.setHidden(False)
        FS.save_option('easyprivacy')

    def system_window_frame(self):
        self.restart_button.setHidden(False)
        FS.save_option('systemWindowFrame')

    def save_data(self):
        if FS.os_user_path_exist():
            QMessageBox.critical(self, "Ошибка операции", f'Файл конфигурации уже был сохранен в каталоге пользователя '
                                                          f'системы, его текущее местоположение: ({FS.config_path()})')
            return self.save_button.setHidden(True)
        if QMessageBox.question(self, 'Сохранение данных', f'Сохранить конфигурацию в каталоге текущего '
                                                           f'пользователя системы?\n\n') == QMessageBox.Yes:
            if FS.create_os_user_path():
                QMessageBox.information(self, 'Операция завершена', 'Копирование конфигурации завершено успешно!')
                self.save_button.setHidden(True)
            else:
                QMessageBox.critical(self, 'Ошибка операции', 'Во время копирования конфигурации произошла ошибка!')

    class Section(QScrollArea):
        def __init__(self, parent: QStackedWidget, icon: str):
            super().__init__(parent)
            self.setFrameShape(QFrame.NoFrame)
            self.vertical_layout = QVBoxLayout(self)
            self.vertical_layout.setContentsMargins(0, 0, 0, 0)
            self.icon = QIcon(icon)
            self.tab_list = parent.parent().sections_panel
            self.tab_list.setIconSize(QSize(25, 25))
            self.tab_item = QListWidgetItem(self.icon, "", self.tab_list)
            self.tab_item.setSizeHint(QSize(16777215, 40))
            self.parent().addWidget(self)

    class CheckBox(QCheckBox):
        def __init__(self, text, option, command, tooltip=None):
            super().__init__(text)
            if tooltip is not None:
                self.setToolTip(tooltip)
            self.setMinimumSize(QSize(0, 25))
            self.setChecked(FS.get_option(option))
            self.stateChanged.connect(command)

    class EmbeddedWidgetList(EmbeddedWidget):
        def __init__(self, parent, title: str, file_name: str):
            super().__init__(parent, title)
            self.file_name = file_name
            self.clean_button = QPushButton(self, icon=QIcon('./ui/custom/svg/clean.svg'), text='Очистить всё')
            self.clean_button.setFixedSize(120, 22)
            self.clean_button.setObjectName('widget_title_button')
            self.clean_button.clicked.connect(lambda: self.remove_from_list(all=True))
            self.title_layout.addWidget(self.clean_button)

            self.clean_select_button = QPushButton(self, text='Удалить')
            self.clean_select_button.setFixedSize(70, 22)
            self.clean_select_button.setObjectName('widget_title_button')
            self.clean_select_button.setToolTip('Удалить выбранное')
            self.clean_select_button.setHidden(True)
            self.clean_select_button.clicked.connect(lambda: self.remove_from_list())
            self.title_layout.addWidget(self.clean_select_button)

            self.list = QListWidget(self)
            self.list.itemClicked.connect(lambda: self.clean_select_button.setHidden(False))
            self.list.itemDoubleClicked.connect(
                lambda: self.open_from_list())
            self.content_layout.addWidget(self.list)

        def remove_from_list(self, all=False):
            item = self.list.currentRow()
            path = f'{FS.config_dir()}/{self.file_name}'
            with open(path, 'r') as file:
                items = file.read().splitlines()
                if not items:
                    return
                del items[item]
            with open(path, 'w') as file:
                if all:
                    file.write('')
                    return self.list.clear()
                items = '\n'.join(items)
                file.write(items)
            self.list.takeItem(item)

        def open_from_list(self):
            self.window().address_edit.setText(self.list.currentItem().text())
            self.window().tab_widget.current().load(self.list.currentItem().text())
